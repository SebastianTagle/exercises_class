
#Esto es para definir una función y no tener que estar escribiendo repetidas veces una accion (print)
#al momento de definir la función, hay que agregar las variables que le vamos a pedir para que haga lo que necesito.
def Hello(name):
    print(f"Hello {name} !")

Names=["sebastian tagle","Sara Tagle","Paula","Jeronimo"]
for x in Names:
    #con esto llamo la funcion
    Hello(x)
