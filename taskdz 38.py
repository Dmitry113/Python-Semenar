"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных."""

def add_contact(contacts, name, phone_number):
    contacts[name] = phone_number
    print("Контакт успешно добавлен:", name, "-", phone_number)

def update_contact(contacts, name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Контакт успешно обновлен:", name, "-", new_phone_number)
    else:
        print("Контакт не найден:", name)

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print("Контакт успешно удален:", name)
    else:
        print("Контакт не найден:", name)

def main():
    contacts = {}
    while True:
        print("\nТелефонный справочник:")
        print("1. Добавить контакт")
        print("2. Обновить контакт")
        print("3. Удалить контакт")
        print("4. Вывести все контакты")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(contacts, name, phone_number)
        elif choice == "2":
            name = input("Введите имя контакта для обновления: ")
            new_phone_number = input("Введите новый номер телефона: ")
            update_contact(contacts, name, new_phone_number)
        elif choice == "3":
            name = input("Введите имя контакта для удаления: ")
            delete_contact(contacts, name)
        elif choice == "4":
            if contacts:
                print("Все контакты:")
                for name, phone_number in contacts.items():
                    print(name, "-", phone_number)
            else:
                print("Телефонный справочник пуст.")
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")

if __name__ == "__main__":
    main()
