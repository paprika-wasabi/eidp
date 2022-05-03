# MIN = []
# i = int(input())
# for x in range(i):
#     k, b = input().split(" ")
#     k = int(k)
#     b = int(b)
#     com = []
#     card = input().split(" ")
#     for value in range(k):
#         if value >= 1 and value < k - 1:
#             com.append(int(card[value - 1]) * int(card[value]) * int(card[value + 1]))
#     num_min = int(min(com))
#     print(min(com))
#     for value in range(k):
#         if value >= 1 and value < k - 1:
#             if int(card[value - 1]) * int(card[value]) * int(card[value + 1]) == num_min:
#                 pass
#             print(card)
#     MIN.append(min(com))
# print(MIN)

def pick_card(cards: list):
    i = len(cards)
    for value in range(i):
        if value >= 1 and value < i - 1:
            cards.pop(value)
            return cards
    
    
def pick_until_2(cards: list):
    x = len(cards)
    while x > 2:
        pick_card(cards)
        x = len(cards)
    return cards


cards = [30, 35, 15, 5, 10, 20, 25]
cards2 = [1, 20, 1]
print(pick_card(cards))
print(pick_until_2(cards))