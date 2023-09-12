# task 1
# 1
def counter_sim_1(word: str) -> int:
    word = word.lower()
    counter = 0
    for symbol in set(word):
        if word.count(symbol) > 1:
            counter += 1
    return counter

# 2


def counter_sim_2(word: str) -> int:
    word = word.lower()
    return len([symbol for symbol in set(word) if word.count(symbol) > 1])

# 3


def counter_sim_3(word: str) -> int:
    word = word.lower()
    return sum([1 if word.count(symbol) > 1 else 0 for symbol in set(word)])


word = input()

print(counter_sim_1(word))
print(counter_sim_2(word))
print(counter_sim_3(word))

# task 2
# 1


def calc_power(power: int) -> str:
    return ['1', '-i', '-1', '-i'][power % 4]


for number in range(5):
    print(calc_power(number))

# task 3
def cyclic_shift(values: list, direction: str) -> list:
    steps = int(direction[1])
    if direction[0].lower() == 'b':
        return values[steps:] + values[:steps]
    elif direction[0].lower() == 'f':
        return values[len(values)-steps:] + values[:len(values)-steps]


data = [1, 2, 3, 4, 4, 5, 6, 7, 78, 9]

print(cyclic_shift(data, 'f10'))
print(cyclic_shift(data, 'b1'))
