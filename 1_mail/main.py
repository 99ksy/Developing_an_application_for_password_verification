import tkinter as tk
from tkinter import messagebox
import sys
import re
import main_find

with open('main_engl_words.txt', 'r', encoding='utf-8') as file:
    english_words = [line.strip() for line in file if line.strip()]

_SEL_LANG = None
_RESULT = True

messages = {
    'rus': {
        'language_select_title': 'Выбор языка/Lang selection',
        'language_select_label': 'Выберите язык | Select a Language',
        'button_rus': 'РУС',
        'button_us': 'ENG',
        'app_title': 'Project K',
        'password_types': ['Простой', 'Средний', 'Сложный'],
        'ok': 'OK',
        'not_ok': 'Не подойдёт!',
        'rul': 'Правила безопасности пароля:',
        'result': 'Результат проверки:',
        'entry_pass':{
            'введите': 'Введите пароль',
            'kol-vo': 'Символов:'
        },
        'rules': {
            'simple': [
                {'title': 'Пароль должен содержать минимум 6 символов.',
                 'len': 6},
                {'title': 'Пароль должен содержать хотя бы одну заглавную букву.',
                 'l': 1},
                {'title': 'Пароль должен содержать хотя бы одну цифру.',
                 'l': 1}
            ],
            'medium': [
                {'title': 'Пароль должен содержать минимум 8 символов.',
                 'len': 8},
                {'title': 'Пароль должен содержать хотя бы одну заглавную букву.',
                 'l': 1},
                {'title': 'Пароль должен содержать хотя бы одну цифру.',
                 'l': 1},
                {'title': 'Пароль должен содержать хотя бы один специальный символ.',
                 'l': 1}
            ],
            'hard': [
                {'title': 'Пароль должен содержать минимум 12 символов.',
                 'len': 12},
                {'title': 'Пароль должен содержать хотя бы две заглавные буквы.',
                 'l': 2},
                {'title': 'Пароль должен содержать хотя бы три цифры.',
                 'l': 3},
                {'title': 'Пароль должен содержать хотя бы два специальных символа.',
                 'l': 2},
                {'title': 'Пароль не должен содержать последовательных одинаковых символов.'},
                {'title_warning': 'Вы ввели год. Возможно, это ваша дата рождения или иная памятная дата. Не рекомендуется.'},
                {'title_warning': 'Пароль содержит слово из словаря. Не рекомендуется.'}
            ]
        }
    },
    'eng': {
        'language_select_title': 'Выбор языка/Lang selection',
        'language_select_label': 'Выберите язык | Select a Language',
        'button_rus': 'RUS',
        'button_us': 'ENG',
        'app_title': 'Project K',
        'password_types': ['Simple', 'Medium', 'Hard'],
        'ok': 'OK',
        'not_ok': 'Not OK',
        'rul': 'Password Security Rules:',
        'result': 'Result of checking:',
        'entry_pass':{
            'введите': 'Enter password',
            'kol-vo': 'Characters:'
        },
        'rules': {
            'simple': [
                {'title': 'The password must contain at least 6 characters.',
                 'len': 6}
            ],
            'medium': [
                {'title': 'The password must contain at least 8 characters.',
                 'len': 8}
            ],
            'hard': [
                {'title': 'The password must contain at least 12 characters.',
                 'len': 12},
                {'title': 'The password must contain at least 2 uppercase letters.',
                 'l': 2},
                {'title': 'The password must contain at least 3 digits.',
                 'l': 3},
                {'title': 'The password must contain at least 2 special characters.',
                 'l': 2},
                {'title': 'The password should not contain consecutive identical characters.'},
                {'title_warning': "You have entered a year. Maybe it's your date of birth or some other notable date. Not recommended."},
                {'title_warning': 'The password contains a dictionary word. Not recommended.'}
            ]
        }
    }
}

def show_language_selection():
    def select_language(language):
        global _SEL_LANG
        _SEL_LANG = language
        root.destroy()

    root = tk.Tk()
    root.withdraw()
    root.title(messages['rus']['language_select_title'])
    root.geometry("300x120+500+300")
    root.resizable(False, False)

    label = tk.Label(root, text=messages['rus']['language_select_label'])
    label.pack(pady=(20, 10))

    btn_frame = tk.Frame(root)
    btn_frame.pack()

    btn_rus = tk.Button(btn_frame, text=messages['rus']['button_rus'],
                        command=lambda: select_language('rus'), width=8)
    btn_rus.pack(side='left', padx=10)

    btn_us = tk.Button(btn_frame, text=messages['rus']['button_us'],
                       command=lambda: select_language('eng'), width=8)
    btn_us.pack(side='left', padx=10)

    root.deiconify()
    root.mainloop()

