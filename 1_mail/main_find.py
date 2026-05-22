import re

# Извлекает буквенные слова из строки (без цифр и спецсимволов)
def extract(input_string):
    return re.findall(r'[a-zA-Z]+', input_string)

# генерирует все возможные "слова" от 3 букв
def generate_some_words(sequence):
    n = len(sequence)
    possible_words = []
    # далее "создает" слово и добавляет в массив
    # for length in range(3, n + 1): # от короткого (3 букв) до длинного
    for length in range(n, 2, -1): # от длинного до короткого (3 букв)
        for start in range(0, n-length+1):
            possible_words.append(sequence[start:start + length])
    return possible_words

# Проверяет, есть ли хотя бы одно слово из списка в файле
def check_words_in_file(words, file_path = 'main_engl_words.txt'):
    # Начиная с длинного "слова"
    with open(file_path) as file:
        word_set = set() # множество (set) так как он хэшируем
        for line in file:
            word_set.add(line.strip().lower())
    
    for word in words:
        if word.lower() in word_set:
            return True, word
    return False, ""

def filter(input_string, word_file="main_engl_words.txt"):
    letter_sequences = extract(input_string)
    # print('extract', letter_sequences)
    
    for seq in letter_sequences:
        possible_words = generate_some_words(seq)
        # print('generate_some_words', seq, possible_words)
    
        found, matched_word = check_words_in_file(possible_words, word_file)
        
        if found:
            print(f'✅ Найдено совпадение |{seq}| --> |{matched_word}|')
            return matched_word
        # else:
        #     print('❌ нету совпадений')

    # print('❌ вообще нету совпадений')
    return 'нету совпадений'

# # Пример
# input_str = "abcdef2312whiteman!$jkdasnjlovenjaks"
# print(filter(input_str, 'eng_web2.txt'))
