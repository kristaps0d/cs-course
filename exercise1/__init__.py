def uzdevums1():
	max, min = 0, 0
	while True:
		foo = int(input('\nIevadiet vērtību: '))

		if foo > max:
			max = foo

		if foo < min and foo != 0:
			min = foo

		if min == 0:
			min = foo

		if foo == 0:
			break

	print(f'\nLielākā dotā vērtība: {max}')
	print(f'Mazākā dotā vērtība: {min}')

def uzdevums2():
	from random import randrange
	all_sum = 0
	
	for i in range(0, 10):
		throw, max, sum = randrange, 0, 0
		
		first, second = throw(1, 7), throw(1, 7)

		max = first if first > second else second
		sum += first + second
		all_sum += sum

		print(f'{first}, {second} | {max} | {sum}')

	print(f'\nKopējā uzmestā vērtība: {all_sum}')

def uzdevums3():
	kredits, preces = 0, {'Piens': 20, 'Cepumi': 45, 'Konfekte': 90, 'Sula': 150}

	print('Preču piedavajums:')
	for prece in preces:
		print(f'{prece} {preces.get(prece)} centi')

	print('\nIevadiet preci, kuru vēlaties pirk: ')

	izvele = str(input())

    # Nepabeigts

if __name__ == '__main__':
	uzdevums1()
	uzdevums2()
	uzdevums3()