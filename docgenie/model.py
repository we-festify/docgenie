from .models import supported_models
from dotenv import load_dotenv
load_dotenv()

class Model:
    def __init__(self, name, config):
        self.name = name
        self.model = None
        self.config = config
        if not self.config:
            self.config = {}

        self.loadModel()

    def loadModel(self):
        if self.name not in supported_models:
            print(f"\u001b[31mModel {self.name} is not supported.\u001b[0m")
            exit(1)
        model_class = supported_models[self.name]
        self.model = model_class(self.name, self.config)
        
    def generateContent(self, prompt: str = ""):
        if self.model is None:
            print("\u001b[31mModel not loaded correctly. Please check the configuration.\u001b[0m")
            exit(1)
        return self.model.generateContent(prompt) + "\n\n" + "The documentation is generated using AI by docgenie. If you found any issues, please report them to the team."
    