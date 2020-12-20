#create input file and then open the file and get day 7 input supplied by adventofcode

import re
r = open("Inputday7.txt", "r")

#using readlines
rules = {}
pattern = r"(\d+|no)? ?(\w+ \w+) bags?"
for line in r.readlines():
	(_,bag), *inner = re.findall(pattern, line)
	rules[bag] = {inner_bag: int(n) for n, inner_bag in inner if n}

#find shiny gold bags
def contain_gold(bag, rules):
	for inner_bag in rules[bag]:
		if contain_gold(inner_bag, rules) or inner_bag == "shiny gold":
			return True
	return False

#count how many bag colors can contain at least one shiny gold bag - 355
count = sum([contain_gold(bag, rules)for bag in rules])
print("Part 1: {0}".format(count))

#How many individual bags are required inside your single shiny gold bag? - 5312

def count_containing_bags(bag, rules):
	return sum([n + n * count_containing_bags(inner_bag, rules) for inner_bag, n in rules[bag].items()])

print("Part 2: {0}".format(count_containing_bags('shiny gold', rules)))
