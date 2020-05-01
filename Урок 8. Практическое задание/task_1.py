'''
Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
'''















import hashlib

STR_ORIGINAL = input('Enter the string - ').lower()
SUB_STR = set()

for i in range(len(STR_ORIGINAL)):
	for j in range(i,len(STR_ORIGINAL)):
		SUB_STR.add(hashlib.sha1(STR_ORIGINAL[i:j+1].encode('utf-8')).hexdigest())

print(f'Quantity of the substrings - {len(list(SUB_STR))}')
