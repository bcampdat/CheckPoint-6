# Ejercicio 1

class Coche:
    def __init__(self, matricula, marca, combustible):
        self.matricula = matricula
        self.marca = marca
        self.combustible = combustible
        
mi_coche = Coche("1234 ABC", "Peugeot", "Gasolina")  
      
print(mi_coche) 
        
# Ejercicio 2

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def recuperar_contrasena(self):
        return f"Usuario: {self.nombre_usuario},\nContraseña: {self.contrasena}"
    
# Crear un objeto usando la clase Usuario
usuario1 = Usuario("mi_usuario", "mi_contraseña")

# uso del método
print (usuario1.recuperar_contrasena())

# Ejercicio 3

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        return "Guau!"

# Crear un objeto perro
mi_perro = Perro("Fido", "Labrador")

# Acceder a los atributos y métodos del perro
print(mi_perro.nombre)  # Output: Fido
print(mi_perro.ladrar())  # Output: Guau!

# Ejercicio 4

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
libro1 = Libro("La novia gitana", "Carmen Mola")
libro2 = Libro("El hombre de tiza", "C.J. Tudor")

print(libro1.informacion())
print(libro2.informacion())

# Ejercicio 5
class Bicicleta:
    def __init__(self, tipo_sillin, num_radios, diametro_rueda):
        self.tipo_sillin = tipo_sillin
        self.num_radios = num_radios
        self.diametro_rueda = diametro_rueda

    def frenar(self):
        return "Frenando la bicicleta"

    def pedalear(self):
        return "Pedaleando la bicicleta"

    def girar(self, direccion):
        return f"Girando la bicicleta hacia {direccion}"


bicicleta = Bicicleta("comodo", 36, 26)

print(bicicleta.frenar())
print(bicicleta.pedalear())
print(bicicleta.girar("izquierda"))

# Ejercicio 6

class ContadorPalabras:
    def __init__(self, texto):
        self.texto = texto

    def __len__(self):
        return len(self.texto.split())

texto = "Hola mundo, este es un texto de ejemplo."
contador = ContadorPalabras(texto)
print(len(contador))  

# Ejercicio 7

class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __eq__(self, other):
        return (self.dia == other.dia) and (self.mes == other.mes) and (self.año == other.año)

fecha1 = Fecha(12, 4, 2024)
fecha2 = Fecha(12, 4, 2024)
fecha3 = Fecha(15, 4, 2024)
print(fecha1 == fecha2)  # Salida: True
print(fecha1 == fecha3)  # Salida: False


# Ejercicio 8      
#       -------------------------    RETO      ----------------------------------

class Calculadora:
    def __init__(self, valor=0):
        self.valor = valor

    def __add__(self, otro):
        return Calculadora(self.valor + otro.valor)

    def __sub__(self, otro):
        return Calculadora(self.valor - otro.valor)

    def __mul__(self, otro):
        return Calculadora(self.valor * otro.valor)

    def __truediv__(self, otro):
        return Calculadora(self.valor / otro.valor)

    def __str__(self):
        return str(self.valor)

# Crear un objeto de la clase Calculadora
calc1 = Calculadora(10)
calc2 = Calculadora(20)

# Realizar operaciones
suma = calc1 + calc2
resta = calc1 - calc2
multiplicacion = calc1 * calc2
division = calc1 / calc2

# Imprimir los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)