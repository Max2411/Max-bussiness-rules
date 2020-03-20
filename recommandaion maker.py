from connection import psycopg_connect
from connection import close

cur, con=psycopg_connect()

def overzetten():
    'First recommendation table based on previous purchases. Online works for custumers that have already bought something before'
    c = 0
    cur.execute("""select l.profid, l.prodid, pr.segment, r.name, r.category, r.subcategory, r.subsubcategory, r.targetaudience
    from profiles_previously_viewed as L inner join profiles as Pr on l.profid = pr.id
    inner join products as r on l.prodid = r.id
    where segment = 'buyer' or segment = 'BUYER'
    order by profid desc,
    prodid desc
    limit 100
    """)# I have placed a limit of 100 for test purposes.
    table = cur.fetchall()
    list=[] #for checking if an profid already hasbeen inserted.
    for row in table:
        try:
            profid = row[0]
            category = row[4]
            targetaudience = row[7]
            # subcategory = row[5]
            # subsubcategory = row[6]
            if profid not in list and targetaudience != None:
                cur.execute("insert into fav_category (profid, category, targetaudience ) values (%s,%s,%s)",(profid ,category, targetaudience))
            list.append(profid)

        except KeyError:
            continue

overzetten()
close()
