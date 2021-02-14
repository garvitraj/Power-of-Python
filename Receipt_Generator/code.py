# importing the pakages
import string
import random

if __name__ == "__main__":
    string1 = string.ascii_lowercase

    string2 = string.ascii_uppercase

    string3 = string.digits

    string4 = string.punctuation

    passwordLength = int(input("Enter password length\n"))
    finalPassword = []  # creating the blank list to store data
    # apending and extending the list
    finalPassword.extend(list(s1))
    finalPassword.extend(list(s2))
    finalPassword.extend(list(s3))
    finalPassword.extend(list(s4))

    print("Your password is: ")
    # print("".join(s[0:passwordLength]))
    print("".join(random.sample(finalPassword, passwordLength)))
