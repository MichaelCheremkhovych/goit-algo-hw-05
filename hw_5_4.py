contacts = {} # Створюємо порожній словник для зберігання контактів

def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    Обробляє винятки KeyError, ValueError, IndexError.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f"Error: {e}")
            return None
    return wrapper

def parse_input(command):
    """
    Функція для розбору введеної команди.
    """
    parts = command.split()
    if len(parts) < 1:
        return None, []
    return parts[0].lower(), parts[1:]

@input_error
def add_contact(name, phone_number):
    """
    Функція для додавання контакту.
    """
    contacts[name] = phone_number
    print("Contact added.")

@input_error
def change_contact(name, new_phone_number):
    """
    Функція для зміни номеру телефону контакту.
    """
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        raise ValueError("Contact not found.")

@input_error
def show_phone(name):
    """
    Функція для відображення номеру телефону контакту.
    """
    if name in contacts:
        print(contacts[name])
    else:
        raise KeyError("Contact not found.")

def show_all():
    """
    Функція для відображення усіх контактів.
    """
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")

def main():
    """
    Основна функція, яка керує виконанням програми.
    """
    print("Welcome to the assistant bot!") # Виводимо привітальне повідомлення
    while True: # Безкінечний цикл для обробки команд користувача
        command = input("Enter command: ") # Очікуємо введення команди від користувача
        action, args = parse_input(command) # Розбираємо введену команду на дію та аргументи
        if action == "exit" or action == "close": # Виконуємо відповідну дію в залежності від команди
            print("Good bye!") # Виводимо прощальне повідомлення та завершуємо програму
            break
        elif action == "hello":
            print("How can I help you?") # Виводимо запитання "How can I help you?"
        elif action == "add":
            if len(args) != 2: # Додаємо контакт за введеними аргументами
                print("Invalid arguments for 'add' command.")
            else:
                add_contact(args[0], args[1])
        elif action == "change":
            if len(args) != 2: # Змінюємо контакт за введеними аргументами
                print("Invalid arguments for 'change' command.")
            else:
                change_contact(args[0], args[1])
        elif action == "phone":
            if len(args) != 1: # Виводимо номер телефону за введеним аргументом
                print("Invalid arguments for 'phone' command.")
            else:
                show_phone(args[0])
        elif action == "all":
            show_all() # Виводимо усі контакти
        else:
            print("Unknown command.") # Виводимо повідомлення про невідому команду

if __name__ == "__main__": # Перевіряємо, чи цей файл є головним, і викликаємо основну функцію
    main()
