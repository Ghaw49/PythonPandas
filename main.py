from bankprogram import *
is_running= True


def bank_functions():
    global is_running
    while is_running:
        print('Banking Account')
        print('1.Deposit ')
        print('2.Withdraw ')
        print('3.Balance ')
        print('4.Exit')

        choice = int(input('enter choice 1-4 '))
        if choice == 1:
            try:
                deposit()
            except Exception:
                print('you have exceeded max num of limits')
                break
            option = input('do you want to continue? y/n ')
            if option == 'n':
                is_running = False
        elif choice == 2:
            withdraw()
        elif choice == 3:
            show_balance()
            option = input('do you want to continue? y/n ')
            if option == 'n':
                is_running = False
        elif choice == 4:
            is_running = False
        else:
            print('Wrong selection. Try again. ')


bank_functions()
