import sqlite3


class Database():

    # Подключение к БД
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    # Создание таблицы
    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY,"
                     "user_name TEXT,"
                     "user_phone TEXT,"
                     "telegram_id TEXT);"
                     "CREATE TABLE IF NOT EXISTS place("
                     "id INTEGER PRIMARY KEY,"
                     "name_place TEXT,"
                     "place_address TEXT);"
                     "CREATE TABLE IF NOT EXISTS games("
                     "id INTEGER PRIMARY KEY,"
                     "place_id TEXT,"
                     "date_game TEXT,"
                     "time_game TEXT,"
                     "min_player INTEGER,"
                     "max_player INTEGER,"
                     "price TEXT)")
            self.cursor.executescript(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print("Ошибка при создании: ", Error)

    # Добавление пользователя в БД
    def add_user(self, user_name, user_phone, telegram_id):
        self.cursor.execute(
            f"INSERT INTO users (user_name, user_phone, telegram_id) VALUES (?, ?, ?)", (user_name, user_phone, telegram_id))
        self.connection.commit()

    def add_game(self, place_id, date_game, time_game, min_player, max_player, price):
        self.cursor.execute(f'INSERT INTO games(place_id, date_game, time_game, min_player, max_player, price) VALUES (?,?,?,?,?,?)',
                            (place_id, date_game, time_game, min_player, max_player, price))
        self.connection.commit()

    # Извлечение пользовател из БД по его telegram_id
    def select_user_id(self, telegram_id):
        users = self.cursor.execute(
            "SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()

    def db_select_column(self, table_name, column, item):
        result = self.cursor.execute(
            "SELECT * FROM {} WHERE {} = {}".format(table_name, column, item))
        return result

    def db_select_all(self, table_name):
        result = self.cursor.execute("SELECT * FROM {}".format(table_name))
        return result.fetchall()

    # Закрытие соединения
    def __del__(self):
        self.cursor.close()
        self.connection.close()
