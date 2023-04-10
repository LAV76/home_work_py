# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может
# ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
import os

# определение имени файла
filename = 'contacts.txt'

# проверка наличия файла, и создание, если его нет
if not os.path.exists(filename):
    with open(filename, 'w', encoding="utf8"):
        pass

# функция для добавления новой записи
def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(filename, 'a', encoding="utf8") as f:
        f.write(f'{surname} {name} {patronymic} {phone_number}\n')
    print('Контакт добавлен успешно!')

# функция для поиска записей по имени, фамилии или отчеству
def find_contact():
    search = input('Введите имя, фамилию или отчество: ')
    with open(filename, 'r', encoding="utf8") as f:
        for line in f:
            if search.casefold() in line.casefold():
                print(line.strip())

# функция для изменения записи
def edit_contact():
    search = input('Введите имя или фамилию для поиска: ')
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
    with open(filename, 'w', encoding="utf8") as f:
        for line in lines:
            if search.casefold() in line.casefold():
                name, surname, patronymic, phone_number = line.split()
                print(f'Найден контакт: {surname} {name} {patronymic} {phone_number}')
                print('Введите новые данные или нажмите Enter, чтобы оставить прежнее значение')
                new_name = input(f'Имя ({name}): ') or name
                new_surname = input(f'Фамилия ({surname}): ') or surname
                new_patronymic = input(f'Отчество ({patronymic}): ') or patronymic
                new_phone_number = input(f'Номер телефона ({phone_number}): ') or phone_number
                f.write(f'{new_surname} {new_name} {new_patronymic} {new_phone_number}\n')
                print('Контакт изменен успешно!')
            else:
                f.write(line)

# функция для удаления записи
def delete_contact():
    search = input('Введите имя или фамилию для поиска: ')
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
    with open(filename, 'w', encoding="utf8") as f:
        for line in lines:
            if search.casefold() not in line.casefold():
                f.write(line)
        print('Контакт удален успешно!')

# функция для вывода всех записей
def display_contacts():
    with open(filename, 'r', encoding="utf8") as f:
        for line in f:
            print(line.strip())


while True:
    print('\nВыберите действие:')
    print('1. Добавить контакт')
    print('2. Найти контакт')
    print('3. Изменить контакт')
    print('4. Удалить контакт')
    print('5. Показать все контакты')
    print('6. Выход')
    choice = input('> ')
    if choice == '1':
        add_contact()
    elif choice == '2':
        find_contact()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        display_contacts()
    elif choice == '6':
        break