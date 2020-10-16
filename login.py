attempts_of_password = 0
def check_for_account():
    account_status = True
    try:
        open('passwordsstored.txt', 'r')
    except:
        print("make an account: ")
        account_status = False
    if account_status:
        print("Login to pre-existing account:")
        login_to_account()
    else:
        print("Please create an account as one does not exist: ")
        create_account()


def create_account():
    global name, email, password, password2
    name = input("what is your name: ")
    email = input("what is your email adress: ")
    password = input("please choose a password: ")
    password2 = input("please confirm password: ")
    check_passwords_match()


def check_passwords_match():
    if password == password2:
        save_passwords()
    else:
        print("passwords do not match, try again: ")
        input_passwords()

def save_passwords():
    main_password = str(str(password) + "\n" +str(password2))
    file = open('passwordsstored.txt', 'w')
    file.write(main_password)#
    main_name = str("\n" + name.upper())
    file.write(main_name)
    main_email = str("\n" + email)
    file.write(main_email)
    file.close()

def input_passwords():
    global password, password2
    password = input("please choose a password: ")
    password2 = input("please confirm password: ")
    check_passwords_match()


def login_to_account():
    global password, name1, email1, final_password, final_name
    file = open('passwordsstored.txt', 'r')
    all_lines = file.readlines()
    password = all_lines[0]
    password2 = all_lines[1]
    final_password = password[0:-1]
    name1 = all_lines[2]
    final_name = name1[0:-1]
    email1 = all_lines[3]
    if password[0:-1] == password2[0:-1]:
        ask_for_login()
    else:
        print("the passwords in the file do not match")
        print("please talk to an admin to change the passwords")

def ask_for_login():
    global name0, email0, password0
    name0 = input("What is your name: ")
    email0 = input("What is your email address: ")
    password0 = input("What is your password: ")
    checking_details()
    
def checking_details():
    global password_attempt
    password_attempt = 0
    if name0.upper() == final_name.upper():
        pass
    else:
        print("This name is not registered with an account")
        try_again(1)
    if email0 == email1:
        pass
    else:
        print("This email is not registered with an account")
        try_again(2)
    if final_password == password0:
        check_all_credentials()
    else:
        try_again(3)
        print("wrong password")

def try_again(what_is_wrong):
    global name0, email0, attempts_of_password
    if what_is_wrong == 1:
        #name is wrong
        name0 = input("What is your name: ")
        checking_details()
    elif what_is_wrong == 2:
        #email is wrong
        email0 = input("What is your email address: ")
        checking_details()
    elif what_is_wrong == 3:
        print("wrong password you have " + str(2-attempts_of_password) + " attempts left" )
        attempts_of_password += 1
        password_attempt_checker(attempts_of_password)

def password_attempt_checker(number_of_tries):
    global password0 
    if number_of_tries > 2:
        print("you have run out of attempts")
        exit()
    else:
        password0 = input("What is your password: ")
        checking_details()

def check_all_credentials():
        print("Welcome to your account")
        exit()

check_for_account()
