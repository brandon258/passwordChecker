# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def inputs():
    firstname = input(f'Hello, what is your first name?')
    username = input(f'Okay {firstname}, What is your username?')
    password = input(f'Perfect.  Now what is your password {firstname} ?')
    passwordlength = int(len(password))
    passwordmask = passwordlength * '*'
    print(f'{firstname}, your password {passwordmask} is {passwordlength} characters long.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    inputs()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
