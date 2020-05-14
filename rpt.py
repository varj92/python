import psycopg2
import xlsxwriter
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
lastweek = yesterday - datetime.timedelta(days = 7)
lastyear = yesterday - datetime.timedelta(weeks= 52)
ytd = yesterday.strftime('%Y-%m-%d')
lstwk = lastweek.strftime('%Y-%m-%d')
lstyr = lastyear.strftime('%Y-%m-%d')
# print(yesterday.strftime("%A %Y-%m-%d"))
#d = date_time.strftime("%d %b %Y")

#conexion
#conteos año pasado
sql = ("select TRIM(hora),validos,novalidos from fn_conteos('"+lstyr+"')")
conexion_ag = psycopg2.connect(database="prueba", user="usuario", password="pruebas123", host= "localhost", port= 5432)
cursor=conexion_ag.cursor()
cursor.execute(sql)
conexion_ag.commit()
cont_lstyr = cursor.fetchall()
conexion_ag.close()

#conteos semana pasada
sql2 = ("select validos,novalidos from fn_conteos('"+lstwk+"')")
conexion_ag = psycopg2.connect(database="prueba", user="usuario", password="pruebas123", host= "localhost", port= 5432)
cursor=conexion_ag.cursor()
cursor.execute(sql2)
conexion_ag.commit()
cont_lstwk = cursor.fetchall()
conexion_ag.close()

#conteos de ayer
sql3 = ("select validos,novalidos from fn_conteos('"+ytd+"')")
conexion_ag = psycopg2.connect(database="prueba", user="usuario", password="pruebas123", host= "localhost", port= 5432)
cursor=conexion_ag.cursor()
cursor.execute(sql3)
conexion_ag.commit()
cont_ytd = cursor.fetchall()
conexion_ag.close()
#
#creando excel
#
workbook = xlsxwriter.Workbook('Rpt_'+ytd+'.xlsx')
# cell_format = workbook.add_format({'bold': True, 'bg_color': '#008000', 'align': 'center'})
Header = workbook.add_format({'bold': True, 'bg_color': '#33D633', 'align': 'center'})
#format2 = workbook.add_format({'num_format': 'yyyy mmm dd','align': 'center'})
format2 = workbook.add_format({'bold': True, 'bg_color': '#33D633','align': 'center'})
#Header_date = workbook.add_format({'bold': True, 'bg_color': '#8FBC8F', 'align': 'center','num_format': 'yyyy mmm dd'})
f_total = workbook.add_format({'bold': True, 'align': 'center'})
worksheet = workbook.add_worksheet()
worksheet.write('A1', '',Header)
worksheet.write('B1', '',Header)
worksheet.merge_range('B1:C1',lastyear.strftime("%A %Y-%m-%d"), Header)
#worksheet.write('C1', '',Header)
worksheet.write('A2', 'Hora',Header)
worksheet.write('B2', 'Validos',Header)
worksheet.write('C2', 'No Validos',Header)
worksheet.write('D1', '',Header)
worksheet.merge_range('D1:E1',lastweek.strftime("%A %Y-%m-%d"), Header)
# worksheet.write('E1', '',Header)
worksheet.write('D2', 'Validos',Header)
worksheet.write('E2', 'No Validos',Header)
worksheet.write('F1', '',Header)
worksheet.merge_range('F1:G1',yesterday.strftime("%A %Y-%m-%d"), Header)
worksheet.write('F2', 'Validos',Header)
worksheet.write('G2', 'No Validos',Header)


row_y = 2
col = 0
tot_pb = 0
tot_sp = 0

center = workbook.add_format({'align': 'center','bg_color': '#6FA8DC'})
for hora, pb,sp in (cont_lstyr):
    tot_pb += pb
    tot_sp += sp
    worksheet.write(row_y,col,hora,format2)
    worksheet.write(row_y,col +1,pb,center)
    worksheet.write(row_y,col +2,sp,center)
    row_y +=1

row_w = 2
tot_pb_lswk = 0
tot_sb_lswk = 0
for pb,sp in (cont_lstwk):
    tot_pb_lswk += pb
    tot_sb_lswk += sp
    worksheet.write(row_w,col + 3,pb,center)
    worksheet.write(row_w,col + 4,sp,center)
    row_w +=1

row_ytd = 2
tot_pb_ytd = 0
tot_sb_ytd = 0
for pb,sp in (cont_ytd):
    tot_pb_ytd += pb
    tot_sb_ytd += sp
    worksheet.write(row_ytd,col + 5,pb,center)
    worksheet.write(row_ytd,col + 6,sp,center)
    row_ytd +=1

row = 0
if row_y >= row_w >= row_ytd:
    row = row_y
if row_w >= row_ytd >= row_y:
        row = row_w
if row_ytd >= row_y >= row_w:
    row = row_ytd

#Pintamos la fila de totales
worksheet.write(row, 0, 'Total:',format2)
worksheet.write(row,1,tot_pb,format2)
worksheet.write(row,2,tot_sp,format2)
worksheet.write(row,3,tot_pb_lswk,format2)
worksheet.write(row,4,tot_sb_lswk,format2)
worksheet.write(row,5,tot_pb_ytd,format2)
worksheet.write(row,6,tot_sb_ytd,format2)
workbook.close()

print("Finalizo el proceso.")