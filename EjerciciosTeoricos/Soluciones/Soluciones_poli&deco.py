# Ejercicio 1

class Coche:
    def mover(self):
        print("El coche se mueve en cuatro ruedas.")

class Moto:
    def mover(self):
        print("La moto se mueve en dos ruedas.")

class Camion:
    def mover(self):
        print("El camión se mueve en muchas ruedas.")

# Crear objetos para cada tipo de vehículo
coche = Coche()
moto = Moto()
camion = Camion()

# Llamar al método mover para cada vehículo
for vehiculo in [coche, moto, camion]:
    vehiculo.mover() 
        
# Ejercicio 2

class Tomate:
    def tipo(self):
        return "Hortaliza"
    
    def color(self):
        return "Rojo"

class Manzana:
    def tipo(self):
        return "Fruta"
    
    def color(self):
        return "Roja"

class Pera:
    def tipo(self):
        return "Fruta"
    
    def color(self):
        return "Verde"

def mi_funcion(objeto):
    print(objeto.tipo())
    print(objeto.color())

# Crear objetos y usar mi_funcion
tomate = Tomate()
manzana = Manzana()
pera = Pera()

mi_funcion(tomate)
mi_funcion(manzana)
mi_funcion(pera)

# Ejercicio 3

class Spain():
    def capital(self):
        print("Madrid")
 
    def idioma(self):
        print("Español")
 

class Portugal():
    def capital(self):
        print("Lisboa")
 
    def idioma(self):
        print("Portugués")
 
objeto_spain = Spain()
objeto_portugal = Portugal()

for pais in (objeto_spain, objeto_portugal):
    pais.capital()
    pais.idioma()


#                                   Ejercicio 4: 
#       -------------------------       RETO      -------------------------

# EJ:1
def imprimir_mensaje(func):
    def wrapper(objeto):
        print(f"Antes de mover el {objeto.__class__.__name__}:")
        return func(objeto)
    return wrapper

class Coche:
    @imprimir_mensaje
    def mover(self):
        print("El coche se mueve en cuatro ruedas.")

class Moto:
    @imprimir_mensaje
    def mover(self):
        print("La moto se mueve en dos ruedas.")

class Camion:
    @imprimir_mensaje
    def mover(self):
        print("El camión se mueve en muchas ruedas.")

# Crear objetos para cada tipo de vehículo
coche = Coche()
moto = Moto()
camion = Camion()

# EJ:2

def imprimir_tipo_y_color(func):
    def wrapper(objeto):
        print(objeto.tipo())
        print(objeto.color())
        func(objeto)
    return wrapper

class Tomate:
    @imprimir_tipo_y_color
    def tipo(self):
        return "Hortaliza"
    
    def color(self):
        return "Rojo"

class Manzana:
    @imprimir_tipo_y_color
    def tipo(self):
        return "Fruta"
    
    def color(self):
        return "Roja"

class Pera:
    @imprimir_tipo_y_color
    def tipo(self):
        return "Fruta"
    
    def color(self):
        return "Verde"

def mi_funcion(objeto):
    pass  # This function is empty because it's being invoked by the decorator

# Usage
mi_funcion(Tomate())
mi_funcion(Manzana())
mi_funcion(Pera())


# EJ:3

def imprimir_mensaje(func):
    def wrapper(objeto):
        print(f"Función {func.__name__} llamada para {objeto.__class__.__name__}:")
        return func(objeto)
    return wrapper

class Spain:
    @imprimir_mensaje
    def capital(self):
        print("Madrid")
 
    @imprimir_mensaje
    def idioma(self):
        print("Español")
 

class Portugal:
    @imprimir_mensaje
    def capital(self):
        print("Lisboa")
 
    @imprimir_mensaje
    def idioma(self):
        print("Portugués")
 
objeto_spain = Spain()
objeto_portugal = Portugal()

for pais in (objeto_spain, objeto_portugal):
    pais.capital()
    pais.idioma()
    


