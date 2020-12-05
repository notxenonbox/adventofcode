boarding_passes = ''
with open('input.txt') as f:
	boarding_passes = f.read()

# cleaning it up
boarding_passes = boarding_passes.split('\n')
boarding_passes = list(filter(None, boarding_passes))

# part 1
existing = []
for i in boarding_passes:
	seatID = ''
	for j in i:
		if j in ['B', 'R']:
			seatID += '1'
		if j in ['F', 'L']:
			seatID += '0'
	seatID = int(seatID, 2)
	existing.append(seatID)

existing.sort()
maximum = existing[-1]
print(f'part 1: {maximum}')

# part 2
minimum = existing[0]
for i in range(minimum, maximum):
	if i not in existing:
		print(f'part 2: {i}')
		break