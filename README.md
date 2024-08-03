# Password-Strength-Checker-and-Generator

A simple python password strength checker and password generator. 

The algorithm works by checking if the users entered password contains any special characters, uppercase characters or numbers. The more of these that it contains the higher the password's score is and therefore the greater the strength of the password is.

Along with this simple feature the algorithm also checks to see if the password has been leaked in any combination by checking if it appears in the 'rockyou.txt' data breach. If so it will display how many times the password has been found whithin this breach. 

The generator takes a selection of parameters from the user and then uses a list of available characters to create a random password.

Due to githubs file size limitations the rockyou text file cannot be uploaded to the repository for this project but can be easily sourced from this website: https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt

Once sourced ensure the file is whithin the same working directory as the python program and you should be good to go. 

Screenshots:

Home Page:
![passwordhome](https://github.com/user-attachments/assets/89a5de11-713e-4284-bafc-88949e6e5e80)

Password Generator:
![Screenshot 2024-08-03 012645](https://github.com/user-attachments/assets/eb94038f-6cbe-4188-9aef-3235f162ad43)

Password Strength Tester:
![passwordtester](https://github.com/user-attachments/assets/7d2fef31-9a27-47f5-9643-7cac1f500a54)
