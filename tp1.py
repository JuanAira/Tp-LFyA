

"""Funcion para descomprimir la cadena"""

def descomprimir(cadena):
    ListaCadena = []
    ListaCadena = cadena.split("\n")
    return (ListaCadena)

"""Funcion para determinar si es g3"""

"""prueba = ("A:b A\nA:a\nA:A B c\nA:lambda\nB:b")"""

def DeterminarGrado3(cadena):
    error=[]
    texto=""
    ListaCadena = cadena.split("\n")
    band=True

    lista2=[]
    for x1 in range(0, len(ListaCadena)):
        lista2.append(ListaCadena[x1].split(":"))

    listaDeLista=[]

    for x in range(0, len(lista2)):
        listaDeLista=lista2[x]

    mayusculasAntecedente = len([c for c in listaDeLista[0] if c.isupper()])
    minusculasAntecedente = len([c for c in listaDeLista[0] if c.islower()])

    if minusculasAntecedente>=1:
        band = False
        error = lista2[x]
        texto = "Existe un terminal en el antecedente: nt->t"

    if mayusculasAntecedente>1:
        band = False
        error = lista2[x]
        texto = "Existe mas de un no terminal en el antecedente: NTNT->t"

    if listaDeLista[1]=="lambda":
        texto="Existe lambda en el consecuente: NT->lambda"

    mayusculasconsecuente = len([c for c in listaDeLista[1] if c.isupper()])
    minusculasConsecuente = len([c for c in listaDeLista[1] if c.islower()])

    if (minusculasConsecuente>1):
        if mayusculasconsecuente==0:
            band=False
            error = lista2[x]
            texto="Existe mas de un terminal en el consecuente: NT->tt"

    if mayusculasconsecuente>1:
        band = False
        error = lista2[x]
        texto = "Existe mas de un no terminal en el consecuente : NT->NT NT"

    if (mayusculasconsecuente  ==1):
        if (minusculasConsecuente==0):
            band = False
            error = lista2[x]
            texto = "Existe un no terminal en el consecuente, pero no un terminal: NT->NT"
    else:
        if(mayusculasconsecuente > 1):
                if minusculasConsecuente>1:
                    band = False
                    error = lista2[x]
                    texto = "Existe mas de un no terminal y mas de un terminal en el consecuente: NT->ntnt NTNT"

    if band:
        texto="Es g3 ya que cumple con todas las condiciones: NT->t, NT->NT t, NT->t NT"
        return (texto)
    else:
        ExpresionErronea= error[0] + "->" + error[1]
        return (ExpresionErronea,texto)

def verificarSiEsG3(Lista):
    texto = ""


    return texto



"""Funcion para determinar si es g2"""

def verificarSiEsG2(Lista):
    texto = ""
    return texto



"""Funcion para determinar si es g1"""

def verificarSiEsG1(Lista):
    texto = ""
    return texto



"""Funcion general llamando a las demas (g3,g2,g1)"""


def clasificar_gramatica(cadenaString):
    listaTerminos=[]
    listaTerminos=descomprimir(cadenaString)




    diccionario={
                3: ("A:A B c", "no pertenece a ninguna de las formas NT -> t, NT -> NT t, NT -> t NT"),
                2: ("A:A B c", "no pertenece a ninguna de las formas NT -> t, NT -> NT t, NT -> t NT"),
                1: ("A:A B c", "no pertenece a ninguna de las formas NT -> t, NT -> NT t, NT -> t NT"),
                0: ("A:A B c", "no pertenece a ninguna de las formas NT -> t, NT -> NT t, NT -> t NT")
                }

    return diccionario