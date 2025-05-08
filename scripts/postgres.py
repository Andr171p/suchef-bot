import psycopg2
import csv
from datetime import datetime

# Параметры подключения к БД
DB_URL = "postgresql://postgres:JptCaFYYYYYVtDzKizxrazzIoGVXvnwr@junction.proxy.rlwy.net:41552/railway"

# DB_URL = "postgresql://postgres:fvvlCWgHkDHxxUsJmcaFCHfwOkMkVcId@junction.proxy.rlwy.net:54868/railway"

# Имя выходного CSV файла
CSV_FILE = "suchef_dialogs.csv"


def export_users_to_csv():
    try:
        # Подключаемся к базе данных
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()

        # Получаем данные из таблицы users
        cursor.execute("SELECT user_message, bot_message, created_at, user_id, id FROM dialogs")
        # cursor.execute("SELECT id, user_id, username, phone FROM users")
        users = cursor.fetchall()

        # Получаем названия столбцов
        column_names = [desc[0] for desc in cursor.description]

        # Записываем данные в CSV файл
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Записываем заголовки
            writer.writerow(column_names)

            # Записываем данные
            for user in users:
                writer.writerow(user)

        print(f"Данные успешно экспортированы в файл: {CSV_FILE}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем соединение
        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    export_users_to_csv()