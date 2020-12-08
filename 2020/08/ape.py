def execute_instruction(ins, acc, rip):
	opcode, arg = ins.split(' ')
	if opcode == 'nop':
		rip += 1
		return acc, rip
	elif opcode == 'jmp':
		rip += int(arg)
		return acc, rip
	else:
		acc += int(arg)
		rip += 1
		return acc, rip

instructions = []
with open("input.txt") as f:
	instructions = f.readlines()


seen = []
acc = 0
rip = 0
for i in instructions:
	seen.append(False)

while True:
	if seen[rip] == True:
		break
	seen[rip] = True
	acc, rip = execute_instruction(instructions[rip], acc, rip)

print(f'part 1: {acc}')

# part2
for ind, ins in enumerate(instructions):
	acc = 0
	rip = 0

	opcode, arg = ins.split(' ')
	if opcode == 'jmp':
		opcode = 'nop'
	elif opcode == 'nop':
		opcode = 'jmp'


	patch_n = ind
	patch = f'{opcode} {arg}'
	seen = []
	for _ in instructions:
		seen.append(False)

	try:
		while True:
			if seen[rip] == True:
				break
			seen[rip] = True
			ins = instructions[rip]
			if rip == patch_n:
				ins = patch
			acc, rip = execute_instruction(ins, acc, rip)
	except:
		print(f'part 2: {acc}')
		break
