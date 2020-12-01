to_solve = ''

with open('input.txt') as f:
	to_solve = f.read()

to_solve = list(filter(None, to_solve.split('\n')))
to_solve = list(map(int, to_solve))

print('Part 1', '-' * 15)

for i in to_solve:
	for j in to_solve:
		if i + j == 2020:
			print(f'{i} + {j} = 2020')
			print(f'{i} * {j} = {i * j}')

print('Part 2', '-' * 15)

for i in to_solve:
	for j in to_solve:
		for k in to_solve:
			if i + j + k == 2020:
				print(f'{i} + {j} + {k} = 2020')
				print(f'{i} * {j} * {k} = {i * j * k}')