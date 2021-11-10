def VendingMachine(num_items,item_price):
    l=[num_items,item_price]
    return l
def buy(req_items,money):
    L=VendingMachine(a,b)
    if L[0]>=req_items and money>=req_items*L[1]:
        L[0]=L[0]-req_items
        print(money-(req_items*L[1]))
    if L[0]<=req_items and money>=req_items*L[1]:
        print('Not enough items in the machine')
    if L[0]>=req_items and money<=req_items*L[1]:
        print('Not enough coins')
a, b = [int(a) for a in input().split()]
c,d = [int(c) for c in input().split()]
buy(c,d)






