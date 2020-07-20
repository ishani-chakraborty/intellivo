import sqlite3
import random

def insertVariableIntoTable(age, spirituality, location, engagement, user_id):
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
start_idx = int(input('Start Index: '))
num_random = int(input('How many randomly generated users do you want? '))
for i in range(start_idx, start_idx + num_random):
    age = random.randrange(4)+1
    spirituality = random.randrange(5)+1
    location = random.randrange(15)+1
    engagement = random.randrange(5)+1
    insertVariableIntoTable(age, spirituality, location, engagement, i)
