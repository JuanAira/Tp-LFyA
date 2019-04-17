

def DeterminarGrado3(cadena):
    error=[]
    texto=" Es g3 porque cumple ya que cumple con todas las condiciones: NT->t , NT->t NT, NT->t NT, NT-> lambda "
    ListaCadena = cadena.split("\n")
    band=True
    ListaRetornar = []


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
        texto = "Existe un terminal en el antecedente: t->t"

    if mayusculasAntecedente>1:
        band = False
        error = lista2[x]
        texto = "Existe mas de un no terminal en el antecedente: NTNT->t"


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

    ListaRetornar.append(band)
    ListaRetornar.append(texto)

    if band:
        return (ListaRetornar)
    else:
        ExpresionErronea= error[0] + "->" + error[1]
        ListaRetornar.append(ExpresionErronea)
        return (ListaRetornar)


def DeterminarGrado2(cadena):
    error = []
    texto = " Es g2 porque el antecedente tiene que ser un único No terminal y en el consecuente cualquier combinación "
    ListaCadena = cadena.split("\n")
    band = True
    ListaRetornar = []

    lista2 = []
    for x1 in range(0, len(ListaCadena)):
        lista2.append(ListaCadena[x1].split(":"))

    listaDeLista = []

    for x in range(0, len(lista2)):
        listaDeLista = lista2[x]

    mayusculasAntecedente = len([c for c in listaDeLista[0] if c.isupper()])
    minusculasAntecedente = len([c for c in listaDeLista[0] if c.islower()])

    if minusculasAntecedente >= 1:
        band = False
        error = lista2[x]
        texto = "Existe un terminal en el antecedente: t->t"

    if mayusculasAntecedente > 1:
        band = False
        error = lista2[x]
        texto = "Existe mas de un no terminal en el antecedente: NTNT->t"

    ListaRetornar.append(band)
    ListaRetornar.append(texto)

    if band:
        return (ListaRetornar)
    else:
        ExpresionErronea = error[0] + "->" + error[1]
        ListaRetornar.append(ExpresionErronea)
        return (ListaRetornar)


def DeterminarGrado1(cadena):
    error = []
    texto = " Es g1 porque el antecedente tiene que ser un único No terminal y en el consecuente cualquier combinación y el consecuente debe tener igual o mas simbolos que el antecedente "
    ListaCadena = cadena.split("\n")
    band = True
    ListaRetornar = []


    lista2 = []
    for x1 in range(0, len(ListaCadena)):
        lista2.append(ListaCadena[x1].split(":"))

    listaDeLista = []

    for x in range(0, len(lista2)):
        listaDeLista = lista2[x]

    mayusculasAntecedente = len([c for c in listaDeLista[0] if c.isupper()])
    minusculasAntecedente = len([c for c in listaDeLista[0] if c.islower()])

    mayusculasconsecuente = len([c for c in listaDeLista[1] if c.isupper()])
    minusculasConsecuente = len([c for c in listaDeLista[1] if c.islower()])

    cantant = mayusculasAntecedente + minusculasAntecedente
    cantconc = mayusculasconsecuente + minusculasConsecuente

    if (cantconc < cantant):
        band = False
        error = lista2[x]
        texto = "La cantidad del antecedente es mayor a la cantidad del concecuente"

    ListaRetornar.append(band)
    ListaRetornar.append(texto)

    if band:
        return (ListaRetornar)
    else:
        ExpresionErronea = error[0] + "->" + error[1]
        ListaRetornar.append(ExpresionErronea)
        return (ListaRetornar)



def clasificar_gramatica(cadenaString):
    Resultado = DeterminarGrado3(cadenaString)

    diccionario={}

    ok=True
    noes = False
    if Resultado[0]:
        diccionario['3']= Resultado[1]
        noes = True
    else:
        diccionario['3'] = Resultado[2], Resultado[1]
        ok=False

    if ok==False:
        Resultado = DeterminarGrado2(cadenaString)
        if Resultado[0]:
            diccionario['2'] = Resultado[1]
        else:
            diccionario['2'] =  Resultado[2], Resultado[1]
            ok = False
    if ok == False:
        Resultado = DeterminarGrado1(cadenaString)
        if Resultado[0]:
            diccionario['1'] = Resultado[1]
            noes=True
        else:
            diccionario['1'] = Resultado[2],Resultado[1]
    if (noes == False):
        diccionario['0'] = "Es g0"

    return diccionario


prueba=clasificar_gramatica("A:b A\nA:a\nA:A B c\nA:lambda\nBaD:bBB")