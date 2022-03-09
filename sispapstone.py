import random

class Scissors_Paper_Stone():
    pass

command = input("Press 'ENTER' to start\nPress anything to exit\n>>> ")
if command == '':

    def Option():

        while True:
            try:
                select = str(input("Choose one of the following :\n'x' for scissor\n'p' for paper\n's' for stone\n>>> "))
            except ValueError:
                print('Invalid! Try again\n')
            else:
                break

        list = ['x', 'p', 's']
        computer = random.choice(list)

        if select == computer:
            print("You >>> ",select,"\nComputer >>> ",computer,"\nIt's draw\n")
        elif select == 'x' and computer == 'p':
            print("You >>> 'SCISSORS'\nComputer >>> 'PAPER'\nYou win\n")
        elif select == 'x' and computer == 's':
            print("You >>> 'SCISSORS'\nComputer >>> 'STONE'\nComputer wins\n")
        elif select == 'p' and computer == 'x':
            print("You >>> 'PAPER'\nComputer >>> 'SCISSORS'\nComputer wins\n")
        elif select == 'p' and computer == 's':
            print("You >>> 'PAPER'\nComputer >>> 'STONE'\nYou win\n")
        elif select == 's' and computer == 'x':
            print("You >>> 'STONE'\nComputer >>> 'SCISSORS'\nYou win\n")
        elif select == 's' and computer == 'p':
            print("You >>> 'STONE'\nComputer >>> 'PAPER'\nComputer wins\n")
        else:
            print('Invalid! Try again\n')
            Option()

        def Info():

            while True:
                try:
                    info = int(input("'1' to play again\n'2' to exit\n>>> "))
                except ValueError:
                    print('Invalid! Try again\n')
                else:
                    break

            if info == 1:
                Option()
            elif info == 2:
                print('Program exited\n')
                exit()
            else:
                Info()

        Info()
    Option()
else:
    print('Program exited\n')
    exit()