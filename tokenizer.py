import log as logger
import pathlib
log = logger.log()
import json

current_file_path = pathlib.Path(__file__).resolve()
current_file_directory = current_file_path.parent

class tokenizer:
    def __init__(self):
        self.name = "Tokenizer"
        self.version = "v0.1"
        log.log("DATA", "INFO", f"New tokenizer instance, location: {current_file_path}, name: {self.name}, version: {self.version}")
        self.tokens = json.loads(open("tokens.json", "r").read())["tokens"]
        print(self.tokens)
    def tokenize(self, content):
        try:
            """From input create tokenized version, which
            will will be readed by other modules and create HTML"""
            
            """content check"""
            if content is None or content == "":
                log.log("TOKENIZER", "EXTREME", "Content wasn't provided, tokenizer can't continue it's work...")
                raise ValueError("ERROR | EXTREME | Content wasn't provided, tokenizer can't continue it's work...")
            
            """tokenization"""
            for key, value in self.tokens["primary_tokens"].items():
                content = content.replace(key, value)
            for key, value in self.tokens["tokens"].items():
                content = content.replace(key, value)
            log.log("TOKENIZER", "INFO", "Tokenization completed successfully")
            context = {
                "content": content,
                "tokenized": True
            }

            return context
        except Exception as e:
            log.log("TOKENIZER", "EXTREME", f"Tokenizer error: {e}")
            return {"content": None,
                    "tokenized": False
                    }