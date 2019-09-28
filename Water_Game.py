from collections import Counter


def create_contestant(n, k):
    contestant = []
    for i in range(n):
        contestant.append(input())
    contestant[k - 1] += 'w'
    return contestant


def find_min_card(contestant, i):
    alist = list(contestant[i])
    return_list = []
    cnt = Counter(alist)
    min_cnt = min(cnt.values())
    for n in alist:
        if cnt[n] == min_cnt:
            return_list.append(n)
    return min(return_list)


line1 = input()
n = int(line1[0])
k = int(line1[2])
contestant = create_contestant(n, k)
i = 0
turn = 1
while contestant[i] != contestant[i][::-1]:
    