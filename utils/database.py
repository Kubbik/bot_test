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
                     "id INTEGER PRYMARY KEY,"
                     "user_name TEXT,"
                     "user_phone TEXT,"
                     "telegram_id TEXT);")
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print("Ошибка при создании: ", Error)

    # Добавление пользователя в БД
    def add_user(self, user_name, user_phone, telegram_id):
        self.cursor.execute(
            f"INSERT INTO users (user_name, user_phone, telegram_id) VALUES (?, ?, ?)", (user_name, user_phone, telegram_id))
        self.connection.commit()

    # Извлечение пользовател из БД по его telegram_id
    def select_user_id(self, telegram_id):
        users = self.cursor.execute(
            "SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()

    # Закрытие соединения
    def __del__(self):
        self.cursor.close()
        self.connection.close()
