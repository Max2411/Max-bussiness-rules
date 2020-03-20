import psycopg2

def psycopg_connect():
    'Make connection with the database.'
    con = psycopg2.connect("dbname=voordeelshop user=postgres password=groep5")
    cur = con.cursor()
    return cur, con


