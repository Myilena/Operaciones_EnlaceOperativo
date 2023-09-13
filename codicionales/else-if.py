ingreso_mensual = 81000
gasto_mensual =80000

if ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en deficit")
    elif ingreso_mensual - gasto_mensual >3000:
        print("Estás bien de dinero")
    else:
        print("Estas gastando en mucha ropa, hay que ver si alnza")    


elif ingreso_mensual <10000:
    print("Tienes buena economia en latinoamerica")

elif ingreso_mensual <500:
    print("Tienes buena economia en peru")

elif ingreso_mensual <200:
    print("Tienes buena economia en brasil ")
else:
    print("Estas en la pobreza")