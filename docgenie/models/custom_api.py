import os
from ..utils.terminal import red, gray

class CustomAPI:
    def __init__(self, model_name: str, generation_config):
        self.api_key = os.getenv("DOCGENIE_MODEL_API_KEY")
        self.model_name = model_name
        self.generation_config = generation_config

        self.loadModel()
        
    def loadModel(self):
        try:
            import requests

            headers = self.generation_config.get("headers", {})
            query_params = self.generation_config.get("query", {})
            api_url = self.generation_config.get("url", "")
            
            # replace {DOCGENIE_MODEL_API_KEY} with the actual API key
            for key, value in headers.items():
                headers[key] = value.replace("{DOCGENIE_MODEL_API_KEY}", self.api_key)
            for key, value in query_params.items():
                query_params[key] = value.replace("{DOCGENIE_MODEL_API_KEY}", self.api_key)
            api_url = api_url.replace("{DOCGENIE_MODEL_API_KEY}", self.api_key)

            self.headers = headers
            self.query_params = query_params
            self.api_url = api_url

        except ImportError:
            print(red("Please install the dependencies by running the following commands:\n"))
            print(gray("pip install requests"))
            print()
            exit(1)
        except Exception as e:
            print(f"\u001b[31mError loading Custom API model: {str(e)}\u001b[0m")
            exit(1)

    def generateContent(self, prompt: str = "") -> str:
        import requests
        response = requests.get(self.api_url, headers=self.headers, params=self.query_params)
        response = response.text
        return response