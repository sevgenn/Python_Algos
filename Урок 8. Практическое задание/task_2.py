'''
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''

""""
Придумывать самостоятельное решение не стал, т.к. на данном этапе оно все равно
будет хуже существующих вариантов.
Посчитал, что это тот случай, когда полезнее разобраться в лучших решениях.
"""

from collections import Counter, deque


def huffman_dict(st):
    count = Counter(st)
    count_sorted = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(count_sorted) != 1:
        while len(count_sorted) > 1:
            weight = count_sorted[0][1] + count_sorted[1][1]
            comb = {0: count_sorted.popleft()[0], 1: count_sorted.popleft()[0]}

            for i, _count in enumerate(count_sorted):
                if weight > _count[1]:
                    continue
                else:
                    count_sorted.insert(i, (comb, weight))
                    break
            else:
                count_sorted.append((comb, weight))
    else:
        weight = count_sorted[0][1]
        comb = {0: count_sorted.popleft()[0], 1: None}
        count_sorted.append((comb, weight))
    return count_sorted[0][0]


code = dict()

def huffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code[tree] = path
    else:
        huffman_code(tree[0], path=f'{path}0')
        huffman_code(tree[1], path=f'{path}1')

st_in = "beep boop beer!"

huffman_code(huffman_dict(st_in))

for i in st_in:
    print(code[i], end=' ')
print()

