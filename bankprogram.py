balance = 0
def show_balance():
    print(balance)

def deposit():
    amount = input('enter cash/check ')
    if amount == 'cash':
      try:
          cash = int(input('enter amount in $ '))
          global balance
          balance = cash + balance
          print('$', cash, ' cash deposit has been accepted ')
          print('balance ', balance )
      except ValueError:
          print('invalid entry')
          cash = int(input('enter amount in $ '))
          print('$', cash, ' cash deposit has been accepted ')


    elif amount == 'check':
        check = int(input('present check for $ '))
        print('$', check, 'check deposit has been accepted ')
    else:
        print('invalid entry ')
        deposit()


def withdraw():
    global balance
    amount = int(input('enter amount to withdraw '))
    balance = balance - amount
    print('collect your amount $ ', amount)

balance = 0

