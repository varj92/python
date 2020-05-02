import psycopg2
import datetime

archivo = open("100.txt","r")
#icefas=open("icefas.txt","w")
for reg in archivo.readlines():
    fecha=reg[131:141]

    if '-' in fecha:
        fecha=fecha.replace("-","")
    else:
        fecha=fecha.replace("/","")
    #print(fecha)
    año=fecha[:4]
    mes=fecha[4:6]
    #dia=fecha[6:]
    #print(año+mes+dia)
    
    isValidDate = True
    try:
        date_obj = datetime.datetime.strptime(fecha, '%Y%m%d')

    except ValueError :
        isValidDate = False

    if not isValidDate:
        fecha=año+mes+"01"
        #print(fecha)

    insert_ag = ("insert into tabla_1 (id,nss,rfc,nci,apellidopat,apellidomat,nombre,fechanacimiento) VALUES('"+reg[264:267]+"','"+reg[143:153]+"','"+reg[154:167]+"','"+reg[168:198]+"','"+reg[:40]+"','"+reg[40:80]+"','"+reg[80:130]+"','"+fecha+"')")
    insert_sa = ("insert into tabla_2 (id,nss,rfc,nci,apellidopat,apellidomat,nombre,fechanacimiento) VALUES('"+reg[264:267]+"','"+reg[143:153]+"','"+reg[154:167]+"','"+reg[168:198]+"','"+reg[:40]+"','"+reg[40:80]+"','"+reg[80:130]+"','"+fecha+"')")        

    conexion_ag = psycopg2.connect(database="basededatos1", user="usuario1", password="12345678", host= "10.0.0.1", port= 5432)
    cursor=conexion_ag.cursor()
    cursor.execute(insert_ag)
    conexion_ag.commit()
    conexion_ag.close()

    conexion_sa = psycopg2.connect(database="basededatos2", user="usuario2", password="12345678", host= "10.0.0.2", port= 5432)
    cursor=conexion_sa.cursor()
    cursor.execute(insert_sa)
    conexion_sa.commit()
    conexion_sa.close()