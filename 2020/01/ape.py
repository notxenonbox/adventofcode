to_solve = ''

with open('input.txt') as f:
	to_solve = f.read()

to_solve = list(filter(None, to_solve.split('\n')))
to_solve = list(map(int, to_solve))

part1 = None
for i in to_solve:
	for j in to_solve:
		if i + j == 2020:
			part1 = i * j
print(f'part 1: {part1}')

part2 = None
for i in to_solve:
	for j in to_solve:
		for k in to_solve:
			if i + j + k == 2020:
				part2 = i * j * k
print(f'part 2: {part2}')
