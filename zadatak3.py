import psycopg2 as psycopg2


def unos_proizvoda(naziv_proizvoda,cena,kolicina,opis=None):
    try:
        con=psycopg2.connect(
            database='magacin',
            user='postgres',
            password='itoip',
            host='localhost',
            port='5432'
        )
        cursor=con.cursor()
        com='''INSERT INTO proizvod (naziv_proizvoda,cena,kolicina,opis) VALUES ('{}','{}','{}','{}')'''.format(naziv_proizvoda,cena,kolicina,opis)
        cursor.execute(com)
        con.commit()
    except(Exception,psycopg2.Error) as e:
        print('Error: ',e)
    finally:
        cursor.close()
        con.close()

# def unos_opisa(opis):
#     try:
#         con=psycopg2.connect(
#             database='magacin',
#             user='postgres',
#             password='itoip',
#             host='localhost',
#             port='5432'
#         )
#         cursor=con.cursor()
#         com='''UPDATE proizvod 
#         SET opis='{}'
#         WHERE '''.format(opis)
#         cursor.execute(com)
#         print('Table updated successfully!')
#         con.commit()
#     except(Exception,psycopg2.Error) as e:
#         print('Error: ',e)
#     finally:
#         cursor.close()
#         con.close()
    

i=0
while i<5:
    naziv_proizvoda=input('Unesite naziv proizvoda: ')
    cena=float(input('Unesite cenu proizvoda: '))
    kolicina=eval(input('Unesite kolicinu robe: '))
    opis=input('Unesite opis(ako je potrebno): ')
    if cena<0 or kolicina<0 or len(naziv_proizvoda)<3:
        print('Los unos, neodgovarajuci podaci!')
        break
    i+=1
    unos_proizvoda(naziv_proizvoda,cena,kolicina,opis)
    # if opis is NOT NULL:
    #     unos_opisa(opis)
    