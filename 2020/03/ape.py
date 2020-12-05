lines = []
with open('input.txt') as f:
	lines = f.readlines()
lines = list(map(lambda x: x.strip(), lines))

linelen = len(lines[0])
linec = len(lines)

def check(x, y):
	posX = 0
	posY = 0
	trees = 0
	while posY < linec:
		if lines[posY][posX % linelen] == '#':
			trees += 1
		posX+=x
		posY+=y
	return trees

print(f'part 1: {check(3, 1)}')

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1

for i in slopes:
	result *= check(i[0], i[1])

print(f'part 2: {result}')
