def find_min_card(contestant, i):
    alist = list(contestant[i])
    card = min(alist)
    # 这个肯定是不对的，不过我饿了，晚上再想
    return card


line1 = input()
n = int(line1[0])
k = int(line1[2])
contestant = []
for i in range(n):
    contestant.append(input())
# contestant[k-1] += 'w'
i = 0
while contestant[i] != contestant[i][::-1]:
        turn = 1
