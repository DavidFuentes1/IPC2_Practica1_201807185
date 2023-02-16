from xml.dom import minidom
from game import*
from ListaNoOrdenada import *


listPlatform = []

arch = minidom.parse("entrada.xml")
juegosViejos = arch.getElementsByTagName("JuegosViejos")

for juegoViejo in juegosViejos:
    print("________Lista de Plataformas___________")
    listaPlataformas = juegoViejo.getElementsByTagName("ListaPlataformas")
    for unaPlataforma in listaPlataformas:
        plataformas = unaPlataforma.getElementsByTagName("Plataforma")
        for Plataforma in plataformas:
            code = Plataforma.getElementsByTagName("codigo")[0]
            name = Plataforma.getElementsByTagName("nombre")[0]
            print(code.firstChild.data, name.firstChild.data) 
            consola = game(int(code.firstChild.data), name.firstChild.data )
            listPlatform.append(consola)

            print(consola.code)

for juegoViejo in juegosViejos:  
    print("__________Lista de Juegos___________") 
    listadoJuegos = juegoViejo.getElementsByTagName("Juego")
    for juego in listadoJuegos:
        code = juego.getElementsByTagName("codigo")[0]
        name = juego.getElementsByTagName("nombre")[0]
        print(code.firstChild.data, name.firstChild.data) 
        print()  

for plats in listPlatform:
    print(plats.retItem())