#proyecto: cumpleaños
#autor: ricardo nistch 
#carnet: 1618720
#el fin de este programa es localizar la edad de una persona en base a la fecha de nacimiento

from datetime import date

# la fecha de hoy 
hoy = date.today()

# obtener el dia de hoy 
dia = hoy.day

#obtener el mes de hoy
mes = hoy.month

#obtener el año de hoy 
year = hoy.year

# recolectar los datos de la persona
print( 'hola que tal, hoy vamos a ver calcular tu edad')

# tenemos que saber el dia de nacimiento de la persona 
nombre = input('¿puedes ingresar tu nombre? ')
apellido = input('¿puedes ingresar tu apellidos:? ')

# tenemos que saber el dia de nacimiento de la persona
dia_naci = input = input( '¿puedes ingresar el dia el que naciste? ')
dia_naci = int(dia_naci)

# tenemos que saber el mes en que naciste 
mes_naci = input( '¿puedes ingresar el mes en que naciste? ')
mes_naci = int(mes_naci)

# tenemos que saber el año en el que nacio
year_naci = input('¿podrias ingresar el año en que naciste? ')
year_naci = int(year_naci) 
 
#bueno ahora tenemos que restar el año actual con la fecha de cumploaños de la persno

diff_year = year - year_naci
diff_dia = dia - dia_naci
diff_mes = mes - mes_naci
diff_year -= ((mes , dia) < (mes_naci , dia_naci)) 

# string - cadena - str

print('que bien, alfin lo logramos ya sabemos la edad que ties'  + str(diff_year) + ' años ' + str(diff_mes) +' dias ')