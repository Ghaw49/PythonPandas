import pandas as pd
is_running = True
shoppingcartdictionary = {}
outputdictionary = {}
while is_running:
    q1 = input('Would you like to see list of available items? y/n ')
    if q1.strip().lower() == 'y':
        #read from inventory.txt file:
        file = open('inventory.txt', 'r')
        inventorydictionary = {}
        for value in file:
            #print(value)
            itemdetails = value.split(' : ')
            #print(itemdetails[0], itemdetails[1])
            inventorydictionary.update({itemdetails[0] : itemdetails[1]})
        print('Inventory ', inventorydictionary)
        q2 = input('Enter required items one at a time ')
        lookup1 = inventorydictionary.get(q2)
        print(lookup1)
        if lookup1 == None:
            print('Item ', q2, 'is not available. ')
            q3 = input('Do you want to continue shopping? y/n ')
            if q3.strip().lower() == 'y':
                q4 = input('Enter required items ')
                lookup2 = inventorydictionary.get(q4)
                if lookup2 == None:
                    print('Item ', q4, 'is not available ')
                    break
                else:
                    q5 = int(input('Enter quantity '))
                    shoppingcartdictionary.update({q4 : q5})
            else:
                print('Thanks for shopping')
                break
        else:
            q6 = int(input('Enter quantity for {} '.format(q2)))
            shoppingcartdictionary.update({q2 : q6})
        print('shopping cart ', shoppingcartdictionary)

        totalprice = 0
        for item,quantity in shoppingcartdictionary.items():
            unitprice = inventorydictionary.get(item)
            outputdictionary.update({item : ', quantity = ' + str(quantity) + ', unit price ' + str(unitprice)})

            totalprice=totalprice + (quantity * float(unitprice))
        outputdf = pd.DataFrame(outputdictionary, index=[0])
        print(outputdf)
        print('totalprice = ', totalprice)




    elif q1 == 'n':
        print('Exit')

