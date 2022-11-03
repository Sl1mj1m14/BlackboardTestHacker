import json
import html_to_json
import sys
import os
import importlib
import jsbuilder
from dotenv import load_dotenv

QUESTION_DIV = "takeQuestionDiv" #This is the class of html divs containing questions

#Sets the college, class, and filename from the .env variable
load_dotenv()
college = os.getenv("COLLEGE")
class_code = os.getenv("CLASS")
file_name = os.getenv("FILE")

#Checks for command line arguments to manually set the college, class, and file name
#Format for arguments is "[college|class|file]="
for arg in sys.argv:
    if arg == os.path.basename(__file__):
        continue
    if arg.startswith("college="):
        college = arg.split("=")[1]
        continue
    if arg.startswith("class="):
        class_code = arg.split("=")[1]
        continue
    if arg.startswith("file="):
        file_name = arg.split("=")[1]
        continue

#Setting the directory path for the class file
dir = "colleges." + college + "." + class_code + ".main"

#Importing the class file
course = importlib.import_module(dir)

#Reading html source
with open(file_name,"r", encoding='utf-8') as html_file:
    html_text = html_file.read()

print("Converting to JSON...")

#Converting html source to json
with open("temp/temp.json","w") as json_file:
    json.dump(html_to_json.convert(html_text),json_file)

#Extracting all divs from the form. This path will likely be the cause of issues in case of updates, these searches should be performed dynamically in the future
with open("temp/temp.json","r") as json_file:
    form = json.load(json_file)['html'][0]['body'][0]['div'][5]['div'][1]['div'][0]['div'][0]['div'][0]['div'][0]['div'][1]['form'][0]['input'][0]['div'][2]['div']

#Deleting the temp file
os.remove("temp/temp.json")

#Sorting out only the divs that contain the question class
question_divs = []
for element in form:
    if element["_attributes"]['class'][0] == QUESTION_DIV:
        question_divs.append(element)

console_commands = []
for element in question_divs:
    print (element['h3'][0]['_value'])
    #Path for the plain text question
    question = element['div'][0]['ol'][0]['li'][0]['div'][0]['fieldset'][0]['legend'][0]['html'][0]['body'][0]['div'][0]['_value']
    print (question)
    answer = course.return_answer(question)
    print (answer)
    #Path for the id of the input element. This likely only works for text input questions, more testing should be done
    id = element['div'][0]['ol'][0]['li'][0]['div'][0]['fieldset'][0]['input'][0]['_attributes']['id']
    print (id)
    #Retreiving the answer from the question, returns None if the answer is not found
    console_commands.append(jsbuilder.value_set(answer,id))
    print (console_commands[len(console_commands)-1])
    #Path for the type of input. Will probably be useful in the future
    #print (element['div'][0]['ol'][0]['li'][0]['div'][0]['fieldset'][0]['input'][0]['_attributes']['type'])
    print("\n")

#Writing javascript commands to file
validity = jsbuilder.write_js(console_commands)
print (f"Output Dumped: \n{len(question_divs)} Questions Attempted \n{validity} Questions Answered")

