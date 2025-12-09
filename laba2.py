#1. Створення списку
numbers = [10, 3, 25, 8, 14, 1, 7, 22, 5, 16]     # 10 int
strings = ["apple", "dog", "car", "banana", "sky",
           "alpha", "zero", "home", "python", "cat"]  # 10 str

main_list = numbers + strings   # об’єднання


# 2. Сортування
# окремо сортуємо інт і окремо стр
sorted_numbers = sorted([x for x in main_list if isinstance(x, int)])
sorted_strings = sorted([x for x in main_list if isinstance(x, str)])

sorted_main = sorted_numbers + sorted_strings


#3. Список елементів, кратних 2
even_numbers = [x for x in main_list if isinstance(x, int) and x % 2 == 0]


#4. Список строк у CAPS
strings_caps = [x.upper() for x in main_list if isinstance(x, str)]


#5. Вивід результатів
print("Головний список:", main_list)
print("Відсортований список:", sorted_main)
print("Список чисел кратних 2:", even_numbers)
print("Список рядків у CAPS:", strings_caps)
