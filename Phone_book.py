# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

print("Перед вами телефонный справочник!")
book_file = open("phone_book.txt")
book_file.close()
 
def open_file(): 
    book_file = open("phone_book.txt", "r")
    print(book_file.read())
    book_file.close()

def new_contact():
    name = input("Введите имя контакта : ")
    phone_name = input("Введите номер контакта: ")
    information = input("Введите описание контакта: ")
    book_file = open("phone_book.txt", "a")
    filecontact= []
    filecontact = [ name," ", phone_name, " ", information +'\n']
    top = filecontact[0].split()
    top.extend(filecontact[:])
    book_file.writelines(filecontact)
    print(f'Сохранен контакт {filecontact}')
    #print (top)    
    book_file.close()

def delete_contact(): 
    book_file = open("phone_book.txt", "r")
    name_del = input("Введите удаляемые данные: ")
    data = book_file.read()
    data = data.replace(name_del, "")
    book_file = open("phone_book.txt", "w")
    book_file.write(data)
    print("Данные изменены")
    book_file.close

def deling():
    book_file = open("phone_book.txt", "w") 
    book_file.close()

def find_contact():
    book_file = open("phone_book.txt", "r")
    searched_contact = input("Введите искомый контакт: ")
    data = book_file.read().split('\n')
    for i in data:
        if searched_contact in i:
         print(i)
    book_file.close

def change_contact():
    book_file = open("phone_book.txt", "r")
    searched_contact = input("Введите искомый контакт: ")
    overwriting = input("Введите изменения: ")
    data = book_file.read()
    data = data.replace(searched_contact, overwriting)
    book_file = open("phone_book.txt", "w")
    book_file.write(data)
    print("Данные удалены")
    book_file.close

def main_menu():
  print("\nМеню телефонного справочника\n")
  print("1. Показать все контакты")
  print("2. Создать контакт")
  print("3. Поиск контакта")
  print("4. Удалить контакт")
  print("5. Изменить контакт")
  print("6. Выход")
  print("7. Очистка телефонной книги")
main_menu()
choice = input("Выберите номер пункта: ")
main_menu()
if choice == "1":
    open_file()
    enter = input("Нажмите Enter чтобы продолжить ") 
    main_menu()
elif choice == "2":
    new_contact()
    enter = input("Нажмите enter чтобы продолжить")
    main_menu()
elif choice == "3":
    find_contact()
    enter = input("Нажмите enter чтобы продолжить")
    main_menu()
elif choice == "4":
    delete_contact()
    enter = input("Нажмите enter чтобы продолжить")
    main_menu()
elif choice == "5":
    change_contact()
    enter = input("Нажмите enter чтобы продолжить")
    main_menu()
elif choice == "6":
    print("До свидания!")
    enter = input("Нажмите enter чтобы продолжить")
    main_menu()
elif choice == "7":
    deling()
    print('Книга пуста!')
    enter = input("Нажмите enter чтобы продолжить")
    main_menu()
else:
    print("Вы не туда попали, попроуйте заново, Приятного дня!")
    main_menu()
