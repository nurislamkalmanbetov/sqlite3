# Nurislam 01/03/2023

import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name) 
        self.cursor = self.conn.cursor() # создаем объект курсора

    def create_users_table(self): # создаем таблицу пользователи
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (id INTEGER PRIMARY KEY,
                                name TEXT,
                                email TEXT)''') # Курсор - это объект, который позволяет выполнить SQL-запрос

    def create_orders_table(self): # таблица заказы
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                               (id INTEGER PRIMARY KEY,
                                user_id INTEGER,
                                product TEXT,
                                FOREIGN KEY(user_id) REFERENCES users(id))''')

    def add_user(self, name, email): # добавление через cursor.execute
        self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        return self.cursor.lastrowid # содержит идентификатор последней вставленной строки в базу данных SQLite3

    def add_order(self, user_id, product):
        self.cursor.execute("INSERT INTO orders (user_id, product) VALUES (?, ?)", (user_id, product))

    def delete_user(self, user_id):
        self.cursor.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
        self.conn.commit()

    def delete_order(self, order_id):
        self.cursor.execute('''DELETE FROM orders WHERE id = ?''', (order_id,))
        self.conn.commit()

    def commit(self):
        self.conn.commit() # сохраняем

    def close(self):
        self.conn.close() # и закрываем


if __name__ == '__main__':
    db = Database('shop2.db')
    db.create_users_table()
    db.create_orders_table()

    nuris_id = db.add_user('Nuris Kalm', 'nuris@example.com')
    aidos_id = db.add_user('Aidos', 'aidos@exmapl.com')
    alex_id = db.add_user('Alex', 'alex@example.com')
    bek_id = db.add_user('Bek', 'bek@example.com')

    db.add_order(nuris_id, 'Widget')
    db.add_order(aidos_id, 'Gadget')
    db.add_order(alex_id, 'Phone')
    db.add_order(bek_id, 'Apple Watch')

    db.delete_user(alex_id)
    db.delete_order(aidos_id)

    db.commit()
    db.close()
