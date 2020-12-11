import re

rules = []
with open('input.txt') as f:
    rules = [line.strip() for line in f]

contents = {}
for rule in rules:
    bag, contained_bags = rule.split('contain')
    contained_bags = [b.strip() for b in contained_bags.split(',')]
    parsed_contained_bags = [re.match('(\d)\s([\s\w]+)\s((bags)|(bag))', b) for b in contained_bags]
    parsed_contained_bags = [(int(m.group(1)), m.group(2)) for m in parsed_contained_bags if m]
    contents[bag.split('bags')[0].strip()] = parsed_contained_bags


def find(bag_name, searched_bag):
    return bag_name == searched_bag or any([find(b[1], searched_bag) for b in contents[bag_name]])


# part 1
print(sum([any([find(b[1], 'shiny gold') for b in contents[rule]]) for rule in contents]))


def bag_size(bag_name):
    return sum([b[0] + b[0] * bag_size(b[1]) for b in contents[bag_name]])


# part2
print(sum([b[0] + b[0] * bag_size(b[1]) for b in contents['shiny gold']]))
