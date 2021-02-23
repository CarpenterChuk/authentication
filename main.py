from os import path


class Guest:
    def __init__(self, charter):
        self.charter = charter
        self.menu()

    def menu(self):
        print('\nYou have a "Guest tier".  Login for more privileges!')
        print('Enter "help" to get a list of commands')

        while True:
            command = input("guest:\\")

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
                users = [line.split(':') for line in file if line[0] != '|']

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
                            break
                        else:
                            self.charter = 'user'
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
                file.write("|username:password:blocked:limitation|\nadmin::0:0\n")
            print('The first login is recorded!\nLogged into the system as "admin" with an empty password')
            self.charter = 'guest'

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
                #   |   -user_list                      |   #
                #   |   -user_add                       |   #
                #   |   -user_block                     |   #
                #   |   -user_constr                    |   #
                #   -------------------------------------   #
                #                                           #
                #############################################
              """)


class User(Guest):

    def menu(self):
        print('You have a "User tier".')
        print('Enter "help" to get a list of commands')

        while True:
            command = input("user:\\")

            if command == 'login':
                self.login()
            elif command == 'about':
                self.about()
            elif command == 'help':
                self.help()
            elif command == 'exit':
                self.charter = 'none'
                break
            else:
                print("Command not found! Please, try again")


class Admin(User):

    def menu(self):
        print('You have a "Admin tier".')
        print('Enter "help" to get a list of commands')

        while True:
            command = input("admin:\\")

            if command == 'login':
                self.login()
            elif command == 'about':
                self.about()
            elif command == 'help':
                self.help()
            elif command == 'exit':
                self.charter = 'none'
                break
            else:
                print("Command not found! Please, try again")


def main():
    person = None
    charter = 'guest'

    while True:
        if charter == 'guest':
            person = Guest(charter)
            charter = person.charter
        elif charter == 'user':
            person = User(charter)
            charter = person.charter
        elif charter == 'admin':
            person = Admin(charter)
            charter = person.charter
        elif charter == 'none':
            break
        else:
            print("perm error")


if __name__ == '__main__':
    main()
