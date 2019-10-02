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
    return winner


def pick_card(alist):
    return_card = 0
    for i in range(len(alist)):
        if alist[i] != 0 and alist[i] < alist[return_card]:
            return_card = i


deck = 'A23456789DQJK'
cards_value = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
               '9': 8, 'D': 9, 'Q': 10, 'J': 11, 'K': 12}
line1 = input()
n = int(line1[0])
k = int(line1[2])-1
contestants = create_contestants(n, cards_value)
winners = []
pass_wild_card = True
current_contestant = k
while True:
    for i in range(n):
        if winner_winner(contestants, i) and i != k:
            winners().append(i)
            break
    next_contestant = (current_contestant+1) % n
    if k == current_contestant and pass_wild_card:
        pass_wild_card = False





