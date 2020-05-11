import psycopg2
import xlsxwriter
import datetime

print("Insertar Fecha: ")
fecha = input()
fecha = fecha[:6]

# today = datetime.date.today()

#conexion
conexion_ag = psycopg2.connect(database="dvdrental", user="postgres", password="postgres", host= "localhost", port= 5432)
cursor=conexion_ag.cursor()       
cursor.execute("select rental_date::DATE,count(*) from rental WHERE TO_CHAR(rental_date,'YYYYMM')='"+fecha+"' group by  1")
conexion_ag.commit()
conteos = cursor.fetchall()
conexion_ag.close()

workbook = xlsxwriter.Workbook('Reporte_Mensual.xlsx')
# cell_format = workbook.add_format({'bold': True, 'bg_color': '#008000', 'align': 'center'})
Header = workbook.add_format({'bold': True, 'bg_color': '#8FBC8F', 'align': 'center'})
format2 = workbook.add_format({'num_format': 'yyyy mmm dd','align': 'center'})
#Header_date = workbook.add_format({'bold': True, 'bg_color': '#8FBC8F', 'align': 'center','num_format': 'yyyy mmm dd'})
f_total = workbook.add_format({'bold': True, 'align': 'center'})
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Reporte',Header)
worksheet.write('B1', '',Header)
worksheet.write('A2', 'Día',Header)
worksheet.write('B2', 'Producción',Header)
row = 2
col = 0
tot = 0

center = workbook.add_format({'align': 'center'})
for date, cont in (conteos):
    tot += cont
    worksheet.write(row,col,date,format2)
    worksheet.write(row,col + 1,cont,center)
    row +=1

#Pintamos la fila de totales
worksheet.write(row, 0, 'Total:')
#worksheet.write_formula(row,1, '==SUMA(B3:B10)')
worksheet.write(row,1,tot,f_total)
#worksheet.write(row, 1, '=SUMA(B3:B5)')
workbook.close()
print("Finalizo el proceso.")