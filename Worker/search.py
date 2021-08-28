from datetime import datetime, timedelta
import psycopg2
import config

def search_link(link):
    conn = psycopg2.connect(host = config.host, port=config.port, database = config.database, user = config.user, password = config.password)
    cur = conn.cursor()
    
    cur.execute("SELECT link FROM parsed_pages WHERE link in (%s);", (link,))
    conn.commit()

    short_link = cur.fetchone()

    cur.close()

    conn.close()

    if (short_link == [] or short_link is None):
        return False
    else:
        return True

def search_pages_by_day(day):
    conn = psycopg2.connect(host = config.host, port=config.port, database = config.database, user = config.user, password = config.password)
    conn.set_client_encoding('UNICODE')
    cur = conn.cursor()

    date = datetime.date(datetime.today()) - timedelta(days=day)

    cur.execute("SELECT link, title, txt, img_link, posted_at, parsed_at FROM parsed_pages WHERE posted_at >= %s;", (date.strftime("%Y-%m-%d %H:%M:%S"),))
    conn.commit()

    full_link = cur.fetchall()

    cur.close()

    conn.close()

    if (full_link == [] or full_link is None):
        return False
    else:
        return full_link