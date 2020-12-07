import re
class Bag:
	def __init__(self, _name, _contents):
		self.name = _name
		self.contents = _contents
		self.c_cache = None
		self.has_cache = {}

	def hasBagType(self, _name, bags):
		try:
			return self.has_cache[_name]
		except:
			if _name != self.name:
				for i in self.contents:
					if bags[i[1]].hasBagType(_name, bags):
						break
				else:
					return False
				return True
			else:
				return True
	
	def children_count(self):
		if self.c_cache != None:
			return self.c_cache
			
		count = 0
		for i in self.contents:
			count += i[0] + (i[0] * bags[i[1]].children_count())
		
		self.c_cache = count
		return count

input_lines = []
with open('input.txt') as f:
	input_lines = f.readlines()

input_lines = list(filter(None, input_lines))

bags = {}

for i in input_lines:
	bag, contents = re.search(r'^((?:[\w]+ ){2})bags contain ([\S\s]+)', i).groups()
	if contents.strip() == "no other bags.":
		bag = bag.strip()
		bags[bag] = Bag(bag, [])
		continue
	contents = contents.split(', ')
	contents = list(map(lambda x: re.search(r'(\d)+ ((?:[\w]+ ){2})', x).groups(), contents))

	# cleaning up
	contents = list(map(lambda x: (int(x[0]), x[1].strip()), contents))
	bag = bag.strip()

	bags[bag] = Bag(bag, contents)

part1 = -1
for i in bags.values():
	if i.hasBagType("shiny gold", bags):
		part1 += 1

print(f'part 1: {part1}')
print(f'part 2: {bags["shiny gold"].children_count()}')