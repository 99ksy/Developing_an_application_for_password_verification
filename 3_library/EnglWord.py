import re

def three_var(): # делает из файла где перевод в файл без перевода
    with open('eng_перевод_из_трех_букв.txt', 'r') as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        stripped_line = line.rstrip('\n')  # Удаляем символ перевода строки
        tokens = re.split(r'[\s-]+', stripped_line)  # Разделяем по пробелам или дефисам
        first_word = next((token for token in tokens if token), '')
        processed_lines.append(first_word + '\n')

    with open('eng_слова_из_трех_букв.txt', 'w') as file:
        file.writelines(processed_lines)


# Функция для сохранения в файл
def save_set_to_file(my_set, filename):
    with open(filename, 'w') as f:
        for item in my_set:
            f.write(f"{item}\n")
'''
# Функция для загрузки множества из файла
# def BAD_load_set_from_file(filename): # BAD!!!!
#     try:
#         with open(filename, 'r') as f:
#             return {line.strip() for line in f} # {} - это
#     except FileNotFoundError:
#         return set()  # Возвращаем пустое множество, если файл не найден

def load_set_from_file(filename):
    try:
        result = set()
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if len(word) > 3 and len(word) < 11:  # Проверка длины слова
                    duplicate = False
                    for i in range(len(word) - 1):
                        if word[i] == word[i + 1]:
                            duplicate = True
                            break
                    if duplicate == False:
                        result.add(word)
        return result
    except FileNotFoundError:
        return set()  # Возвращаем пустое множество, если файл не найден


three_var()
# Пример использования
filename = 'new_new.txt'
my_set = load_set_from_file('web2.txt')

# Сохранение множества обратно в файл
save_set_to_file(my_set, filename)
'''

def load_set_from_BIG_file(filename):
    try:
        result = []
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if len(word) > 3 and len(word) < 11:  # Проверка длины слова
                    # удаляем дубликаты (две буквы рядом нельзя)
                    duplicate = False
                    for i in range(len(word) - 1):
                        if word[i] == word[i + 1]:
                            duplicate = True
                            break
                    if duplicate == False:
                        result.append(word)
        return result
    except FileNotFoundError:
        return []  # Возвращаем пустое множество, если файл не найден

def load_set_from_SMALL_file(filename):
    try:
        result = []
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if word:  # Проверяем, что строка не пустая
                    result.append(word)
        return result
    except FileNotFoundError:
        return []  # Возвращаем пустое множество, если файл не найден
    

three_var() # делает из файла где перевод в файл без перевода
# Загружаем слова
main_words = load_set_from_BIG_file('eng_web2.txt')
three_letter_words = load_set_from_SMALL_file('eng_слова_из_трех_букв.txt')

# Объединяем
all_words = main_words + three_letter_words

# Сохраняем БЕЗ СОРТИРОВКИ
save_set_to_file(all_words, 'new_new.txt')

# Проверка наличия слова
print("banana" in all_words)  # True/False