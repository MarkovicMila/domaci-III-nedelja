import psycopg2 as psycopg2


def upis_txt():
    con=psycopg2.connect(
        database='magacin',
        port='5432',
        host='localhost',
        user='postgres',
        password='itoip'
    )
    cursor=con.cursor()
    cursor.execute('SELECT * FROM proizvod')
    result=cursor.fetchall()
    cursor.close()
    con.close()
    return(result)

pom=upis_txt()
print(pom)
f=open('magacin.txt','a')

for i in pom:
    print('ID : ',i[0],file=f)
    print('Naziv: {}'.format(i[1]),file=f)
    print('Cena : {}'.format(i[2]),file=f)
    print('kolicina: {}'.format(i[3]),file=f)
    if i[4]!='':
        print('Opis: {}'.format(i[4]),file=f)
    print('-'*50,file=f)
f.close()