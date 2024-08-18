import os
import json
import time
from .model import Model
from .prompts import generatePrompt
from .utils.file import readFile, writeFile, getOutputExtension
from .utils.patterns import doesMatchPattern
from .utils.languages import getImportPathsFromCode

def loadConfig():
    global __docgenie_config
    global __model
    global ROOT_DIR

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        with open("docgenie.config.json", "r") as file:
            __docgenie_config = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("docgenie.config.json file not found. Please create the file with the required configuration.")
    except Exception:
        __docgenie_config = {}

    MODEL_NAME = __docgenie_config.get("agent", {}).get("name", "custom")
    MODEL_CONFIG = __docgenie_config.get("agent", {}).get("config", {})
    ROOT_DIR = __docgenie_config.get("root_dir", ROOT_DIR)

    __model = Model(MODEL_NAME, MODEL_CONFIG)

def generateCodePromptForFile(src_dir, input_file, depth, isMainFile=False):
    if depth == 0:
        return ""

    # source code
    code = readFile(src_dir, input_file)

    # import paths
    file_extension = os.path.splitext(input_file)[1]
    import_paths = getImportPathsFromCode(code, file_extension, src_dir)

    # prompt
    file_path = os.path.normpath(os.path.join(src_dir, input_file))
    file_prefix = "Main File" if isMainFile else "File"
    prompt = f"{file_prefix}: {file_path}"
    prompt += "\n```" + file_extension[1:] + "\n"
    prompt += code
    prompt += "```\n"

    for import_file in import_paths:
        try:
            new_src_dir = os.path.join(src_dir, os.path.dirname(import_file))
            import_file = os.path.basename(import_file)
            prompt += generateCodePromptForFile(new_src_dir, import_file, depth - 1)
        except Exception:
            pass
    
    return prompt

def generateDocsForRule(rule):
    docs_type = rule["type"] if "type" in rule else "general"
    dir = rule["dir"] if "dir" in rule else "."
    include_patterns = rule["include"] if "include" in rule else []
    exclude_patterns = rule["exclude"] if "exclude" in rule else []
    output_path = rule["output"] if "output" in rule else dir
    max_depth = rule["depth"] if "depth" in rule else 1
    output_format = rule["format"] if "format" in rule else "markdown"
    additional_prompt = rule["prompt"] if "prompt" in rule else ""

    dir_path = os.path.join(ROOT_DIR, dir)
    if not os.path.exists(dir_path):
        print(f"Directory '{dir_path}' does not exist")
        return

    for file in os.listdir(dir_path):
        # skip if folder
        if os.path.isdir(os.path.join(dir_path, file)):
            continue
        # skip if file matches exclude patterns
        if doesMatchPattern(file, exclude_patterns):
            continue
        # process if file matches include patterns
        if doesMatchPattern(file, include_patterns):
            # generate prompt
            code_prompt = generateCodePromptForFile(dir_path, file, max_depth, True)
            prompt = generatePrompt(code_prompt, docs_type, output_format, additional_prompt)

            # generate documentation
            print(file, end=": ")
            timer = time.time()
            response = __model.generateContent(prompt)
            print(f"{time.time() - timer:.2f} seconds")

            # write to file
            try:
                output_file = os.path.splitext(file)[0] + getOutputExtension(output_format)
                writeFile(output_path, output_file, response)
            except Exception:
                print(f"Error writing to file {output_file}. Skipping...")
    
def main():
    # Load configuration
    loadConfig()

    global __docgenie_config
    rules = __docgenie_config["rules"] if "rules" in __docgenie_config else []

    # Generate documentation for each rule
    timer = time.time()
    for rule in rules:
        generateDocsForRule(rule)
    print(f"Generated documentation in {time.time() - timer:.2f} seconds")

if __name__ == "__main__":
    main()