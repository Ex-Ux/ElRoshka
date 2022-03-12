bol1, bol2, bol3 = False, False, False
while bol1 == False:

    try:
        print('Reqem sechin: ')
        x = float(input())
        bol1 = True

    except ValueError:
        print('Secdiyiniz reqem deyil!')

while bol2 == False:
    try:
        p = input("Emeliyyat sechin: \n" + str(x) +' ')

        if p == '+' or p =='-' or p =='*' or p =='/':
            bol2 = True
            
        else:
            print('Emeliyyat duz sechilmeyib!')
            bol2 = False
    except:
        print('Error')

while bol3 == False:
    try:
        y = float(input('Ikinci reqem sechin: \n' + str(x) + ' ' + str(p) + ' '))
        bol3 = True
    except ValueError:
        print('Secdiyiniz reqem deyil!')



if bol3 == True:
    if p == '+' or p =='-' or p =='*' or p =='/':
        if p == '+':
            print('Netice:')
            print(str(x) + ' + ' + str(y) + ' =',x + y)
        elif p == '-':
            print('Netice:')
            print(str(x) + ' - ' + str(y) + ' =',x - y)
        elif p == '*':
            print('Netice:')
            print(str(x) + ' * ' + str(y) + ' =',x * y)
        elif p == '/':
            if x == 0 or y == 0:
                print('0 -ra bolunmur!')
            else:
                print('Netice:')
                print(str(x) + ' / ' + str(y) + ' =',x / y)