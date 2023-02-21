from xml.dom import minidom
from game import*
from ListaOrdenada import*
import xml.etree.ElementTree as ET

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8').decode('utf8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


listaPlataforma = ListaOrdenada()
listaJuego = ListaOrdenada()


#Head del XML
xmlJuego = ET.Element("JuegosViejos")
print('INGRESE LA RUTA ABSOLUTA DEL DOCUMENTO A INSEPECCIONAR')
ruta = input()
arch = minidom.parse(str(ruta))
juegosViejos = arch.getElementsByTagName("JuegosViejos")

for juegoViejo in juegosViejos:
     print("________Lista de Plataformas___________")
     listadoPlataforma = juegoViejo.getElementsByTagName("ListaPlataformas")
     for unaPlataforma in listadoPlataforma:
         plataformas = unaPlataforma.getElementsByTagName("Plataforma")
         for Plataforma in plataformas:
             code = Plataforma.getElementsByTagName("codigo")[0]
             name = Plataforma.getElementsByTagName("nombre")[0]
             print(code.firstChild.data, name.firstChild.data)
             x = code.firstChild.data
             y = name.firstChild.data 
             listaPlataforma.InsertarPlataforma(x,y)

listaPlataforma.OrdenarPlataforma()
print(listaPlataforma.ImprimirPlataforam())     
Lplats = ET.SubElement(xmlJuego,"ListaPlataformas")
head = listaPlataforma.Cabeza
while head != None:
    plt = ET.SubElement(Lplats,"Plataforma")
    ET.SubElement(plt, "codigo").text = str(head.getNumeroPlataforma())
    ET.SubElement(plt, 'nombre').text = str(head.getNamePlt())
    head = head.Next



print()                        
        

for juegoViejo in juegosViejos:  
    print("__________Lista de Juegos___________") 
    listadoJuegos = juegoViejo.getElementsByTagName("Juego")
    for juego in listadoJuegos:
        code = juego.getElementsByTagName("codigo")[0]
        name = juego.getElementsByTagName("nombre")[0]
        listadoPlats = juego.getElementsByTagName("Plataforma")
        for plate in listadoPlats:
            plat = plate.getElementsByTagName("codigo")[0]
            z = plat.firstChild.data             
        x = code.firstChild.data
        y = name.firstChild.data
        print(x,y,z) 
        listaJuego.InsertarJuego(x,y,z)
print()

listaJuego.OrdenarJuego()
print(listaJuego.Impimir())	
Lju = ET.SubElement(xmlJuego, 'ListadoJuegos')
apuntador = listaJuego.Cabeza
while apuntador != None:
    ju = ET.SubElement(Lju, 'Juego')
    ET.SubElement(ju,'codigo').text = str(apuntador.getNumeroJuego())
    ET.SubElement(ju, 'nombre').text = str(apuntador.getNameJuego())
    pl = ET.SubElement(ju, 'Plataforma')
    ET.SubElement(pl, 'codigo').text = str(apuntador.getPltJuego())
    apuntador = apuntador.Next

print('Ingrese Nombre del archivo para Guardar')    
nameArc= input()
arc = open(str(nameArc)+'.xml', 'a')
arc.write(prettify(xmlJuego))

