import log as logger
log = logger.log()

##lolz
"""
.-.. --- .-..
parser to data
format which
will be readable
to the app
.-.. --- .-..
"""

import pathlib
import os
import json

current_file_path = pathlib.Path(__file__).resolve()
current_file_directory = current_file_path.parent


class parser:
    def __init__(self):
        self.name = "Parser"
        self.version = "v0.0.1"
        self.tokens_to_html = json.loads(open("tokens.json", "r").read())["tokens"]["html_base"]
        self.container = ["<!DOCTYPE html>", "<html>"]
        self.closing = ["</html>"]
        log.log("DATA", "INFO", f"New {self.name} instance, location: {current_file_path}, name: {self.name}, version: {self.version}")
    def parser(self, content, output_path):
        lines = content.strip().split('\n')
        result = {
            "path": output_path,
            "container": self.container,
            "content": {
                "style": [],
                "head": [],
                "body": []
            },
            "closing": self.closing
        }
        
        current_section = None
        current_content = []
        
        current_section = None

        for line in lines:
            stripped = line.strip()
            
            # Check closes FIRST (to avoid "11" matching "1")
            if stripped.startswith("11"):
                current_section = None
            elif stripped.startswith("22"):
                current_section = None
            elif stripped.startswith("33"):
                current_section = None
            # Then check opens
            elif stripped.startswith("1"):
                current_section = "style"
            elif stripped.startswith("2"):
                current_section = "head"
            elif stripped.startswith("3"):
                current_section = "body"
            # Everything else is content for the current section
            else:
                if current_section and stripped:  # Don't append empty lines
                    result["content"][current_section].append(stripped)
                    """lolz"""     
            print(result)
        return result
    def create_html(self, content):
        """Create HTML file from parser's dict structure"""
        try:
            html = f"{content['container'][0]}\n{content['container'][1]}\n"

            # Add style content 
            style_content = content["content"]["style"]
            html += "<style>\n"
            for text in style_content:
                html += f"    {text}\n"
            html += "</style>\n"


            # Open head
            html += "<head>\n"

            # Add other head content
            head_content = content["content"]["head"]
            for text in head_content:
                html += f"    {text}\n"

            # Close head
            html += "</head>\n"

            

            # Add body content
            html += "<body>\n"
            body_content = content["content"]["body"]
            for text in body_content:
                html += f"    {text}\n"
            html += "</body>\n"

            # Close html
            for closing_tag in content["closing"]:
                html += f"{closing_tag}\n"

            # Write to file
            with open(content["path"], "w", encoding="utf-8") as f:
                f.write(html)

            log.log("PARSER", "INFO", f"HTML written to {content['path']}")
            return True

        except Exception as e:
            log.log("PARSER", "EXTREME", f"Error creating HTML: {e}")
            return False
