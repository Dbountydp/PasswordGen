import random as ran


LowChar = "abcdefghijklmnopqrstwxyz"
UppChar = LowChar.upper() 
num = "1234567890"
symbol = "!@#$%^&*()?|}{]["


def password_gen(size):
    password = ''
    if size <= 4:
        print("size must be 8 ")

    elif size == None:

            for i in range(8):
                tempPass = ran.choice(LowChar+UppChar+num+symbol
            )
                password = password + tempPass
            return password

    else:
            for i in range(size):
                tempPass = ran.choice(LowChar+UppChar+num+symbol
            )
                password = password + tempPass
            return password


ask_length = input(
    "Do you want to genrate password in specific length [yes/no]: ")


if ask_length == "yes" and "Yes" and "y":
    length = int(input(" how much length you want: "))
    # call function for gen password
    password = password_gen(length)
    print(f"you {length} digit password is: {password}"



elif ask_length == 'no' and 'No' and 'n':
    # call function for gen password

    password=password_gen(size=None)
    print(f"you 8 digit password is: {password}")

else:
    print("<---must be typing error --->")
