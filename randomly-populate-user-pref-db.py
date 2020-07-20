import sqlite3
import random

def insertVaribleIntoTable(age, spirituality, location, engagement, user_id):
    try:
        sqliteConnection = sqlite3.connect('Intellivo-app/intellivo_package/intellivoUser.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO user_pref (age, spirituality, location, engagement, user_id)
VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (age, spirituality, location, engagement, user_id)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

# adjust the range based on the current ids already in the db
# adn how many user prefs you want to generate
for i in range(8, 60):
    age = random.randrange(4)+1
    spirituality = random.randrange(5)+1
    location = random.randrange(15)+1
    engagement = random.randrange(5)+1
    insertVaribleIntoTable(age, spirituality, location, engagement, i)
