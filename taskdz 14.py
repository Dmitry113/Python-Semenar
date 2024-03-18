# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

def powers_of_two(N):
    power = 1
    result = []
    while power <= N:
        result.append(power)
        power *= 2
    return result

# Пример использования
N = int(input("Введите число N: "))
print("Целые степени двойки, не превосходящие", N, ":")
print(powers_of_two(N))

