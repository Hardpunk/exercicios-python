import psycopg2
import psycopg2.extras

con = psycopg2.connect(host='localhost', database='brasil',
                       user='postgres', password='root')
cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
# cur.execute('insert into estado values (28, 1, \'PS\', \'Paraná do Norte\')')
# con.commit()
cur.execute("""select (nom_estado, nom_cidade) from cidade, estado 
                where nom_cidade like '%Presidente%' and 
                cidade.cod_estado = estado.cod_estado""")
listaCidades = cur.fetchall()
for cidade in listaCidades:
    print(cidade)