def show_main_window():
    def check_password():
        global _RESULT
        _RESULT = True
        password = entry.get().strip()
        password_type = var.get()

        rules = messages[_SEL_LANG]['rules'][password_type]

        instructions_text.config(state='normal')
        instructions_text.delete(1.0, tk.END)

        if len(password) >= rules[0]['len']:
            instructions_text.insert(tk.END, f"{rules[0]['title']}\n\n", 'green')
        else:
            instructions_text.insert(tk.END, f"{rules[0]['title']}\n\n", 'red')
            _RESULT = False

        upper_count = 0
        digit_count = 0
        alnum_count = 0
        for char in password:
            if char.isupper():
                upper_count += 1
            if char.isdigit():
                digit_count += 1
            if not char.isalnum():
                alnum_count += 1

        reg = re.compile(r'^[^а-яА-Я]*$')
        if (" " in password) or not (reg.match(password)):
            if _SEL_LANG == "rus":
                instructions_text.insert(tk.END, 'В пароле есть пробел или русские символы. Исправьте.', 'red')
            else:
                instructions_text.insert(tk.END, 'The password contains a space or Russian characters - correct it.', 'red')
            _RESULT = False
        elif password_type == 'hard':
            if upper_count >= rules[1]['l']:
                instructions_text.insert(tk.END, f"{rules[1]['title']}\n\n", 'green')
            else:
                instructions_text.insert(tk.END, f"{rules[1]['title']}\n\n", 'red')
                _RESULT = False
            if digit_count >= rules[2]['l']:
                instructions_text.insert(tk.END, f"{rules[2]['title']}\n\n", 'green')
            else:
                instructions_text.insert(tk.END, f"{rules[2]['title']}\n\n", 'red')
                _RESULT = False
            if  alnum_count >= rules[3]['l']:
                instructions_text.insert(tk.END, f"{rules[3]['title']}\n\n", 'green')
            else:
                instructions_text.insert(tk.END, f"{rules[3]['title']}\n\n", 'red')
                _RESULT = False
            duplicate = False
            for i in range(len(password) - 1):
                if password[i] == password[i + 1]:
                    duplicate = True
                    instructions_text.insert(tk.END, f"{rules[4]['title']}\n\n", 'red')
                    _RESULT = False
                    break
            if duplicate == False:
                instructions_text.insert(tk.END, f"{rules[4]['title']}\n\n", 'green')
            pattern = r'(?<![\d])\d{4}(?![\d])'
            matches = re.findall(pattern, password)
            for year in matches:
                if 1930 < int(year) < 2026:
                    instructions_text.insert(tk.END, f"{rules[5]['title_warning']}\n\n", 'DarkOrchid')
                    break
            find_res = main_find.filter(password)
            if find_res == 'нету совпадений':
                pass
            else:
                found = '[{0} found]'.format(find_res)
                instructions_text.insert(tk.END, f"{rules[6]['title_warning']}{found}\n", 'DarkOrchid')
        instructions_text.config(state='disabled')

        if _RESULT:
            status_label.config(text=messages[_SEL_LANG]['ok'], fg='green')
        else:
            status_label.config(text=messages[_SEL_LANG]['not_ok'], fg='red')

    def display_rules():
        password_type = var.get()
        rules = messages[_SEL_LANG]['rules'][password_type]
        instructions_text.config(state='normal')
        instructions_text.delete(1.0, tk.END)

        for rule in rules:
            if 'title' in rule:
                instructions_text.insert(tk.END, f"{rule['title']}\n\n")
        instructions_text.config(state='disabled')

    root = tk.Tk()
    root.title(messages[_SEL_LANG]['app_title'])
    root.geometry("800x600+200+50")

    def close_app():
        sys.exit()

    root.protocol("WM_DELETE_WINDOW", close_app)

    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    var = tk.StringVar(value='hard')

    entry_label = tk.Label(main_frame, text=messages[_SEL_LANG]['entry_pass']['введите'])
    entry_label.grid(row=3, column=0, sticky='w', pady=(20, 0))

    def update_char_count(*args):
        password = entry.get().strip()
        char_count.set(f"{messages[_SEL_LANG]['entry_pass']['kol-vo']} {len(password)}")

    char_count = tk.StringVar()
    char_count.set(f"{messages[_SEL_LANG]['entry_pass']['kol-vo']} 0")

    entry_var = tk.StringVar()
    entry_var.trace_add("write", update_char_count)

    char_count_label = tk.Label(main_frame, textvariable=char_count)
    char_count_label.grid(row=5, column=0, sticky='w')

    entry = tk.Entry(main_frame, width=30, textvariable=entry_var)
    entry.grid(row=4, column=0, sticky='w')

    check_button = tk.Button(main_frame, text=("Проверить" if _SEL_LANG=="rus" else "Check"), command=check_password)
    check_button.grid(row=6, column=0, sticky='w', pady=(20, 0))

    instructions_and_output_windows = tk.Label(main_frame, text=messages[_SEL_LANG]['rul'])
    instructions_and_output_windows.grid(row=0, column=1, padx=(40, 0), pady=(0, 15))

    instructions_text = tk.Text(main_frame, height=15, width=45, wrap='word', state='disabled')
    instructions_text.grid(row=1, column=1, rowspan=10, sticky='nw', padx=(40, 0))

    instructions_text.tag_configure('green', foreground='green')
    instructions_text.tag_configure('red', foreground='red')
    instructions_text.tag_configure('DarkOrchid', foreground='DarkOrchid')

    status_label = tk.Label(main_frame, text='', font=('Arial', 14))
    status_label.grid(row=9, column=0, sticky='w', pady=(20, 0))

    display_rules()

    root.mainloop()

if __name__ == "__main__":
    show_language_selection()
    if _SEL_LANG is not None:
        show_main_window()
