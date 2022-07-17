import random
from controller import PARTICIPANTS
from controller import Person, Box
list_order = list(range(1, PARTICIPANTS + 1))



list_person = []


for person_number in list_order:
    list_person.append(Person(number=person_number))



# for box in list_box:
#     print(f'Номер коробки - {box.number_box}, Индекс коробки - {box.index}')

# for player in list_person:
#     player.check_box_algorithm(list_box=list_box)
#
# count_win = 0
# for win_player in list_person:
#     if win_player.win:
#         count_win += 1

# print(f'Всего победителей - {count_win}!')

count_play = 0
count_win = 0
while count_play < 100:
    count_player_win = 0
    count_play += 1

    list_box = []
    list_random = list(range(1, PARTICIPANTS + 1))
    random.shuffle(list_random)
    dict_random = {}

    for key in list_order:
        k = key
        dict_random[k] = list_random[key - 1]

    for number_box, index_box in dict_random.items():
        list_box.append(Box(number_box=number_box, index=index_box))

    for player in list_person:
        player.attempt = len(list_person) // 2
        player.list_check_box = []
        player.win = False

    for player in list_person:
        player.check_box_algorithm(list_box=list_box)

    for player in list_person:
        if player.win:
            count_player_win += 1
    # print(f'Количество победителей - {count_player_win}/{len(list_person)}')

    if count_player_win == len(list_person):
        count_win += 1



print(f'Всего пройденных игр - {count_win}/{count_play}')
print(f'Выигрыш в процентах - {count_win // count_play * 100}%')