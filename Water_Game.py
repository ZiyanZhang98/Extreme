def create_contestants(num, dic):
    hand = []
    for i in range(num):
        hand.append([0] * 13)
        sets = list(input())
        for card in sets:
            hand[i][dic[card]] += 1
    return hand


def winner_winner(dlist, i):
    winner = False
    for card in dlist[i]:
        if card == 4:
            winner = True
            break
    return winner


def pick_card(alist):
    mn = -1
    for i in range(len(alist)):
        if alist[i] != 0 and (mn == -1 or alist[i] < alist[mn]):
            mn = i
    return mn


def play(n, k, contestants):
    current_contestant = k
    pass_wild_card = False
    for i in range(n):
        if winner_winner(contestants, i) and i != k:
            return i
    while True:
        next_contestant = (current_contestant + 1) % n
        if k == current_contestant and pass_wild_card is True:
            pass_wild_card = False
            k = next_contestant
        else:
            pass_wild_card = True
            card = pick_card(contestants[current_contestant])
            contestants[current_contestant][card] -= 1
            contestants[next_contestant][card] += 1
        if winner_winner(contestants, current_contestant) and k != current_contestant:
            return current_contestant
        current_contestant = next_contestant


deck = 'A23456789DQJK'
cards_value = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
               '9': 8, 'D': 9, 'Q': 10, 'J': 11, 'K': 12}
line1 = input()
n = int(line1[0])
k = int(line1[2])-1
contestants = create_contestants(n, cards_value)
print(play(n, k, contestants)+1)




