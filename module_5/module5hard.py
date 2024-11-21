# bcrypt Спроектирован специально для хеширования паролей и учитывает потребность в защите от атак.
# Использует случайные соли и адаптивное хеширование, что делает его устойчивым к атакам
# типа "brute-force" и "rainbow table".
# Позволяет настраивать сложность хеширования (количество "раундов"), что делает его более безопасным,
# особенно на современных компьютерах.
import bcrypt
import time

#Каждый объект класса User должен обладать следующими атрибутами и методами:
#Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число),
# age(возраст, число)

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        # Сохраняем хеш пароля
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.age = age

    def check_password(self, password):
    # Хешируем пароль с использованием bcrypt с автоматической генерацией соли
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

#Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
# time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # Название видео (заголовок, строка)
        self.duration = duration  # Продолжительность видео в секундах
        self.time_now = 0  # секунда остановки (изначально 0), указывает на текущую секунду воспроизведения
        self.adult_mode = adult_mode  # Флаг для видео с возрастными ограничениями

#Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
class UrTube:
    def __init__(self):
        self.users = [] #список объектов User
        self.videos = [] # список объектов Video
        self.current_user = None #текущий пользователь

#Метод log_in, который принимает на вход
# аргументы: nickname, password и пытается найти пользователяв users с такими же логином и паролем.
# Если такой пользователь существует,то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    def log_in(self, nickname, password):
        # Поиск пользователя по nickname
        for user in self.users:
            if user.nickname == nickname and user.check_password(password): #password передаётся в виде строки,
                                                                           # а сравнивается по хэшу
                self.current_user = user # текущий пользователь
                return
        print("Неверные имя пользователя или пароль!")

#Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
# если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
# "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.

    def register(self, nickname, password, age):

# any используется для проверки, содержат ли элементы итерируемого объекта
# хотя бы один элемент, который является истинным
# Проверка, существует ли пользователь с таким nickname
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user


#Метод log_out для сброса текущего пользователя на None.

    def log_out(self):
        self.current_user = None

#Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
# если с таким же названием видео ещё не существует. В противном случае ничего не происходит.

    def add(self, *videos):
        # Добавляем видео, если такого видео еще нет в списке
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

#Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
# содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке
# 'Urban the best' (не учитывать регистр).
    def get_videos(self, search_word):
        search_word = search_word.lower() #не учитывать регистр
        return [video.title for video in self.videos if search_word in video.title.lower()]

#Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # next позволяет получать элементы по одному, без необходимости вручную управлять индексами или циклами
        video = next((vid for vid in self.videos if vid.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(1, video.duration + 1):
            print(second, end=" ", flush=True)
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0


# Проверка кода
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
