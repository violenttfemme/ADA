#define una variable de cada tipo de primitivo
numero = 3
flotante = 4.6
maestro = True 
cadena = "str"
#Concatena a la cadena las otras variables aplicando la coversiom correcta para funcionar, guarde el resultado en una variable
concatena = cadena + " "+ str(numero) + " "+ str(flotante) + " "+ str(maestro)
print (concatena)
#el limite de un entero es:Los números se dividen en tres tipos de datos de Python: int / Integer: Int puede almacenar todos los valores enteros. Este tipo de datopuede ser de cualquier tamaño. No hay límite de tamaño. Los float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar. La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308 , pero si no nos crees, lo puedes verificar tu mismo.
#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
n = 20 
for i in range (2, n + 1, 2):
 print (i)
