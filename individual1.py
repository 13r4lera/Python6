#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date

def get_person():
    """
    Запросить данные о человеке
    """

    name = input("Фамилия и имя: ")
    phone = input("Номер телефона: ")
    year, month, day = map(int, input("Дата рождения (гггг мм дд): ").split())
    birthday = date(year, month, day)

    return {
        "name": name,
        "phone": phone,
        "birthday": birthday
    }

def display_people(everybody):
    """
    Вывести список всех людей
    """
    if everybody:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Фамилия Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        print(line)

        for idx, pers in enumerate(everybody, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    pers.get('name', ''),
                    pers.get('phone', ''),
                    str(pers.get('birthday', ''))
                )
            )

        print(line)

    else:
        print("Список людей пуст.")

def birthday_select(persons, birthday_month):
    result = []
    for pers in persons:
        if pers['birthday'].month == birthday_month:
            result.append(pers)

    return result




def main():
    people = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            person = get_person()
            people.append(person)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        elif command == "list":
            display_people(people)

        elif command.startswith('select'):
            parts = command.split(' ', maxsplit=1)
            birth_month = int(parts[1])

            selected = birthday_select(people, birth_month)
            display_people(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;\n")
            print("list - вывести список работников;\n")
            print("select <месяц> - вывести имена людей, у которых день рождение в этом месяце;\n")
            print("help - отобразить справку;\n")
            print("exit - завершить работу с программой;\n")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    sys.exit(main())