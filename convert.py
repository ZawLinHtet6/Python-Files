class Convert():
    pass

def Unit():

    while True:
        try:
            unit = int(input("'1' convert inch -> feet\n'2' to convert feet -> inch\n'3' to convert meter to kilometer\n'4' convert kilometer to meter\n>>> "))
        except ValueError:
            print('Invalid! Try again')
        else:
            break

    if unit == 1:
        while True:
            try:
                inch = float(input('Enter in inch\n>>> '))
            except ValueError:
                print('Invalid! Try again')
            else:
                break

        print(inch/12, ' ft')

    elif unit == 2:
        while True:
            try:
                feet = float(input('Enter in feet\n>>> '))
            except ValueError:
                print('Invalid! Try again')
            else:
                break

        print(feet*12, ' in')

    elif unit == 3:
        while True:
            try:
                meter = float(input('Enter in meter\n>>> '))
            except ValueError:
                print('Invalid! Try again')
            else:
                break

        print(meter/1000, ' km')

    elif unit == 4:
        while True:
            try:
                km = float(input('Enter in kilometer\n>>> '))
            except ValueError:
                print('Invalid! Try again')
            else:
                break

        print(km*1000, ' m')

    else:
        print('Invalid! Try again')
        Unit()

    def MSG():

        while True:
            try:
                msg = int(input("'1' to convert again\n'2' to exit\n>>> "))
            except ValueError:
                print('Invalid! Try again')
            else:
                break

        if msg == 1:
            Unit()
        elif msg == 2:
            print('Program exited')
            exit()
        else:
            MSG()

    MSG()

Unit()