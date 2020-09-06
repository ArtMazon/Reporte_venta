from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

usuarios=[["admin","admin",1],["Juan","Rojo",0],["Daniel","Azul",0],["Roman","Verde",1]]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
######################################################
###El poceso corresponde a la lista de los 50 producots más vendidos
lista_pivote_uno = lifestore_sales[:] 
lista_cincuenta_sinorden = []

while lista_pivote_uno:
  producto_id=lista_pivote_uno[0][1]#SE tomara el id de cada producto
  i=0
  for variable in lifestore_sales:
      if producto_id==variable[1] and variable[3] !=0:# Se compara cuantas veces aparece el id en la lista de ventas y si tuvo devolucion
        i+=1 #El contador en caso de que se encuentre el id
        lista_pivote_uno.remove(variable) #Se remueve de la lista pivote
  lista_cincuenta_sinorden.append([producto_id,i])# Se añade cuantas veces se vendio cada producto por su id , con el contador i

lista_pivote_dos = lista_cincuenta_sinorden[:]
lista_cincuenta_conorden=[]
while lista_pivote_dos:
  maximo = lista_pivote_dos[0][1] #Se toma como maximo las ventas del primer elemento de la lista pivote
  for variable in lista_pivote_dos:
    if maximo < variable[1]: #Se busca el maximo verdadero
      maximo=variable[1]
  for variable in lista_pivote_dos:#SE buscan todas las veces que se repite el maximo , y se eliminan
    if maximo== variable[1]:
      lista_cincuenta_conorden.append(variable)
      lista_pivote_dos.remove(variable)

########################################################
# El proceso corresponde a la lista de 100 los productos más buscados
lista_pivote_uno = lifestore_searches[:]
lista_cien_sinorden = []

while lista_pivote_uno:
  producto_id=lista_pivote_uno[0][1]
  i=0
  for variable in lifestore_searches:
    if producto_id==variable[1]:
      i+=1
      lista_pivote_uno.remove(variable)
  lista_cien_sinorden.append([producto_id,i])
                       
lista_pivote_dos = lista_cien_sinorden[:]
lista_cien_conorden=[]

while lista_pivote_dos:
  maximo = lista_pivote_dos[0][1]
  for variable in lista_pivote_dos:
    if maximo < variable[1]:
       maximo=variable[1]

  for variable in lista_pivote_dos:
    if maximo== variable[1]:
      lista_cien_conorden.append(variable)
      lista_pivote_dos.remove(variable)
#########################################################
# Este proceso crea una lista con todas las posibles categorias que existan para los productos
lista_pivote_categorias=lifestore_products[:]
lista_categorias=[]
while lista_pivote_categorias:
  categoria=lista_pivote_categorias[0][3]
  
  for variable in lifestore_products:
    if categoria== variable[3]:
      lista_pivote_categorias.remove(variable)
  lista_categorias.append(categoria)    
 
################################################
# Este proceso separa los productos por categorias
lista_categorias_productos=[] #Cada elemento de esta lista sera una lista con productos, donde todos tienen en comun la categoria
for cat in lista_categorias:
  categoria_separada=[]
  for variable in lifestore_products:
    if cat == variable[3]:
      categoria_separada.append(variable)
  lista_categorias_productos.append(categoria_separada)

###########################################################
# Este proceso es para los 50 productos con menor venta , por categoria
lista_categorias_cincuenta_sinorden = []
for lista in lista_categorias_productos:
  lista_producto_especifico_sin_orden=[]
  for producto in lista:
    i=0
    for venta in lifestore_sales:
      if producto[0] == venta[1]:
        i+=1
    lista_producto_especifico_sin_orden.append([producto[0],i])

  lista_categorias_cincuenta_sinorden.append(lista_producto_especifico_sin_orden)  

lista_categorias_cincuenta_con_orden = []

for lista in lista_categorias_cincuenta_sinorden:
  lista_producto_especifico_con_orden=[]
  lista_pivote_uno=lista[:]

  while lista_pivote_uno:
    maximo=lista_pivote_uno[0][1]

    for variable in lista_pivote_uno:
      if maximo < variable[1]:
        maximo=variable[1]

    for variable in lista_pivote_uno:
      if maximo== variable[1]:
        lista_producto_especifico_con_orden.append(variable)
        lista_pivote_uno.remove(variable)
  lista_categorias_cincuenta_con_orden.append(lista_producto_especifico_con_orden)

#Aqui empieza el proceso para darle el orden inverso a la lista anterior, ya que la lista esta ordenada de mayor a menor, esto la conviernte de menor a mayor cada lista por categoria
lista_categorias_cincuenta_con_orden_inverso=[]
auxiliar=[]
for lista in lista_categorias_cincuenta_con_orden:
  auxiliar=lista[::-1]
  lista_categorias_cincuenta_con_orden_inverso.append(auxiliar)

##########################################################
#Aqui empiezan los procedimientos para la lista de 100 menos buscados por categoria
###########################################################

