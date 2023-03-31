import psycopg2 as psycopg2

try:
    con=psycopg2.connect(
        database='magacin',
        host='localhost',
        user='postgres',
        port='5432',
        password='itoip'
    )
    cursor=con.cursor()

    com='''CREATE TABLE proizvod(
    ID_proizvod SERIAL PRIMARY KEY,
    naziv_proizvoda VARCHAR(30) NOT NULL,
    cena FLOAT NOT NULL,
    kolicina INTEGER NOT NULL,
    opis TEXT)
    '''
    cursor.execute(com)
    print('Table created successfully')
    con.commit()

except(Exception,psycopg2.Error) as e:
    print('Error: ',e)

finally:
    con.close()
    cursor.close()

