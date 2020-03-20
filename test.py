from connection import psycopg_connect
from connection import close

cur, con=psycopg_connect()

def test():
    cur.execute("""select l.profid, l.prodid, pr.segment, r.name, r.category, r.subcategory, r.subsubcategory, r.targetaudience
        from profiles_previously_viewed as L inner join profiles as Pr on l.profid = pr.id
        inner join products as r on l.prodid = r.id
        where segment = 'buyer' or segment = 'BUYER'
        order by profid desc,
        prodid desc
        limit 100
        """)

    list = []
    table = cur.fetchall()
    for row in table:
            subsubcategory = row[7]
            list.append(subsubcategory)
    print(list)
#test()

def recommend():
    'Gives the recommendation'
    cur.execute("select * from fav_category")
    table = cur.fetchall()
    # profid = input("Voor profid in:")
    profid= "5c472504dbed8900019d65f0"
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
recommend()


close()
