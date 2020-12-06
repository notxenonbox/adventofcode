groups = ''
with open('input.txt') as f:
	groups = f.read()

# cleaning up
splitted = list(filter(None, groups.split('\n\n')))
groups = list(map(lambda x: list(filter(None, x.split('\n'))), splitted))

part1 = 0
for i in splitted:
	answers = list(i.replace('\n', ''))
	uniq = list(set(answers))
	part1 += len(uniq)
print(f'part 1: {part1}')

part2 = 0
for i in groups:
	summ = 0
	chars = range(ord('a'), ord('z')+1)
	for j in chars:
		for k in i:
			if chr(j) not in k:
				break
		else:
			summ += 1
	part2 += summ

print(f'part 2: {part2}')
