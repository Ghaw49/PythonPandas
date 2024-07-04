def count(lst):
    even = 0
    odd = 0
    even_list=[]
    odd_list=[]
    for i in lst:
        if i%2 == 0:
            even = even + 1
            even_list.append(i)
        else:
            odd = odd + 1
            odd_list.append(i)

    return even, odd, even_list, odd_list
lst = [1,2,3,4,5,6,7]
even, odd, even_list, odd_list = count(lst)

print(even)
print(odd)
print(even_list)
print(odd_list)
print('even : {} and odd : {}'.format(even,odd))
print('{}, {}'.format('siva', 2))


list = [8,9,0,7]
def value(list):
    even1 = 0
    odd1 = 0
    even1_list = []
    odd1_list = []
    for z in list:
        if z % 2 == 0:
            even1 = even1 + 1
            even1_list.append(z)
        else:
            odd1 = odd1 + 1
            odd1_list.append(z)
    return even1, odd1, even1_list, odd1_list

even1, odd1, even1_list, odd1_list = value(list)
print('even : {} and odd : {} and even list {} and odd list {}'.format(even1,odd1,even1_list,odd1_list))