lista_categorias_cien_sinorden = []
for lista in lista_categorias_productos:
  lista_producto_especifico_sin_orden=[]
  for producto in lista:
    i=0
    for busqueda in lifestore_searches:
      if producto[0] == busqueda[1]:
        i+=1
    lista_producto_especifico_sin_orden.append([producto[0],i])

  lista_categorias_cien_sinorden.append(lista_producto_especifico_sin_orden)  

lista_categorias_cien_con_orden = []

for lista in lista_categorias_cien_sinorden:
  lista_producto_especifico_con_orden=[]
  lista_pivote_uno=lista[:]

  while lista_pivote_uno:
    maximo=lista_pivote_uno[0][1]

    for variable in lista_pivote_uno:
      if maximo < variable[1]:
        maximo=variable[1]

    for variable in lista_pivote_uno:
      if maximo== variable[1]:
        lista_producto_especifico_con_orden.append(variable)
        lista_pivote_uno.remove(variable)
  lista_categorias_cien_con_orden.append(lista_producto_especifico_con_orden)

#Aqui empieza el proceso para darle el orden inverso a la lista anterior, ya que la lista esta ordenada de mayor a menor, esto la conviernte de menor a mayor cada lista por categoria

lista_categorias_cien_con_orden_inverso=[]
auxiliar=[]


for lista in lista_categorias_cien_con_orden:
  auxiliar=lista[::-1]
  lista_categorias_cien_con_orden_inverso.append(auxiliar)



##########################################################
#Aqui  empieza los procesos para las reseñas de 20 mejores reseñas y 20 peores reseñas 
#
lista_pivote_uno = lifestore_sales[:]
lista_veinte_sin_orden_positivo = []

while lista_pivote_uno:
  producto_id=lista_pivote_uno[0][1]
  i=0
  calificacion=0
  for variable in lifestore_sales:
      if producto_id==variable[1]:
        calificacion+=variable[2]
        i+=1
        lista_pivote_uno.remove(variable)
  lista_veinte_sin_orden_positivo.append([producto_id,int(10*(calificacion/i))/10])

lista_pivote_dos = lista_veinte_sin_orden_positivo[:]
lista_veinte_con_orden_positivo=[]
while lista_pivote_dos:
  maximo = lista_pivote_dos[0][1]
  for variable in lista_pivote_dos:
    if maximo < variable[1]:
      maximo=variable[1]
  for variable in lista_pivote_dos:
    if maximo== variable[1]:
      lista_veinte_con_orden_positivo.append(variable)
      lista_pivote_dos.remove(variable)

#Aqui empieza el proceso para darle el orden inverso a la lista anterior, ya que la lista esta ordenada de mayor a menor, esto la conviernte de menor a mayor 
lista_veinte_con_orden_negativo=lista_veinte_con_orden_positivo[::-1]

###########################################################
#Esta seccion busca clasificar las ventas de acuerdo al mes en que se obutvieron
ventas_por_mes = []  #Esta será la lista lifestore_sales ordenada cronologicamente las ventas.
for x in range(12):
    x += 1
    lista_mes=[]
    for ventas in lifestore_sales:
        if x < 10:
            mes = "/" + "0" + str(x) + "/" #Busca encontrar el formato /00/ que tiene el mes en la base de datos
            if mes in ventas[3]:
                lista_mes.append(ventas)
                continue
        else:
            mes = "/" + str(x) + "/"
            if mes in ventas[3]:
                lista_mes.append(ventas)
    ventas_por_mes.append(lista_mes)


##############################################################
#Este proceso crea listas de venta por mes, tomando solo el id de producto, la cantidad vendida en el mes, y el valor generado por este en el mes
lista_ventas_mensuales = []

for lista in ventas_por_mes:
  lista_producto_especifico_sin_orden=[]
  for producto in lifestore_products:
    i=0
    for venta in lista:
      
      if producto[0] == venta[1] and 0 != venta[3]:
        i+=1
    if i !=0:
       lista_producto_especifico_sin_orden.append([producto[0],i,producto[2]*i])

  lista_ventas_mensuales.append(lista_producto_especifico_sin_orden)


