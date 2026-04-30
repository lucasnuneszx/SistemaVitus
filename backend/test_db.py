import psycopg2
try:
    conn = psycopg2.connect(host='IP_REMOVIDO', port='5432', user='fortis', password='SENHA_REMOVIDA', dbname='postgres')
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('CREATE DATABASE "sistemaxi-prod";')
    print('Database created successfully')
except Exception as e:
    print('Error:', e)
