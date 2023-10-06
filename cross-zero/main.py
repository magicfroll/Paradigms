from models import Bar, User


def main():
    users = []
    user_cross_name = input("В ведите имя игрока, который будет ставить '+'\n>>> ")
    user_cross = User(user_cross_name, '+')
    users.append(user_cross)
    user_zero_name = input("В ведите имя игрока, который будет ставить 'o'\n>>> ")
    user_zero = User(user_zero_name, 'o')
    users.append(user_zero)
    bar = Bar()
    print()
    bar.print()

    count = 0
    user_num = 0

    while bar.is_winner == False and bar.is_draw == False:
        cell = input(f"{users[user_num].name}, в какую ячейку вы хотите поставить {users[user_num].symbol}?\n>>> ")
        print()
        if bar.is_none(cell):
            bar.wrong_cell = True
        while bar.wrong_cell:
            print('Вы неверно указали номер ячейки! Попробуйте еще раз')
            cell = input(f"{users[user_num].name}, в какую ячейку вы хотите поставить {users[user_num].symbol}?\n>>> ")
            if bar.is_none(cell):
                bar.wrong_cell = True
            else:
                bar.wrong_cell = False
        bar.put_symbol(cell, users[user_num].symbol)
        bar.print()
        if bar.check_is_over(users[user_num].symbol):
            print(f'{users[user_num].name} выиграл!')
        elif bar.is_draw:
            print('Ничья!')

        count += 1
        user_num = count % 2

if __name__ == '__main__':
    main()


"""
Использовал структурную парадигму и ООП. Структурную, т.к. так быстрее и переиспользование не планируется. 
ООП - т.к. необходимо хранить значения переменных, а также из-за инкапсуляции - скрыта неоптимальная реализация)))  
"""

