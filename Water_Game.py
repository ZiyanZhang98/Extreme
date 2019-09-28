from collections import Counter


def create_contestant(n, k):
    contestant = []
    for i in range(n):
        contestant.append(input())
    contestant[k - 1] += 'w'
    return contestant


def find_min_card(contestant, i):
    alist = list(contestant[i])
    dic = Counter(alist)
    return_dic = min(dic.values())
    return next(n for n in alist[::-1] if dic[n] == return_dic)


line1 = input()
n = int(line1[0])
k = int(line1[2])
contestant = create_contestant(n, k)
i = 0
while contestant[i] != contestant[i][::-1]:
        turn = 1
