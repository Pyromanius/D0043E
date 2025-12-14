print("\n---- 03 ----\n")

str = "I love programming. Programming is fun!"
str2 = str.replace("Programming", "Python")
print(str2)

print("\n---- 10 ----\n")

numbers = list(range(1, 11))

for i in range(len(numbers)):
    if numbers[i] < 6:
        continue
    print(numbers[i])

print("\n---- 13 ----\n")

my_list = [10, 20, 30, 40]
for i in my_list:
    print(i * 2)

print("\n---- 15 ----\n")

person = {'name': 'John', 'age': 30, 'profession': 'Engineer'}
print(person['profession'])