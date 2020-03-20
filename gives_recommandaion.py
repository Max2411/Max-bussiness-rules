from connection import psycopg_connect


cur, con=psycopg_connect()

def recommend(profid):
    'Gives the recommendation'
    cur.execute("select * from fav_category")
    table = cur.fetchall()
    # profid = input("Voor profid in:")
    for row in table:
        if profid== row[0]:
            category= row[1]
            targetaudience = row[2]

    cur.execute("select id, category, targetaudience from products")
    prodtable = cur.fetchall()
    for row in prodtable:
        if category==row[1] and (targetaudience==row[2] or targetaudience== None):
            prodid = row[0]

    print("item {} is recommended for profile {}".format(prodid, profid))
    return profid, prodid
recommend("5c477cdc00ead60001294308")


con.commit()
cur.close()
con.close()
