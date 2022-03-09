history = []

def Functional():

    info = input("\nPress 'ENTER' to start\nEnter 'h' to view history\nEnter anything to exit\n>>> ")
    if info == '':

        def Main():

            while True:
                try:
                    fnum = float(input('\nEnter first number\n>>> '))
                except ValueError:
                    print('\nInvalid! Try again\n')
                else:
                    break

            while True:
                try:
                    snum = float(input('\nEnter second number\n>>> '))
                except ValueError:
                    print('\nInvalid! Try again\n')
                else:
                    break

            def Work():

                while True:
                    try:
                        oper = int(input('\nSelect one of the operations below:\n1.Add\n2.Sub\n3.Mul\n4.Div\n>>> '))
                    except ValueError:
                        print('\nInvalid! Try again\n')
                    else:
                        break
                
                if oper in range(1,5):

                    if oper == 1:
                        ans = fnum + snum
                        if ans.is_integer():
                            ans = int(ans)
                        else:
                            ans = float(ans)
                        record =f'{fnum} + {snum} = {ans}\n'
                        print(record)
                        print('\nAnswer >>> ',ans)

                    if oper == 2:
                        ans = fnum - snum
                        if ans.is_integer():
                            ans = int(ans)
                        else:
                            ans = float(ans)
                        record =f'{fnum} - {snum}={ans}\n'
                        print(record)
                        print('\nAnswer >>> ',ans)


                    if oper == 3:
                        ans = fnum * snum
                        if ans.is_integer():
                            ans = int(ans)
                        else:
                            ans = float(ans)
                        record =f'{fnum} * {snum} = {ans}\n'
                        print(record)
                        print('\nAnswer >>> ',ans)


                    if oper == 4:
                        ans = fnum / snum
                        if ans.is_integer():
                            ans = int(ans)
                        else:
                            ans = float(ans)
                        record =f'{fnum} / {snum} = {ans}\n'
                        print(record)
                        print('\nAnswer >>> ',ans)

                    history.append(record)

                else:
                    print('\nInvalid! Try again\n')
                    Work()
            Work()

            def Ask():

                ask = input("\nPress 'ENTER' to restart\nEnter 'h' to view history\nEnter anything to exit\n>>> ")
                if ask == '':
                    Main()
                elif ask == 'h':
                    print('\n',*history, sep='\n')
                    Ask()
                else:
                    print('\nProgram exited\n')
                    exit()      
            Ask()
        Main()

    elif info == 'h':
        print('No recorded history yet >>> ',history)
        Functional()
    else:
        print('\nProgram existed\n')
        exit()
Functional()