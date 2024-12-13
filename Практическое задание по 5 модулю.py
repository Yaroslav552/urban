import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # Имя пользователя
        self.password = hash(password)  # Хеш пароль
        self.age = age  # Возраст

    def __str__(self):  # Необходимо для отображения в консоли
        return f"{self.nickname} ({self.age})"

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        adult = "Да" \
            if self.adult_mode \
            else "Нет"
        return f"Видео: {self.title}, Длительность: {self.duration}, 18+: {adult}"


class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        if users is None:
            users = []
        if videos is None:
            videos = []
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def add(self, *videos):
        for video in videos:
            duplicate = False
            for i in self.videos:
                if i.title == video.title:
                    duplicate = True
                    break
            if duplicate:
                print(f'Видео с названием {video.title} уже существует')
            else:
                self.videos.append(video)
                print(f'Видео {video.title} добавлено')

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Вход выполнен: {nickname}')
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Регистрация {nickname} прошла успешно')

    def log_out(self):
        self.current_user = None
        print(f'Выход выполнен')

    def get_videos(self, search_term):
        search_term = search_term.lower()
        result = []
        for video in self.videos:
            if search_term in video.title.lower():
                result.append(video.title)
        if not result:
            print(f'Видео по запросу "{search_term}" не найдено.')
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        video = None
        for i in self.videos:
            if i.title == title:
                video = i
                break
        if video is None:
            print("Видео не найдено.")
            return
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for second in range(video.duration):
            video.time_now = second + 1
            print(f"Секунда {video.time_now} из {video.duration}")
            time.sleep(1)

        print("Конец видео")

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
