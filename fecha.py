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
        if int(mes) > 0 and int(mes) < 13:
            fecha=año+mes+"01"
        else:
            fecha=año+"0101"
    
    print(fecha)