class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login, password):
        is_found = False
        for item in self.users:
            if login == item.nickname and item.password == hash(password):
                self.current_user = item
                print(f'Добро пожаловать, {item.nickname}')
                is_found = True
        if not is_found:
            print('Такого пользователя не существует ')


    def register(self, nickname, password, age):
        is_found = False
        a = User(nickname, password, age)
        for item in self.users:
            if nickname != item.nickname:
                self.users.append(a)
                print(f'Добро пожаловать, {nickname}')
                is_found = True
        if not is_found:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта ')



user1 = User('яша', 1234, 19)
user2 = User('лиза', 5678, 12)
user3 = User('лена', 8910, 48)

us = [user1, user2, user3]

v1 = Video('123', 30, 0)
v2 = Video('234', 45, 0)
v3 = Video('345', 55, 0)

vi = [v1, v2, v3]

ur = UrTube(us, vi, user2)

ur.log_in('света', 8910)

ur.register('яша', 1234, 19)

ur.log_out()