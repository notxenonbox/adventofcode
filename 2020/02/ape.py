to_solve = ''

with open('input.txt') as f:
	to_solve = f.readlines()

to_solve = list(map(lambda x: x.split(': '), to_solve))
temp = []

for i in to_solve:
	ttemp = i[0].split(' ')
	tttemp = ttemp[0].split('-')
	ttttemp = {'char': ttemp[1], 'passwd': i[1], 'min': int(tttemp[0]), 'max': int(tttemp[1])}
	temp.append(ttttemp)

to_solve = temp
part1 = 0

for i in to_solve:
	char = i['char']
	string = i['passwd']
	counter = 0
	for j in string:
		if j == char:
			counter += 1
	if i['min'] <=counter <= i['max']:
		part1 += 1

print(f'part 1: {part1}')

part2 = 0

for i in to_solve:
	char = i['char']
	string = i['passwd']
	counter = 0
	if string[i['min']-1] == char:
		counter += 1
	if string[i['max']-1] == char:
		counter += 1
	if counter == 1:
		part2 += 1

print(f'part 2: {part2}')
