"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    N = input('Enter some natural number or "Q" to exit: ')
    if N.lower() == 'q':
        break
    else:
        try:
            N = int(N)
        except ValueError:
            print("It is not a number. Try again.\n")
            continue
        S1 = 0
        S2 = N * (N + 1) // 2
        for i in range(1, N+1):
            S1 += i
        print('S1 = S2 is', S1 == S2)
        print(f'The left side is {S1}\nThe right side is {S2}\n')
print('Finish.')