#######################################
#En esta parte construimos el proceso de realizar el reporte mensual
salida="Si"
acceso=0
while salida=="Si":
    print("Bienvenido al sistema de analisis de Life Store")
    usuario=input("usuario \n")
    contraseña=input("contrseña \n")

    for variable in usuarios:
        if usuario==variable[0] and contraseña == variable[1]:
            acceso=1
            privilegio=variable

    if acceso == 1:
        if privilegio[2]==0:
            print("Bienvenido "+privilegio[0])
            print("Solo tienes nivel de seguridad usuario, necesitas privilegios de administrador")
            salida=input("¿Deseas volver al menu de inicio?(Si \ No) ")
        else:
            while salida=="Si":
                print("Aqui empieza el menu")
                print("1.- Los 50 productos más vendidos")
                print("*"*20)
                print("2.- los 100 productos más buscados")
                print("*"*20)
                print("3.- Los 50 productos con menores ventas, por categoria")
                print("*"*20)
                print("4.- los 100 productos con menores busquedas, por categoria")
                print("*"*20)                
                print("5.- Los 20 productos con mejor reseñas")
                print("*"*20)
                print("6.- Los 20 productos con peor reseñas")
                print("*"*20)
                print("7.- Total de ingresos y ventas promedio mensuales")
                print("*"*20)
                print("8.- Total de ingresos y ventas anuales.")
                print("*"*20)

                menu=input("Ingrese el número de la opción a realizar \n")

                print(2*"\n")
                if menu=="1":
                  
                    n=0   
                    for   variable in lista_cincuenta_conorden:
                      n+=1
                      print(lifestore_products[variable[0]-1][1]+"\n"+" Es el °"+str(n)+" más vendido "+" con "+str(variable[1])+" ventas")
                      print(20*"*")

                      if n>49:
                        break

                elif menu == "2":

                  n=0   
                  for   variable in lista_cien_conorden:
                    n+=1
                    print(lifestore_products[variable[0]-1][1]+"\n"+" Es el °"+str(n)+" más buscado "+" con "+str(variable[1])+" busquedas")
                    print(20*"*")

                    if n>99:
                      break
                elif menu == "3":
                  i=0

                  for variable in lista_categorias:
                    i+=1
                    print(str(i)+".- "+variable)
                    print(20*"*")
                  opcion=input("Introduzca la categoria que quiera analizar \n")
                  n=0

                  for variable in lista_categorias_cincuenta_con_orden_inverso[int(opcion)-1]:
                    n+=1
                    print(lifestore_products[variable[0]-1][1]+"\n" +" Es el °"+str(n)+" menos vendido en la categoria "+lista_categorias[int(opcion)-1]+" con "+str(variable[1])+" ventas")
                    print(20*"*") 
                elif menu == "4":
                  i=0

                  for variable in lista_categorias:
                    i+=1
                    print(str(i)+".- "+variable)
                    print(20*"*")
                  opcion=input("Introduzca la categoria que quiera analizar \n")
                  n=0


                  for variable in lista_categorias_cien_con_orden_inverso[int(opcion)-1]:
                    n+=1
                    print(lifestore_products[variable[0]-1][1]+"\n" +" Es el °"+str(n)+" menos buscado en la categoria "+lista_categorias[int(opcion)-1]+" con "+str(variable[1])+" busquedas")
                    print(20*"*") 
                elif menu== "5":
                    n=0   
                    for  variable in lista_veinte_con_orden_positivo:
                      n+=1
                      print(lifestore_products[variable[0]-1][1]+"\n"+" Es el °"+str(n)+" mejor evaluado "+" con una calificaciín de "+str(variable[1])+" Estrellas")
                      print("********************")

                      if n>19:
                        break      
                elif menu == "6": 
                    n=0   
                    for  variable in lista_veinte_con_orden_negativo:
                      n+=1
                      print(lifestore_products[variable[0]-1][1]+"\n"+" Es el °"+str(n)+" peor evaluado "+" con una calificaciín de "+str(variable[1])+" Estrellas")
                      print("********************")

                      if n>19:
                        break 
                elif menu == "7":
                  i=0

                  for variable in meses:
                    i+=1
                    print(str(i)+".- "+variable)
                    print(20*"*")
                  opcion=input("Introduzca el mes que quiera analizar \n")
                  total_ventas_mensual=0
                  total_valor_mensual=0


                  for variable in lista_ventas_mensuales[int(opcion)-1]:
                    
                    total_ventas_mensual+=variable[1]
                    total_valor_mensual+=variable[2]


                    print(lifestore_products[variable[0]-1][1]+"\n" +" vendió "+str(variable[1])+" unidades con una ganancia de $"+str(variable[2]))
                    print(20*"*") 
                  
                  valor_promedio=str(int(100*(total_valor_mensual/total_ventas_mensual))/100)
                  
              

                  print("\n Un total de "+str(total_ventas_mensual)+ " ventas con un valor total de $"+str(total_valor_mensual)+ " con un valor promedio de venta de $"+valor_promedio+" por compra")
                

                elif menu=="8":
                  total_ventas_mensual=0
                  total_valor_mensual=0
                     
                  for   variable in lista_cincuenta_conorden:

                    total_ventas_mensual+=variable[1]
                    total_valor_mensual+=variable[1]*lifestore_products[variable[0]-1][2]
                    valor=variable[1]*lifestore_products[variable[0]-1][2]

                    print(lifestore_products[variable[0]-1][1]+"\n" +" vendió "+str(variable[1])+" unidades con una ganancia de $"+str(valor))
                    print(20*"*") 
                  
                  valor_promedio=str(int(100*(total_valor_mensual/total_ventas_mensual))/100)
                  
              

                  print("\n Un total de "+str(total_ventas_mensual)+ " ventas en el año con un valor total de $"+str(total_valor_mensual)+ " con un valor promedio de venta de $"+valor_promedio+" por compra")
                else:
                  print("Opcion no valida")

                salida=input("\n ¿Desea volver al menu principal? (Si \ No ) **Cerrar el menu, cerrara la sesion y el programa** \n")  

              
    else:
        print("Usuario o contraseña incorrecta")
        salida=input("¿Deseas volver ingresar su informacion de usuario?(Si \ No) \n")



