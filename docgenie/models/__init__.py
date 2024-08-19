from .gemini import Gemini
from .custom_api import CustomAPI

supported_models = {
    "gemini-1.5-flash": Gemini,
    "custom-api": CustomAPI,
}