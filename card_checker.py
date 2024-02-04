'''
Andrew Deal
Credit Card Checker
02/03/2024

This program uses the Luhn Algorithm to check if
a credit card number is valid.
'''

## -- Imports -- ##
import sys


## -- Create functions -- ##

#Get card input from user
def get_input(repeated=False):
    if not repeated:
        num = input("Please enter a credit card number: ") #Data type string
    else:
        #User has entered an invalid card number immediately
        num = input("Please enter a credit card number or type 'stop' to terminate: ")
        if num == "stop":
            sys.exit(0)
    num = num.replace(" ", "") #Remove spaces
    print() #Create a new line
    return num #Return the formatted card number string

#Return the brand of a credit card based on a string input
def get_brand(c_num):
    first = int(c_num[0]) #Get the first number of the card as an int
    #Dictionary stores possible brand for each number
    brands = {
        #Uses most common brand/industry for each number
        0: ["ISO TC 68", "an"],
        1: ["Airline", "an"],
        2: ["Mastercard", "a"],
        3: ["American Express", "an"],
        4: ["Visa", "a"],
        5: ["Mastercard", "a"],
        6: ["Discover", "a"],
        7: ["gas", "a"],
        8: ["healthcare", "a"],
        9: ["government", "a"]
        #Source 1: USAToday.com
        #Source 2: Wikipedia.org : Payment Card Number
        #The brands also store an article (a/an) for
         #grammatically correct print formatting
    }
    return brands[first]

#Use Luhn Algorithm to check card validity
def check_card(c_num):
    #Convert card number to list of ints
    digits = []
    for number in c_num:
        digits.append(int(number))

    #Double every other number from right to left
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        #Subtract 9 if result is greater than 9
        if digits[i] > 9:
            digits[i] -= 9

    #Get sum of digits
    total = sum(digits)

    #If total is divisible by 10, the card is valid
    return total % 10 == 0


## -- Runtime Logic -- ##

#Get user input for credit card number
card_number = get_input()

#Make sure card is only number characters and has 16 digits
while not card_number.isdigit() or len(card_number) != 16:
    print("Invalid card number. Card numbers contain 16 digits.")
    card_number = get_input(repeated=True)

#Print whether the card is valid
is_valid = check_card(card_number)
if is_valid:
    print("That is a valid credit card number.")
    #Print the brand of the card
    brand, article = get_brand(card_number) #Multiple variable assignment from list
    print("It is %s %s card." % (article, brand)) #Uses string formatting
else:
    print("That is not a valid credit card number.")

#Keep screen open
input()


