import random # import the random module to generate random password
import string # importing the string module to carry out some operation like slicing




# function id created to collect user data
def user_details ():
    first_name = input("enter your first name:").upper() # this input will always be in lowwer case
    last_name = input ("enter your last name:").upper()
    email = input("enter your email address:")
    details = [first_name,last_name,email]
    return details



# funtion is created to generate random password
def pass_create(details):
    characters = string.ascii_letters
    lenght = 5
    random_pass = ''.join(random.choice(characters)for i in range(lenght))

    password_gen = str(details[0][0:2] + details[1][-2:] + random_pass)

    return password_gen


status =True
storage =[]

while status:

    details = user_details()

    password=pass_create(details)
    print ("your password is: " + str(password))

    password_satisfy = input(str("do you like the password? enter yes or no "))

    password_loop = True

    while password_loop:
        if password_satisfy == "yes":
            details.append(password)

            storage.append(details)  # adding user details to the variable storage   g


            password_loop = False;

        else:

            new_pass = input(str("enter a new pasword not less than 7 characters: "))

            pass_len =True

            while pass_len:
                if len(new_pass) >= 7:

                    details.append(new_pass)

                    storage.append(details)

                    pass_len = False

                    password_loop = False
                else:

                    print("your password is less than 7, not valid ")

                    new_pass = input(str("password must not be less than 7 "))

        new_user=input(str("is there another user? yes or no "))

        if (new_user == "no"):
            status = False
            for list in storage:  # this print out the value stored in the storage variable
                print(list)

        else:

            status = True