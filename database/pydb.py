import pymysql.cursors

connection = pymysql.Connection(
                                host = "localhost",
                                user = "root",
                                password = "",
                                database = "todo",
                                cursorclass = pymysql.cursors.DictCursor # Optional
                            )

with connection.cursor() as cursor:

    sql_command = """
                    SELECT users.name, todo.title, todo.body FROM todo
                    JOIN users
                    ON todo.uid = users.id
                """
    cursor.execute(sql_command)
    print(cursor.fetchall())


with connection.cursor() as cursor:

    sql_command = """
                    INSERT INTO todo (uid, title, body, date_added, completed) VALUES(2, "Dance in the Sunlight", "Me and my baby doing happy things in the moonlight.", "02-01-2020", 0)
                """
    cursor.execute(sql_command)
    connection.commit()