import datetime

class log:
    def __init__(self):
        self.path = "log.txt"
    def log(self, log_type, insanity, text):
        timestamp = datetime.datetime.now().isoformat()
        with open(self.path, "a") as w:
            w.write(f"""
                [{timestamp}] <<warning level :: {insanity}>>  <type :: {log_type}> {text}
                """)
            
