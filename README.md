# Password-Strength-Checker

A simple python password strength checker. 

The algorithm works by checking if the users entered password contains any special characters, uppercase characters or numbers. The more of these that it contains the higher the password's score is and therefore the greater the strength of the password is.

Along with this simple feature the algorithm also checks to see if the password has been leaked in any combination by checking if it appears in the 'rockyou.txt' data breach. If so it will display how many times the password has been found whithin this breach. 

Due to githubs file size limitations the rockyou text file cannot be uploaded to the repository for this project but can be easily sourced from this website: https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt

Once sourced ensure the file is whithin the same working directory as the python program and you should be good to go. 
