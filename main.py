from os import path


class Guest:
    def __init__(self, charter, name):
        self.charter = charter
        self.name = name
        self.menu()

    def menu(self):
        print('\nYou have a "Guest tier".  Login for more privileges!')
        print('Enter "help" to get a list of commands')

        while True:
            command = input(f"┌──({self.name}㉇guest) - [~|help|about|login|exit|~]\n└─$ ")

            if command == 'login':
                self.login()
                break
            elif command == 'about':
                self.about()
            elif command == 'help':
                self.help()
            elif command == 'exit':
                self.charter = 'none'
                break
            else:
                print("Command not found! Please, try again")

    def login(self):
        if path.exists('Q:\\users.txt'):
            with open('Q:\\users.txt', 'r') as file:
                users = [line.split(':') for line in file if line[0:44] != '<username>:<password>:<blocked>:<limitation>']

            for _ in range(3):
                username = input("Login: ")
                password = input("Password: ")
                user_data = []
                for user in users:
                    if username == user[0]:
                        user_data = user
                if not user_data:
                    print("Such user is not registered in the system!")
                else:
                    if password == user_data[1]:
                        if username == 'admin':
                            self.charter = 'admin'
                            self.name = 'admin'
                            break
                        else:
                            self.charter = 'user'
                            self.name = username
                            break
                    elif username == user_data[0] and user_data[2] == 1:
                        print("This account is blocked! Contact the administrator to resolve this issue")
                        continue
                    else:
                        print("Login or password incorrect!")
                        continue
            else:
                self.charter = 'none'
        else:
            with open('Q:\\users.txt', 'w') as file:
                file.write("<username>:<password>:<blocked>:<limitation>\nadmin::false:false\n")
            print('The first login is recorded!\nLogged into the system as "admin" with an empty password')
            self.charter = 'guest'
            self.name = 'guest'

    @staticmethod
    def about():
        print("Developer: Stoliarchuk Vladyslav\nGroup: FB-81\nVariant: 17\nTask: password not matching username")

    @staticmethod
    def help():
        print("""\
                #############################################
                #                                           #
                #   ---------Available Commands----------   #
                #   | Guest tier:                       |   #
                #   |   -login                          |   #
                #   |   -about                          |   #
                #   |   -help                           |   #
                #   |   -exit                           |   #
                #   | User tier:                        |   #
                #   |   -change_pass                    |   #
                #   | Admin tier:                       |   #
                #   |   -get_user_list                  |   #
                #   |   -add_user                       |   #
                #   |   -block_user                     |   #
                #   |   -limited_user_pass              |   #
                #   -------------------------------------   #
                #                                           #
                #############################################
              """)


class User(Guest):

    def menu(self):
        print('You have a "User tier".')
        print('Enter "help" to get a list of commands')

        while True:
            command = input(f"┌──({self.name}㉇user) - [~|help|about|login|exit|change_pass|~]\n└─$ ")

            if command == 'login':
                self.login()
                break
            elif command == 'about':
                self.about()
            elif command == 'help':
                self.help()
            elif command == 'exit':
                self.charter = 'none'
                break
            elif command == 'change_pass':
                self.change_pass()
            else:
                print("Command not found! Please, try again")

    def change_pass(self):
        username = self.name
        with open('Q:\\users.txt', 'r') as file:
            users = [line.split(':') for line in file]
        check = False
        index = None
        for user in range(len(users)):
            if username in users[user]:
                check = True
                index = user
        if check:
            while True:
                old_password = input('Please, write a password to change to a new one or write "quit" to quit!\nPassword: ')
                if old_password == users[index][1]:
                    while True:
                        new_password_first = input("New password: ")
                        new_password_second = input("Confirm new password: ")
                        if new_password_first == new_password_second:
                            users[index][1] = new_password_second
                            new_users = [':'.join(user) for user in users]
                            new_users_str = ''.join(user for user in new_users)
                            with open('Q:\\users.txt', 'w') as file:
                                file.write(new_users_str)
                            print(f"Success change password!")
                            break
                        else:
                            print("Passwords not matching! Try again!")
                            continue
                    break
                elif old_password == 'quit':
                    break
                else:
                    print("Incorrect password! Try again!")
                    continue
        else:
            print("User with this name does not exist!")


class Admin(User):

    def menu(self):
        print('You have a "Admin tier".')
        print('Enter "help" to get a list of commands')

        while True:
            command = input(f"┌──({self.name}㉇admin) - [~|help|about|exit|change_pass|get_user_list|add_user|block_user|limited_user_pass|~]\n└─$ ")

            if command == 'login':
                self.login()
                break
            elif command == 'about':
                self.about()
            elif command == 'help':
                self.help()
            elif command == 'exit':
                self.charter = 'none'
                break
            elif command == 'change_pass':
                self.change_pass()
            elif command == 'get_user_list':
                self.get_user_list()
            elif command == 'add_user':
                self.add_user()
            elif command == 'block_user':
                self.block_user()
            elif command == 'limited_user_pass':
                self.limited_user_pass()
            else:
                print("Command not found! Please, try again")

    @staticmethod
    def get_user_list():
        with open('Q:\\users.txt', 'r') as file:
            users = [line.split(':') for line in file]
        for user_data in users:
            print("{: >20} {: >20} {: >20} {: >20}".format(*user_data))

    @staticmethod
    def add_user():
        username = input("Enter the username of the new user: ")
        user_data = username + '::false:false\n'
        with open('Q:\\users.txt', 'r+') as file:
            users = [line.split(':') for line in file if line[0:44] != '<username>:<password>:<blocked>:<limitation>']
            check = False
            for user in users:
                if username in user:
                    check = True
            if not check:
                file.write(user_data)
                print("Success!")
            else:
                print("User with this name already exists!")

    @staticmethod
    def block_user():
        username = input("Enter the username you want to block: ")
        with open('Q:\\users.txt', 'r') as file:
            users = [line.split(':') for line in file]
        check = False
        index = None
        for user in range(len(users)):
            if username in users[user]:
                check = True
                index = user
        if check:
            users[index][2] = 'true'
            new_users = [':'.join(user) for user in users]
            new_users_str = ''.join(user for user in new_users)
            with open('Q:\\users.txt', 'w') as file:
                file.write(new_users_str)
            print(f"Success blocked user: {username}!")
        else:
            print("User with this name does not exist!")

    @staticmethod
    def limited_user_pass():
        username = input("Enter the username you want to add limited: ")
        with open('Q:\\users.txt', 'r') as file:
            users = [line.split(':') for line in file]
        check = False
        index = None
        for user in range(len(users)):
            if username in users[user]:
                check = True
                index = user
        if check:
            users[index][3] = 'true'
            new_users = [':'.join(user) for user in users]
            new_users_str = ''.join(user for user in new_users)
            with open('Q:\\users.txt', 'w') as file:
                file.write(new_users_str)
            print(f"Success add limited to user: {username}!")
        else:
            print("User with this name does not exist!")


def main():
    charter = 'guest'
    name = 'guest'
    while True:
        if charter == 'guest':
            person = Guest(charter, name)
            charter = person.charter
            name = person.name
        elif charter == 'user':
            person = User(charter, name)
            charter = person.charter
            name = person.name
        elif charter == 'admin':
            person = Admin(charter, name)
            charter = person.charter
            name = person.name
        elif charter == 'none':
            break
        else:
            print("Admittance error!")


if __name__ == '__main__':
    main()
