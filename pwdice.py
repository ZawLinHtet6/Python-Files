from random import randint
import random
import string

def Main():

    command = input("Press 'ENTER' to start\nPress anything to cancel\n>>> ")
    if command == '':

        def Work():

            while True:
                try:
                    info = int(input("Enter '1' to generate a new password\nEnter '2' to play dice rolling game\n>>> "))
                except ValueError:
                    print('Invalid! Try again\n')
                else:
                    break

            if info == 1:

                def Generate_new_password():

                    print(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12)))
                    
                    def Generate_again():

                        while True:
                            try:
                                select = int(input("Enter '1' to get new password\nEnter '2' to choose options\nEnter '3' to exit\n>>> "))
                            except ValueError:
                                print('Invalid! Try again\n')
                            else:
                                break

                        if select == 1:
                            Generate_new_password()
                        elif select == 2:
                            Work()
                        elif select == 3:
                            print('Program exited')
                            exit()
                        else:
                            print('Invalid! Try again\n')
                            Generate_again()

                    Generate_again()

                Generate_new_password()

            elif info == 2:

                def Dice_rolling_game():

                    print(random.randint(1,7))

                    def Roll_again():

                        while True:
                            try:
                                index = int(input("Enter '1' to get roll dice again\nEnter '2' to choose options\nEnter '3' to exit\n>>> "))
                            except ValueError:
                                print('Invalid! Try again\n')
                            else:
                                break

                        if index == 1:
                            Dice_rolling_game()
                        elif index == 2:
                            Work()
                        elif index == 3:
                            print('Program exited\n')
                            exit()
                        else:
                            Roll_again()

                    Roll_again()

                Dice_rolling_game()

        Work()
    
    else:
        print('Program exited\n')
        exit()

Main()