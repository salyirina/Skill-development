from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os


def change_theme(theme):
    """Изменение цветовой темы текста."""
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']


def change_fonts(font):
    """Изменение шрифта текста."""
    text_field['font'] = fonts[font]['font']


# Функции
def open_file():
    """Открыть файл и загрузить содержимое в текстовое поле."""
    file_path = filedialog.askopenfilename(
        title="Открыть файл",
        filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*"))
    )
    if file_path:
        try:
            with open(file_path, encoding="utf-8") as f:
                text_field.delete("1.0", END)
                text_field.insert("1.0", f.read())
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")


def save_file():
    """Сохранить текущее содержимое в выбранный файл."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        title="Сохранить файл",
        filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*"))
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                text = text_field.get("1.0", END).strip()
                f.write(text)
            messagebox.showinfo("Сохранено", f"Файл успешно сохранён:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")


def save_as():
    """Сохранить как (альтернативная функция для создания нового файла)."""
    save_file()


def download_file():
    """Скачать содержимое текстового поля как файл в указанную папку."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        title="Скачать файл",
        filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*"))
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                text = text_field.get("1.0", END).strip()
                f.write(text)
            messagebox.showinfo("Успех", f"Файл успешно скачан:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось скачать файл:\n{e}")


def delete_file():
    """Удалить содержимое текстового поля."""
    if messagebox.askyesno("Удалить файл", "Вы уверены, что хотите удалить содержимое?"):
        text_field.delete("1.0", END)


def notepad_exit():
    """Закрыть приложение."""
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()


def show_info():
    """Отображение информации о приложении."""
    messagebox.showinfo("Информация", "Блокнот v1.0\nРазработано с использованием tkinter.")


def about_program():
    """Отображение информации о программе."""
    messagebox.showinfo("О программе", "Блокнот для работы с текстами.\nАвтор: Ирина.")


# Создаем главное окно
root = Tk()
root.title('Блокнот')
root.geometry('600x700')

# Меню "Файл"
main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Сохранить как", command=save_as)
file_menu.add_command(label="Скачать", command=download_file)
file_menu.add_command(label="Удалить файл", command=delete_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=notepad_exit)

main_menu.add_cascade(label="Файл", menu=file_menu)

# Загрузка иконок
icon_dir = "путь_к_каталогу_с_иконками"  # Убедитесь, что путь указан верно
try:
    icon_open = PhotoImage(file=os.path.join(icon_dir, "open.png"))
    icon_save = PhotoImage(file=os.path.join(icon_dir, "save.png"))
    icon_save_as = PhotoImage(file=os.path.join(icon_dir, "save_as.png"))
    icon_download = PhotoImage(file=os.path.join(icon_dir, "download.png"))
    icon_delete = PhotoImage(file=os.path.join(icon_dir, "delete.png"))
except TclError:
    icon_open = None  # Если иконка не найдена, используем None или альтернативу

# Меню "Вид"
view_menu = Menu(main_menu, tearoff=0)
theme_menu = Menu(view_menu, tearoff=0)
font_menu = Menu(view_menu, tearoff=0)

theme_menu.add_command(label='Тёмная', command=lambda: change_theme('dark'))
theme_menu.add_command(label='Светлая', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Тема', menu=theme_menu)

font_menu.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu.add_command(label='Comic Sans MS', command=lambda: change_fonts('ComicSans'))
font_menu.add_command(label='Times New Roman', command=lambda: change_fonts('TNR'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu)

main_menu.add_cascade(label='Вид', menu=view_menu)

# Добавление меню в главное окно
root.config(menu=main_menu)

# Основной фрейм для текста
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# Цветовые темы
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

# Шрифты
fonts = {
    'Arial': {'font': 'Arial 14 bold'},
    'ComicSans': {'font': ('Comic Sans MS', 14, 'bold')},
    'TNR': {'font': ('Times New Roman', 14, 'bold')}
}

# Текстовое поле
text_field = Text(f_text, bg='black', fg='lime', padx=10, pady=10, wrap=WORD,
                  insertbackground='brown', selectbackground='#8D917A', spacing3=10,
                  width=30, font='Arial 14 bold')
text_field.pack(expand=1, fill=BOTH, side=LEFT)

# Скроллбар
scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=RIGHT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

# Запуск основного цикла программы
root.mainloop()
