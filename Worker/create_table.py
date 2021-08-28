import psycopg2
import config

def create_table_parsed_pages():
    conn = psycopg2.connect(host = config.host, port=config.port, database = config.database, user = config.user, password = config.password)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS public.parsed_pages ( id SERIAL UNIQUE, link VARCHAR(255), title TEXT, txt TEXT, img_link TEXT, posted_at TIMESTAMP, parsed_at TIMESTAMP );")
    conn.commit()
    print("Table created")

    cur.close()
    conn.close()