from colorama import Fore, Style

UP_ONE_LINE = "\033[F\033[K"

to_solve = ''

with open('input.txt') as f:
	to_solve = f.read()

to_solve = list(filter(None, to_solve.split('\n')))
to_solve = list(map(lambda x: x.split(': '), to_solve))

temp = []
for i in to_solve:
	ttemp = i[0].split(' ')
	tttemp = ttemp[0].split('-')
	ttttemp = {'char': ttemp[1], 'passwd': i[1], 'min': int(tttemp[0]), 'max': int(tttemp[1])}
	temp.append(ttttemp)
to_solve = temp

print('-' * 10, 'Part 1', '-' * 10)

part1 = 0
for i in to_solve:
	char = i['char']
	string = i['passwd']
	print(f'{i["min"]}-{i["max"]} {char}: ', end='')
	counter = 0
	for j in string:
		if j == char:
			print(Fore.GREEN, end='')
			counter += 1
		print(f'{j}{Style.RESET_ALL}', end='')
	if i['min'] <=counter <= i['max']:
		print(f'\t{Fore.GREEN}{counter}{Style.RESET_ALL}')
		part1 += 1
	else:
		print(f'\t{Fore.RED}{counter}{Style.RESET_ALL}')
