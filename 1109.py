# 1

# msg = 'Введите свои предметы, студент {0}:\n'
# sub1, sub2 = input(msg.format(1)).split(), input(msg.format(2)).split()

# print('Студенты вместе пойдут на', *(set(sub1) & set(sub2)))

# 2 из текста нужно сделать #AaaBbb, должна быть регистра от текста

# 1 вариант

# text = input('Введите текст для хэштэга: ')
# words = text.split()
# new_words = []
# for word in words:
#     new_words.append(word[0].upper() + word[1:].lower())

# print('#' + ''.join(new_words))

# 2 вариант

# print('#' + (input('Введите текст для хэштэга: ').title().replace(' ', '')))

# 3 циклы
# numbers_1 = [1,2,3,4]
# numbers_2 = [7,8,9]
# dict_numbers = dict()

# for num, num_2 in zip(numbers_1, numbers_2):
#     print(num, num_2)

# for num, num_2 in zip(numbers_1, numbers_2):
#     dict_numbers[num] = num_2

# print(dict_numbers)

# for value, key in zip(dict_numbers.keys(), dict_numbers.values()):
#     print(value, key)

# users = input('Введите имена пользователей: ').split()
# users_count = len(users)

# if not users_count:
#     print('Никому не понравилось')
# elif users_count == 1:
#     print(f'{users[0]} понравилось')
# elif users_count == 2:
#     print(f'{users[0]} и {users[1]} понравилось')
# elif users_count == 3:
#     print(f'{users[0]}, {users[1]} и {users[2]} понравилось')
# else:
#     print(f'{users[0]} и {users_count-1} пользователям понравилось')

