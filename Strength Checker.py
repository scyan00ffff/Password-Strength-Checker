from threading import Thread
from multiprocessing import Queue 
from queue import Empty
import random
import string

numbers = ["1","2","3","4","5","6","7","8","9"]
special_characters = ["!","@","$","£","%","^","&","*","(",")","_","-","+","_","[","]","{","}","<",">","/","?",";",":"]
characters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

def strength_checker():
    user_input = input("Enter Password: ")

    score = 0

    for x in range(0, len(special_characters)):
        if special_characters[x] in user_input:
            score += 1


    for y in range(0, len(numbers)):
        if numbers[y] in user_input:
            score += 1


    for g in range (0, len(user_input)):
        if user_input[g].isupper():
            score +=1


    if score == 0:
        print("Very Weak Password")
    elif score >= 1 and score < 3:
        print("Weak Password")
    elif score >= 3 and score < 5:
        print("Good Password")
    elif score >= 5 and score < 7:
        print("Strong Password")
    elif score >= 7:
        print("Very Strong Password")



    passwords_file = open("rockyou.txt", "r", encoding="utf-8",errors="replace")
    lines = passwords_file.readlines()
    counter = 0
    for line in lines:
        if user_input in line:
            counter +=1
    print("Password found in", counter, "different combinations in data breaches!")
    passwords_file.close()




def password_generator():
    character_list = ""
    #eventually these inputs will be turned into check boxes on the GUI
    use_special_character = input("Do you want to use special characters? (Y/N): ")
    use_uppercase_character = input("Do you want to use uppercase characters? (Y/N): ")
    use_numbers_character = input("Do you want to use numbers? (Y/N): ")
    length_of_password = int(input("Enter the desired length of your password: "))

    password = []

    if use_special_character == "N" and use_numbers_character == "N" and use_uppercase_character == "N":
        character_list += string.ascii_letters
    elif use_special_character == "Y" and use_numbers_character == "N" and use_uppercase_character == "N":
        character_list += string.ascii_letters + string.punctuation
    elif use_special_character == "Y" and use_numbers_character == "Y" and use_uppercase_character == "N":
        character_list += string.ascii_letters + string.punctuation + string.digits
    elif use_special_character == "Y" and use_numbers_character == "Y" and use_uppercase_character == "Y":
        character_list += string.ascii_letters + string.punctuation + string.ascii_uppercase + string.digits
        

    for desired_length in range(length_of_password):
        randomchar = random.choice(character_list)
        password.append(randomchar)
    print("Your password is: " + "".join(password))

        

while True:
    print("Select which tool you wish to use: ")
    selection = input("Password Generator (1) Password Checker (2): ")

    if selection == "2":
        strength_checker()

        
    elif selection == "1":
        password_generator()











# To do
# - Add Gui



