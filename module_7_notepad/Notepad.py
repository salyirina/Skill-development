from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os


def load_icon(path, size=(24, 24)):
    """Загрузка иконки с помощью Pillow."""
    try:
        img = Image.open(path).resize(size, Image.Resampling.LANCZOS)  # Используем LANCZOS для resize
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке иконки '{path}': {e}")
        return None


def change_theme(theme):
    """Изменение цветовой темы текста."""
    if theme in view_colors:
        text_field['bg'] = view_colors[theme]['text_bg']
        text_field['fg'] = view_colors[theme]['text_fg']
        text_field['insertbackground'] = view_colors[theme]['cursor']
        text_field['selectbackground'] = view_colors[theme]['select_bg']
    else:
        messagebox.showerror("Ошибка", f"Тема '{theme}' не найдена.")


def change_font(font_name):
    """Изменение шрифта текста."""
    if font_name in fonts:
        text_field.config(font=fonts[font_name]['font'])
    else:
        messagebox.showerror("Ошибка", f"Шрифт '{font_name}' не найден.")


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


def save_as_file():
    """Сохранить как."""
    save_file()


def download_file():
    """Скачать содержимое текстового поля."""
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
            messagebox.showinfo("Скачано", f"Файл успешно скачан:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось скачать файл:\n{e}")


def delete_file():
    """Очистить содержимое текстового поля."""
    if messagebox.askyesno("Удалить содержимое", "Вы уверены, что хотите удалить всё содержимое?"):
        text_field.delete("1.0", END)


def about_program():
    """Отображение информации о программе."""
    messagebox.showinfo("О программе", "Блокнот для редактирования текстовых файлов.\nВерсия 1.0.")


def about_us():
    """Отображение информации 'О нас'."""
    messagebox.showinfo("О нас", "Ирина из команды разработчиков, которая создала этот блокнот.")


def notepad_exit():
    """Закрыть приложение."""
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        root.destroy()


# Создаем главное окно
root = Tk()
root.title("Блокнот")
root.geometry("800x600")

# Цветовые темы
view_colors = {
    'dark': {'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'white', 'select_bg': '#555555'},
    'light': {'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black', 'select_bg': '#CCCCCC'}
}

# Шрифты
fonts = {
    'Arial': {'font': ('Arial', 14)},
    'ComicSans': {'font': ('Comic Sans MS', 14)},
    'TNR': {'font': ('Times New Roman', 14)}
}

# Создаем текстовый фрейм и поле
f_text = Frame(root)
f_text.pack(expand=1, fill=BOTH)

text_field = Text(f_text, bg='white', fg='black', padx=10, pady=10, wrap=WORD,
                  insertbackground='black', selectbackground='#CCCCCC', spacing3=10,
                  width=30, font='Arial 14')
text_field.pack(expand=1, fill=BOTH, side=LEFT)

# Скроллбар
scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=RIGHT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

# Загрузка иконок для кнопок
icon_open = load_icon("icons/open.ico")  # Иконка для кнопки "Открыть"
icon_save = load_icon("icons/save.ico")  # Иконка для кнопки "Сохранить"
icon_save_as = load_icon("icons/save_as.ico")  # Иконка для кнопки "Сохранить как"
icon_download = load_icon("icons/download.ico")  # Иконка для кнопки "Скачать"
icon_delete = load_icon("icons/delete.ico")  # Иконка для кнопки "Удалить"

# Определяем текущую директорию скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Устанавливаем путь к иконке
icon_path = os.path.join(script_dir, "icons")

# Проверяем существование файла
if not os.path.exists(icon_path):
    print(f"Иконка не найдена по пути: {icon_path}")
else:
    print(f"Иконка найдена: {icon_path}")

# Устанавливаем иконку
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Ошибка при установке иконки через iconbitmap: {e}")
    # Альтернативный способ через PhotoImage
    icon_image = PhotoImage(file=icon_path)
    root.iconphoto(True, icon_image)

# Главное меню
main_menu = Menu(root)

# Меню "Файл"
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть", image=icon_open, compound=LEFT, command=open_file)
file_menu.add_command(label="Сохранить", image=icon_save, compound=LEFT, command=save_file)
file_menu.add_command(label="Сохранить как", image=icon_save_as, compound=LEFT, command=save_as_file)
file_menu.add_command(label="Скачать", image=icon_download, compound=LEFT, command=download_file)
file_menu.add_command(label="Удалить", image=icon_delete, compound=LEFT, command=delete_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", compound=LEFT, command=notepad_exit)

main_menu.add_cascade(label="Файл", menu=file_menu)

# Меню "Вид"
view_menu = Menu(main_menu, tearoff=0)
theme_menu = Menu(view_menu, tearoff=0)
theme_menu.add_command(label="Тёмная", command=lambda: change_theme('dark'))
theme_menu.add_command(label="Светлая", command=lambda: change_theme('light'))
view_menu.add_cascade(label="Тема", menu=theme_menu)

font_menu = Menu(view_menu, tearoff=0)
for font_name in fonts.keys():
    font_menu.add_command(label=font_name, command=lambda f=font_name: change_font(f))
view_menu.add_cascade(label="Шрифт", menu=font_menu)

main_menu.add_cascade(label="Вид", menu=view_menu)

# Меню "Справка"
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="О программе", command=about_program)
help_menu.add_command(label="О нас", command=about_us)

main_menu.add_cascade(label="Справка", menu=help_menu)

# Применение главного меню
root.config(menu=main_menu)

# Запуск основного цикла программы
root.mainloop()