import os

def readFile(srcDir, inputFile):
    path = os.path.join(srcDir, inputFile)
    path = os.path.abspath(path)
    print(f"\u001b[90m{path}\u001b[0m")
    path = os.path.abspath(path)
    with open(path, "r") as file:
        return file.read()
    
def writeFile(srcDir: str, outputFile: str, content: str) -> None:
    path = os.path.join(srcDir, outputFile)
    path = os.path.abspath(path)
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, "w") as file:
        file.write(content)

def getOutputExtension(format):
    return {
        "markdown": ".md",
        "html": ".html",
        "text": ".txt",
    }.get(format, ".md")
