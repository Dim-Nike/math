from random import randint


PARTICIPANTS = 100

class Person:
    def __init__(self, number):
        self.number = number
        self.is_active = True
        self.attempt = PARTICIPANTS // 2
        self.list_check_box = []
        self.win = False

    def check_box(self, list_box):
        while True:
            if self.attempt >= 1:
                choice_box = randint(1, len(list_box))
                if choice_box not in self.list_check_box:
                    self.list_check_box.append(choice_box)
                    # print(F'Мой номер - {self.number}\n'
                    #       F'Я выбираю номер - {choice_box}\n'
                    #       F'Номер коробки - {list_box[choice_box - 1].number_box}\n'
                    #       F'Индекс коробки - {list_box[choice_box - 1].index}')
                    if self.number == list_box[choice_box-1].index:
                        self.win = True
                        # print(f'Игрок под номером {self.number} выиграл!')
                        # print(F'Попытка - {self.attempt}')
                        break
                    else:
                        self.attempt -= 1
                        # print(F'Попытка - {self.attempt}')
                        # print('Не совпало!')
                else:
                    continue
            else:
                # print('Попытки закончились')
                break

    def check_box_algorithm(self, list_box):
        next_step = 0
        while True:
            if self.attempt >= 1:
                if next_step == 0:
                    choice_box = self.number
                else:
                    choice_box = next_step
                if choice_box not in self.list_check_box:
                    self.list_check_box.append(choice_box)
                    # print(F'Мой номер - {self.number}\n'
                    #       F'Я выбираю номер - {choice_box}\n'
                    #       F'Номер коробки - {list_box[choice_box - 1].number_box}\n'
                    #       F'Индекс коробки - {list_box[choice_box - 1].index}')
                    if self.number == list_box[choice_box - 1].index:
                        self.win = True
                        # print(f'Игрок под номером {self.number} выиграл!')
                        # print(F'Попытка - {self.attempt}')
                        break
                    else:
                        self.attempt -= 1
                        # print(F'Попытка - {self.attempt}')
                        # print('Не совпало!')
                        next_step = list_box[choice_box - 1].index
                        continue
                else:
                    continue
            else:
                # print('Попытки закончились')
                break



class Box:
    def __init__(self, number_box, index=1):
        self.number_box = number_box
        self.index = index






