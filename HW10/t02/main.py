# Создать программу для работы с учетными записями пользователей.
# Программа позволяет создавать, искать, править, фильтровать, удалять.
# Учетная запись пользователя представляет из себя словарь
# со следующими данными: имя, фамилия, дата рождения, профессия,
# числовой идентификатор(id). Для хранения данных использовать
# json файл. Задание выполнить в отдельной папке.

from utils import (
    show_all,
    write_new_record,
    edit_record,
    remove_record,
    search_by_id,
    filter_by_keyword,
    init_db,
)


def start():
    print(
        '''
        Hello. Choose what do you want to do
        --------------------
        1. Show all records.
        2. Add new record.
        3. Edit record.
        4. Remove record.
        5. Search by id.
        6. Filter by keyword.
        ------------------
        9. Init Data base.
        0. Exit. 
        '''
    )


def main():
    while True:
        start()
        desision = input('Write your desision: ')
        if not desision.isdigit():
            print('Wrong input')
            continue
        desision = int(desision)
        if not desision:
            print('See you next time')
            break
        elif desision == 1:
            show_all()
        elif desision == 2:
            write_new_record()
        elif desision == 3:
            edit_record()
        elif desision == 4:
            remove_record()
        elif desision == 5:
            search_by_id()
        elif desision == 6:
            filter_by_keyword()
        elif desision == 9:
            init_db()


if __name__ == "__main__":
    main()