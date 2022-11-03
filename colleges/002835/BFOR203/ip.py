OCTET = 8
IP_SECTOR_LENGTH = 4

#Returns an ip in a binary form as a string
def ip_to_binary_string (ip):

    if not is_ip:
        return False

    #Removing the subnet if a subnet was included in the parameter
    if "/" in ip:
        ip = ip.split("/")[0]

    sectors = ip.split(".")

    binary_string = ""

    for sector in sectors:
        binary_string += x_bin(sector,OCTET)

    return binary_string

#Returns an ip in a binary form as an array
def ip_to_binary_list (ip):
    return [*ip_to_binary_string(ip)]

#Returns a binary list as an ip string in format x.x.x.x
def binary_list_to_ip (bin_list):

    return_ip = ""

    for x in range(IP_SECTOR_LENGTH):
        return_octet = ""

        for y in range (OCTET):
            return_octet += bin_list[(x*OCTET) + y]

        return_ip += str(int(return_octet,2)) + "."

    return return_ip.rstrip(".")

    
#Checks if the IP address is in format: x.x.x.x
def is_ip (ip):

    #Checking string to make sure there are 4 sectors
    if type(ip) is str and len(ip.split(".")) == IP_SECTOR_LENGTH:
        return True

    return False

#Finds the network ip or broadcast ip of the specified ip and subnet
def find_sub_ip (bin_list, subnet, type):

    host = "0"

    #Host bit should be 0 for network ip
    #Host bit should be 1 for broadcast ip
    if type == "broadcast":
        host = "1"

    index = 0
    return_ip_list = []

    for byte in bin_list:
        index += 1

        if (index > int(subnet)):
            return_ip_list.append(host)
            continue

        return_ip_list.append(byte)

    return return_ip_list

#Returns the class of the ip that is passed
def ip_class (ip):
    octet = ip.split(".")[0]
    bin_list = [*x_bin(octet,8)]
    char = 65 #65 is ASCII for A
    for byte in bin_list:
        if (byte == "0" or char >= 69): #69 is ASCII for E
            return chr(char)
        char += 1


#Converts number to binary and adds X leading 0s
def x_bin (i,x):
    return bin(int(i)).replace("0b","").zfill(x)