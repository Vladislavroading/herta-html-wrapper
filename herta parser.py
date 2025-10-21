open("log.txt", "w")

""" 
    herta design parser to html
    in development
"""
import getpass
import time
import os
import log as logger
import parser as herta_parser
import tokenizer
import sys

if len(sys.argv) < 3:
    file_path = input("file path :: ")
    output_path = input("output path ::")
    log.log("PARSER", "INFO", f"Succesfully inputed file path and output path: {file_path}, {output_path}")
else:
    file_path = sys.argv[1]
    output_path = sys.argv[2]


parser = herta_parser.parser()

log = logger.log()

token = tokenizer.tokenizer()



data = {
    "herta parser version": "0.0.1",
    "user": getpass.getuser(),
    "time-stamp": time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
    "platform": os.name,
    "file": file_path
}
print(f"telemetry :: {data}")
log.log("DATA", "INFO", "Telemetry collected successfully")

tokens = token.tokenize(open(file_path).read())
if tokens["tokenized"] is True:
    log.log("TOKENIZER", "None", "Tokenizer finished work succesfully")
    print(tokens["content"])
else:
    log.log("TOKENIZER", "EXTREME", "Tokenizer output error, output most probably corrupted")
    exit("Tokenizer error...")
content = parser.parser(tokens["content"], output_path)
print(content)
output = parser.create_html(content)
