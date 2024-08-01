from threading import Thread
from multiprocessing import Queue 
from queue import Empty
import time 

numbers = ["1","2","3","4","5","6","7","8","9"]
special_characters = ["!","@","$","£","%","^","&","*","(",")","_","-","+","_","[","]","{","}","<",">","/","?",";",":"]
characters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

while True:
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
        print(" Very Weak Password")
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









# To do
# - Add common passwords database/breached passwords
# - Add password generator
# - Add Gui



