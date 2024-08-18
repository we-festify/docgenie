import os

class Gemini:
    def __init__(self, model_name: str, generation_config):
        self.api_key = os.getenv("DOCGENIE_MODEL_API_KEY")
        if self.api_key is None or self.api_key == "":
            print("\u001b[31mAPI key not found. Please set DOCGENIE_MODEL_API_KEY in the environment variables.\u001b[0m")
            exit(1)
        self.model_name = model_name
        self.generation_config = generation_config

        self.loadModel()

    def loadModel(self):
        import google.generativeai as genai
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config,
        )

    def generateContent(self, prompt: str = "") -> str:
        response = self.model.generate_content(prompt).text
        return response