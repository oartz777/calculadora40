#hola1
import psycopg2
import math

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "victor",
        password = "victor",
        dbname = "postgres"
    )
    print("conexión exitosa")
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("Verifique los parametros")


while True:

    print("""
    CALCULADORA PROYECTOS A.I.I
    
    1) Suma
    2) Resta
    3) Multiplicacion
    4) División
    5) Potencia 
    6) Raíz Cuadrada
    7) Ver historial de operaciones
    8) Guardar ultima operacion
    """)
    try:
     opcion = int(input("Elige una opción: ") )     
    
    
     if opcion == 1:
        try:
         operacion = "suma"
         n1 = float(input("Introduce tu primer número: ") )
         n2 = float(input("Introduce tu segundo número: ") )
         resultado = n1+n2
         print(" ")
         print("RESULTADO:",resultado)
        except :
            print("solo puede ingresar numeros")

             
     elif opcion == 2:
          try:
           operacion = "resta"   
           n1 = float(input("Introduce tu primer número: ") )
           n2 = float(input("Introduce tu segundo número: ") )
           resultado = n1-n2
           print(" ")
           print("RESULTADO:",resultado)
          except :
              print("solo puede ingresar numeros")

           
     elif opcion == 3:
          try:
           operacion = "multiplicacion"   
           n1 = float(input("Introduce tu primer número: ") )
           n2 = float(input("Introduce tu segundo número: ") )
           resultado = n1*n2
           print(" ")
           print("RESULTADO:",resultado)
          except :
              print("solo puede ingresar numeros")
          

     elif opcion == 4:
          try:
           operacion = "division"   
           n1 = float(input("Introduce tu primer número: ") )
           n2 = float(input("Introduce tu segundo número: ") )
           resultado = n1/n2
           print(" ")
           print("RESULTADO:",resultado)
          except ZeroDivisionError:
              print("el segundo numero no puede ser 0")
          except:
              print("solo puede ingresar numeros")

     elif opcion == 5:
        try:
         operacion = "potencia"
         n1 = float(input("Introduce el numero que sera la base: ") )
         n2 = float(input("Introduce el numero que sera la potencia: ") )
         resultado = n1**n2
         print(" ")
         print("RESULTADO:",resultado)
        except :
            print("solo puede ingresar numeros")

     elif opcion == 6:
          try:
           operacion = "raiz cuadrada"
           n1 = float(input("Introduce un número: ") )
           n2 = float(input("Vuelva a introducir el numero: ") )
           resultado=math.sqrt(n1)
           print(" ")
           print("RESULTADO:",resultado)
          except:
              print("solo puede ingresar un numero positivo")
    
     elif opcion == 7:
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM calculadoraintento11;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        cursor.close()
        conexion.close()

     elif opcion == 8:
        break
     else:
        print("Opción incorrecta")
    except : 
     print("solo puede ingresar numeros")


cursor = conexion.cursor()
cursor.execute("INSERT INTO calculadoraintento11(operacion,numero_1,numero_2,resultado) VALUES(%s,%s,%s,%s);",(operacion,n1,n2,resultado))
conexion.commit()
cursor.close()
conexion.close()

