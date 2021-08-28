import psycopg2
import config

def insert_pages(link, title, txt, img_link, posted_at, parsed_at):
    conn = psycopg2.connect(host = config.host, port=config.port, database = config.database, user = config.user, password = config.password)
    cur = conn.cursor()

    cur.execute("INSERT INTO parsed_pages (link, title, txt, img_link, posted_at, parsed_at) VALUES (%s, %s, %s, %s, %s, %s) ;", (link, title, txt, img_link, posted_at, parsed_at))
    conn.commit()

    cur.close()
    conn.close()