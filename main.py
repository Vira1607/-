print('НОД')

# Функция, вычисляющая наибольший общий делитель двух чисел

def divider(a, b):
  for number in range(1, a + 1):
    if (a % number == 0) and (b % number == 0):
      NOD = number
  return NOD

number_first = int(input('Введите первое число: '))
number_twice = int(input('Введите второе число: '))

if number_first > number_twice:
  answer = divider(number_first, number_twice)
else:
  answer = divider(number_twice, number_first)

print(answer)
