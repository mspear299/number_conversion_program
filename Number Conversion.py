#Lab 1 - Conversion between different number systems
#Marcus Spear

#function converts any number that corresponds to a hex letter to that letter otherwise returns the decimal number as is
def decimalToHexDigit(decimal_value):
    dictionary={10: "A", 11: "B", 12 : "C", 13: "D", 14 : "E", 15 : "F"}
    for key in dictionary:
        if decimal_value == key:
            return dictionary[key]          
    return decimal_value 

#function converts decimal input to a hex number
def decToHex(decimal_number):
    hex_result= ""

    while int(decimal_number) > 0:
        remainder=int(decimal_number)%16
        hex_digit=decimalToHexDigit(remainder)
        hex_result=f"{hex_digit}{hex_result}"
        decimal_number=int(decimal_number)/16
    
    return hex_result

#function converts any hexadecimal letter to its corresponding decimal number otherwise returns the digit as is
def hexDigitToDecimal(hex_digit):
    dictionary={"A": 10, "B": 11, "C" : 12, "D": 13, "E" : 14, "F" : 15}
    for key in dictionary:
        if str(hex_digit).capitalize() == key:
            return dictionary[key]      
    return hex_digit

#function converts hex input to a decimal number
def hexToDec(hex_number):
    deciVal=0
    pos=0
    #in case the hexDigitToDecimal function fails to convert letter to a decimal number then return "Invalid input"
    try:
        for digit in reversed(hex_number):     
            deciVal=deciVal+(int(hexDigitToDecimal(digit))*16**pos)
            pos=pos+1
    except ValueError:
        return "Invalid input"
    
    return deciVal

#function converts binary input to decimal number
def binaryToDec(binary_number):
    deciVal=0
    pos=0

    for digit in reversed(binary_number):
        deciVal=deciVal+(int(digit)*2**pos)
        if int(digit)>1:
            return "Invalid input"
        pos=pos+1

    return deciVal

#function converts decimal input to binary
def decToBinary(decimal_number):
    binary_result=""

    while int(decimal_number)>0:
        remainder=int(decimal_number)%2
        binary_result=f"{int(remainder)}{binary_result}"
        decimal_number=int(decimal_number)/2
    
    return binary_result

#function converts hex input to binary
def hexToBinary(hex_number):
    convert_to_decimal=hexToDec(hex_number)
    if convert_to_decimal =="Invalid input":
        return "Invalid input"
    return decToBinary(convert_to_decimal)

#function converts binary input to hex value
def binaryToHex(binary_number):
    convert_to_decimal=binaryToDec(binary_number)
    if convert_to_decimal =="Invalid input":
        return "Invalid input" 
    return decToHex(convert_to_decimal)

    
#Main
#While loop for the program to loop continuously until the user decides to exit
while True:
    print("Type in number (1-6) to execute the corresponding algorithm:" 
    "\n1. binary to decimal"
    "\n2. decimal to binary"
    "\n3. hex to decimal"
    "\n4. decimal to hex"
    "\n5. hex to binary"
    "\n6. binary to hex")

#match statement for user selection 
    while True:
        match input("\nEnter selection: "):
            case "1":
                print("You chose binaryToDec")
                user_input=input("Type in binary number to convert: ")
                print("Result:", binaryToDec(user_input))
                break
            case "2":
                print("You chose decToBinary")
                user_input=input("Type in decimal number to convert: ")
                print("Result:", decToBinary(user_input))
                break
            case "3":
                print("You chose hexToDec")
                user_input=input("Type in hex number to convert: ")
                print("Result:", hexToDec(user_input))
                break
            case "4":
                print("You chose decToHex")
                user_input=input("Type in decimal number to convert: ")
                print("Result:", decToHex(user_input))
                break
            case "5":
                print("You chose hexToBinary")
                user_input=input("Type in hex number to convert: ")
                print("Result:", hexToBinary(user_input))
                break
            case "6":
                print("You chose binaryToHex")
                user_input=input("Type in binary number to convert: ")
                print("Result:", binaryToHex(user_input))
                break
            case _ :
                print("Invalid input")
                continue

   #ask user to enter Y/y to continue or N/n to terminate program, prompt again if user fails to enter either choice        
    while True:
        exit_prompt_input=input("Type in Y/y to continue, or N/n to terminate program: ").capitalize()         
        if exit_prompt_input == "Y" or exit_prompt_input == "N":
            break
        else:
            continue
           
    if exit_prompt_input == "N":
        break

    print("\n")

                             
