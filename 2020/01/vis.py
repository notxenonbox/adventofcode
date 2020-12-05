from colorama import Fore, Style

UP_ONE_LINE = "\033[F\033[K"

to_solve = ''

with open('input.txt') as f:
	to_solve = f.read()

to_solve = list(filter(None, to_solve.split('\n')))
to_solve = list(map(int, to_solve))

print('-' * 10, 'Part 1', '-' * 10, '\n')
part1 = None
for i in to_solve:
	for j in to_solve:
		print(f'{UP_ONE_LINE}{i} + {j} = {i + j}\t', f'{Fore.GREEN}O{Style.RESET_ALL}' if i + j == 2020 else f'{Fore.RED}X{Style.RESET_ALL}')
		if i + j == 2020:
			print(f'{i} * {j} = {Fore.GREEN}{i * j}{Style.RESET_ALL}\n')
			part1 = i * j
			break

print('-' * 10, 'Part 2', '-' * 10, '\n')
part2 = None
for i in to_solve:
	for j in to_solve:
		for k in to_solve:
			print(f'{UP_ONE_LINE}{i} + {j} + {k} = {i + j + k}\t', f'{Fore.GREEN}O{Style.RESET_ALL}' if i + j + k == 2020 else f'{Fore.RED}X{Style.RESET_ALL}')
			if i + j + k == 2020:
				print(f'{i} * {j} * {k} = {Fore.GREEN}{i * j * k}{Style.RESET_ALL}\n')
				part2 = i * j * k
				break

print('-' * 10, 'Summary', '-' * 10)
print('Part 1:', part1)
print('Part 2:', part2)