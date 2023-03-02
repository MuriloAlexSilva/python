number  =   int(input('Digite um número para ver sua tabuada: '))


print('-------------------------')

for n in range(1,11):
    print('{} x {:2} = {}'.format(number,n,(number * n)))

print('-------------------------')