#Any import statements for custom functions included in the answering function
#should be listed at the top. Required imports are necessary.
import re #REQUIRED - For Pattern Matching
import json #REQUIRED - For searching through json of questions
import importlib #REQUIRED - Necessary for trying to import files within this file
dir = "colleges.002835.BFOR203" #REQUIRED - Specify the file location in order for custom files and the question bank to be loaded. Use periods to seperate directories
ip_func = importlib.import_module(f"{dir}.ip") #OPTIONAL - Custom file for the math required on this test. Full path from colleges must be included

#This is the function that should contain all the code necessary
#to find an answer for a given question. It should list all
#custom questions, and if applicable call a search through a
#question bank
def return_answer (que):

    #Many non word bank questions will rely on regex formulas, which should be learned when creating
    #custom functions
    if re.compile("What is the network ID of [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\/[0-9]+").match(que):
        ip = que.split(" ")[len(que.split(" "))-1]
        subnet = ip.split("/")[1]
        binary_list = ip_func.ip_to_binary_list(ip.split("/")[0])
        return ip_func.binary_list_to_ip(ip_func.find_sub_ip(binary_list,subnet,"network"))

    if re.compile("What is Broadcast IP of [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\/[0-9]+").match(que):
        ip = que.split(" ")[len(que.split(" "))-1]
        subnet = ip.split("/")[1]
        binary_list = ip_func.ip_to_binary_list(ip.split("/")[0])
        return ip_func.binary_list_to_ip(ip_func.find_sub_ip(binary_list,subnet,"broadcast"))

    if re.compile("How many useable hosts are in the network with [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\/[0-9]+ *").match(que):
        subnet = que.split("/")[1].split(" ")[0]
        return 2**(32-int(subnet))-2

    if re.compile("In classful addressing\.\.\. what class is this ip address in [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\/[0-9]+ *").match(que):
        ip = que.split("/")[0].split(" ")[len(que.split("/")[0].split(" "))-1]
        return ip_func.ip_class(ip)

    if re.compile("How many \/[0-9]+'s networks are in a \/[0-9]+ network\? *").match(que):
        a = int(que.split("/")[1].split("'")[0])
        b = int(que.split("/")[2].split(" ")[0])
        return 2**(a-b)

    if re.compile("Convert from Binary TO Decimal the following (\-|\:) [01]+").match(que):
        return int(que.split(" ")[len(que.split(" "))-1],2)

    if re.compile("Convert from Decimal TO Binary the following (\-|\:) [0-9]+").match(que):
        return ip_func.x_bin(que.split(" ")[len(que.split(" "))-1],0)

    #Before the final return statement, a question bank search should be completed if applicable
    return search_question_bank(que)
    
    #Return undefined if the value is not found, this will ensure when submitting the user is warned these
    #answers were missing. Only use this if there is no question bank to search, and comment out the above 

    #return None

#This searches the local bank.json file for any question/answer pairs, and returns None if they are not found
def search_question_bank (que):
    dir2 = dir.replace(".","/")
    with open(f"{dir2}/bank.json", "r") as bank:
        parsed_bank = json.load(bank)
        if que in parsed_bank:
            return parsed_bank[que]
    return None


