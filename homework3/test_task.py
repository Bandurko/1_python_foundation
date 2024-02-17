
items = {
    "спальник": 1.0,
    "палатка": 2.0,
    "термос": 0.5,
    "карта": 0.1,
    "фонарик": 0.2,
    "котелок": 0.5,
    "еда": 2.0,
    "одежда": 1.0,
    "обувь": 0.8,
    "нож": 0.2
}
max_weight = 10.0




import warnings

warnings.filterwarnings('ignore')

#-----------------------------

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

#-----------------------------


max_weight = 10.0
backpacks_test = []
sorted_result = []
for i in range(2**len(items)):
    backpack_test = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack_test[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks_test.append(backpack_test)

full_result = [backpack_test for backpack_test in backpacks_test if backpack_test]
result = []
for item in full_result:
    if item not in result:
        result.append(item)

x = 0
for i in result:
    if dict(sorted(i.items(), key=lambda item: item[1], reverse=True)) == dict(sorted(backpack.items(), key=lambda item: item[1], reverse=True)):
        x += 1
if x > 0:
    print(True)
else:
    print(False)


