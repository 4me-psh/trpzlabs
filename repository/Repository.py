import psycopg2


class Repository:


    def exec(self, dbname, user, password, host, port, query):
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

    def fetch(self, dbname, user, password, host, port):
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute('SELECT * from histories')
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        print(result)
