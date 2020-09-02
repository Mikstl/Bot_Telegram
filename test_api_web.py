# import sqlite3
 
# conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
# cursor = conn.cursor()
 
# # Создание таблицы
# cursor.execute("""CREATE TABLE albums
#                   (name_id INTEGER PRIMARY KEY,id_human INTEGER, kurs REAL)
#                """)


import sqlite3
 
conn = sqlite3.connect("mydatabase.db") 
cursor = conn.cursor()
zalupa = [("5345345","0.03")]
# Вставляем данные в таблицу
cursor.executemany('INSERT INTO albums(id_human, kurs) VALUES (?,?)',zalupa)
# Сохраняем изменения
conn.commit()