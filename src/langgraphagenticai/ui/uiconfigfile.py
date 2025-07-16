from configparser import ConfigParser

class Config:
    def __init__(self,config_file=".\\src\\langgraphagenticai\\ui\\uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTION").split(", ")
    
    def get_usercase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTION").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTION").split(", ")
    

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")