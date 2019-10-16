### BACKEND ###

import sys

def HexToText(hexx):
        hexDecoded = bytearray.fromhex(hexx).decode()
        return hexDecoded

def TextToHex(text):
        textEncoded = text.encode('utf-8')
        textConverted = textEncoded.hex()
        return textConverted

### MAINLINE ###

bool_loop = True

print("""
WELCOME TO THE HEX - TEXT CONVERTER
""")
str_correctChoices = ["0","1","2"]
while bool_loop == True:
        str_choice = input("""
Convert Text to Hex --- 0
Convert Hex to Text --- 1
Exit the Program --- 2\n\n""")
        if str_choice.isdigit():
            if str_choice in str_correctChoices:
                bool_loop = False    
            else:
                print("User input invalid, please try again.")      
        else:
            print("User input invalid, please try again.")
        while bool_loop == False:
                if str_choice == "0":
                        str_textHex = input("Please enter the text you wish to convert to hex:\n")
                        try:
                                str_conversion = TextToHex(str_textHex)
                                print(str_conversion)
                                bool_loop = True
                        except:
                                print("Error, please enter valid text.")
                elif str_choice == "1":
                        str_hexText = input("Please enter the hex you wish to convert to text:\n")
                        try:
                                str_conversion = HexToText(str_hexText)
                                print(str_conversion)
                                bool_loop = True
                        except:
                                print("Error, please enter valid hex.")
                elif str_choice == "2":
                        sys.exit()
                        

                                
                        
                
