# importing the random module so as to be able to genertae random paswords for user

import random

# A function is being created to validate the password when creating it

def pasword():
    satisfy = 'no'
    while satisfy == 'no':
        new_pass =input("please enter new password: ")
        if len(new_pass) < 7:
            print ("password must be a minimum of 7 chracters")
        else:
            print(f"your new password is {new_pass}")
            break




# Another function is created to collect data and process them


def start ():
    my_list =[]
    first_name = input("enter your first name:").upper() # this input will always be in lowwer case
    last_name = input ("enter your last name:").upper()
    email = input("enter your email address:")
    details = [first_name,last_name,email]
    first_2 = first_name[0:2] # extracting characters from the user data
    last_2 = last_name[-2:]
    pick_up = "ertyuiopasdfghjklzxcvbnm1234567890@#$&,><?/qw"
    password_length = 5
    password = (random.sample(pick_up , password_length)) # the random password generator which will return as a list
    password2 = "".join(password) # converting the list result into a string
    final_pass = f"{first_2}{password2}{last_2}"


    print(f"your password is {final_pass} , i hope you like it? input yes or no  ")
    satisfaction = input()
    if satisfaction == "yes":
        details.append(final_pass)
        my_list.append(details)
        print(f"welcome on board {first_name} {last_name}")
        new_u =input("is there a another user? ")
        if new_u == 'yes':
            start()

    else:
        for list in my_list:
            print (list)


        pasword()  # the password validation function will only work when user is not satisfy with password generated

        new_pass=input('retype new password: ')
        my_list =[first_name,last_name,new_pass]
        print(f"welcome on board {first_name} {last_name} ")
        print ("have a safe journey with us")
        print(my_list)
        new_u = input("is there another user? input yes or no ")
        if new_u == 'no' :
            print("check back later")
                #break
        else:
                while new_u =='yes':
                    start()   # iterating the code using the start function so as to register more users without having



                    break




start()

print("thanks for your time")

