input_str = ''

with open('input.txt') as f:
	input_str = f.read()

raw_passports = input_str.split('\n\n')
almost_not_raw = list(map(lambda x: x.replace('\n', ' '), raw_passports))
almost_not_raw = list(map(lambda x: x.split(' '), almost_not_raw))
done = []
for i in almost_not_raw:
	temp = list(filter(None, i))
	to_append = {}
	for j in temp:
		temp = j.split(':')
		to_append[temp[0]] = temp[1]
	done.append(to_append)

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valids = []
for i in done:
	vaild = True
	for j in required:
		try:
			x = i[j]
		except:
			vaild = False
			break
	if vaild:
		valids.append(i)

print(f'part 1: {len(valids)}')

part2 = 0
for i in valids:
	try:
		byr = int(i["byr"])
		if not 1920 <= byr <= 2002:
			continue

		iyr = int(i["iyr"])
		if not 2010 <= iyr <= 2020:
			continue

		eyr = int(i["eyr"])
		if not 2020 <= eyr <= 2030:
			continue

		if len(i["pid"]) != 9:
			continue
		pid = int(i["pid"])

		ecl = i["ecl"]
		if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			continue

		hcl = i["hcl"]
		if hcl[0] != '#':
			continue
		hcl_hex = hcl[1:]
		if len(hcl_hex) != 6:
			continue
		hex_valid = True
		for j in hcl_hex:
			if j not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
				hex_valid = False
				break
		if not hex_valid:
			continue

		hgt_valid = False
		hgt = i["hgt"]
		hgt_n = int(hgt[:-2])
		hgt_m = hgt[-2:]
		if hgt_m == 'cm':
			hgt_valid = 150 <= hgt_n <= 193
		elif hgt_m == 'in':
			hgt_valid = 59 <= hgt_n <= 76
		else:
			continue
		if not hgt_valid:
			continue

		part2 += 1
	except:
		continue

print(f'part 2: {part2}')