from functools import reduce

allergens_map = {}

with open('input.txt') as f:
    for line in f:
        ingredients, allergens = line.split('(')
        ingredients = set([ingredient.strip() for ingredient in ingredients.split() if ingredient])
        allergens = allergens.split('contains')[1][:-2]
        allergens = set([allergen.strip() for allergen in allergens.split(',') if allergen])
        for allergen in allergens:
            if allergen in allergens_map:
                allergens_map[allergen].append(ingredients)
            else:
                allergens_map[allergen] = [ingredients]

allergens_possible = {}
for allergen, lists in allergens_map.items():
    possibles = reduce(set.intersection, lists)
    allergens_possible[allergen] = possibles


def backtrack(allergens, assigned):
    if len(allergens) == 0:
        return True

    allergen = allergens[0]
    for match in allergens_possible[allergen]:
        if all([match not in v for v in assigned.values()]):
            assigned[allergen] = match
            if backtrack(allergens[1:], assigned):
                return True
            del assigned[allergen]

    return False

matches = {}
backtrack(list(allergens_possible.keys()), matches)

lists = set([tuple(ingredients) for ingredients_lists in allergens_map.values() for ingredients in ingredients_lists])
not_matched = {}
for ingredients in lists: 
    for i in ingredients:
        if i not in matches.values():
            not_matched[i] = not_matched.get(i, 0) + 1

# part 1
print(sum(not_matched.values()))

# part 2
sorted_matches = dict(sorted(matches.items(), key=lambda item: item[0]))
print(','.join(sorted_matches.values()))
