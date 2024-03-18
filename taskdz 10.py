#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.

def min_flips(coins):
    heads = 0
    tails = 0

    for coin in coins:
        if coin == 'H':
            heads += 1
        else:
            tails += 1

    return min(heads, tails)

# Пример использования
coins = input("Введите последовательность монет (например, 'HHHTTT'): ")
print("Минимальное количество переворотов:", min_flips(coins))