a = int(input(' enter a value : '))
b = int(input('enter b value : '))
if (a%2==0 and b%2==0):
    print('both  are even')
elif a%2==0 :
    print('a is even and b is odd' )
elif b%2 ==0:
    print('b is even and a is odd')
else:
    print('both are odd')
