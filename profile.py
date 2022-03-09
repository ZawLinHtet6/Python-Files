def Main():

    while True:
        try:
            ask = int(input("\n'1' Sign up\n'2' Sign in\n'3' Exit\n>>> "))
        except ValueError:
            print('\nInvalid! Try again')
        else:
            break

    if ask == 1:

        name = input('\nName\n>>> ')
        birth = input('\nDate of birth\n>>> ')
        phone = input('\nPhone number\n>>> ')
        address = input('\nAddress\n>>> ')
        email = input('\nEmail\n>>> ')
        college = input('\nCollege\n>>> ')
        work = input('\nOccupation\n>>> ')
        username = input('\nUsername\n>>> ')
        password = input('\nPassword\n>>> ')

        print('Account successfully created')

        info = f'Name - {name}\nDate of birthday - {birth}\nPhone - {phone}\nAddress - {address}\nEmail - {email}\nCollege - {college}\nOccupation - {work}\nUsername - {username}'
        secret = f'{username}\n{password}'

        file = open("profile.txt", "w")
        file.write(info)
        file.close()

        txt = open("account.txt", "w")
        txt.write(secret)
        txt.close()

        def Func():

            while True:
                try:
                    show = int(input("\n'1' Sign in\n'2' Exit\n>>> "))
                except ValueError:
                    print('\nInvalid! Try again')
                else:
                    break

            if show == 1:

                def Account():

                    username = input('\nUsername\n>>> ')
                    password = input('\nPassword\n>>> ')

                    safe = f'{username}\n{password}'

                    txt = open("account.txt", "r")
                    save = txt.read()
                    txt.close()

                    if safe == save:
                        print('\nAccount signed in suuuessfully\n')
                    else:
                        print('\nIncorrect username or password')
                        Account()

                    def Work():

                        while True:
                            try:
                                command = int(input("'1' View profile\n'2' Sign out\n'3' Exit\n>>> "))
                            except ValueError:
                                print('\nInvalid! Try again')
                            else:
                                break

                        if command == 1:
                            file = open("profile.txt", "r")
                            print('\n',file.read())
                            file.close()
                        elif command == 2:
                            Main()
                        else:
                            print('\nInvalid! Try again')
                            Work()
                    Work()
                    
                Account()
        Func()

    elif ask == 2:

        def Account():

            username = input('\nUsername\n>>> ')
            password = input('\nPassword\n>>> ')

            safe = f'{username}\n{password}'

            txt = open("account.txt", "r")
            save = txt.read()
            txt.close()

            if safe == save:
                print('\nAccount signed in suuuessfully\n')
            else:
                print('\nIncorrect username or password')
                Account()

            def Work():

                while True:
                    try:
                        prompt = int(input("'1' View profile\n'2' Sign out\n'3' Exit\n>>> "))
                    except ValueError:
                        print('\nInvalid! Try again')
                    else:
                        break

                if prompt == 1:
                    file = open("profile.txt", "r")
                    print('\n',file.read())
                    file.close()

                    def Do():

                        while True:
                            try:
                                signal = int(input("\n'1' Sign out\n'2' Exit\n>>> "))
                            except ValueError:
                                print('\nInvalid! Try again')
                            else:
                                break

                        if signal == 1:
                            Main()
                        elif signal == 2:
                            print('\nProgram exited\n')
                            exit()
                        else:
                            print('\nInvalid! Try again')
                            Do()
                    Do()

                elif prompt == 2:
                    Main()
                else:
                    Work()
                    
            Work()

        Account()

    elif ask == 3:
        print('\nProgram exited\n')
        exit()
    else:
        Main()
Main()