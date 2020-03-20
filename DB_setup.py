from connection import psycopg_connect
from connection import close

cur, con=psycopg_connect()
cur.execute("DROP TABLE IF EXISTS fav_category")
cur.execute("""create table fav_category(
            profid varchar unique,
            category varchar,
            targetaudience varchar
            )""")



con.commit()
cur.close()
con.close()
