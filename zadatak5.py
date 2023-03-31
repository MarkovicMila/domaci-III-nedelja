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

    com='''DROP TABLE proizvod'''
    cursor.execute(com)
    print('Table deleted successfully')
    con.commit()

except(Exception,psycopg2.Error) as e:
    print('Error: ',e)

finally:
    con.close()
    cursor.close()

