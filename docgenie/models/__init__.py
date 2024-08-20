from .gemini import Gemini
from .custom_api import CustomAPI

supported_models = {
    # Gemini models
    "gemini-1.0-pro": Gemini,
    "gemini-1.5-pro": Gemini,
    "gemini-1.5-flash": Gemini,

    # Custom API model
    "custom-api": CustomAPI,
}