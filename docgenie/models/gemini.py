import os
from ..utils.terminal import red, gray

class Gemini:
    def __init__(self, model_name: str, generation_config):
        self.api_key = os.getenv("DOCGENIE_MODEL_API_KEY")
        if self.api_key is None or self.api_key == "":
            print(red("Gemini API key not found. Please set DOCGENIE_MODEL_API_KEY in the environment variables as your Gemini API key."))
            exit(1)
        self.model_name = model_name
        self.generation_config = generation_config

        self.loadModel()
        
    def loadModel(self):
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=self.generation_config,
            )
        except ImportError:
            print(red("Please install the dependencies by running the following commands:\n"))
            print(gray("pip install google-generativeai"))
            print()
            exit(1)
        except Exception as e:
            print(red("Error loading Gemini model: {str(e)}"))
            exit(1)

    def generateContent(self, prompt: str = "") -> str:
        response = self.model.generate_content(prompt).text
        return response