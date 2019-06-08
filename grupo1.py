

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
            break

        if mayusculasAntecedente>1:
            band = False
            error = lista2[x]
            texto = "Existe mas de un no terminal en el antecedente: NTNT->t"
            break


        mayusculasconsecuente = len([c for c in listaDeLista[1] if c.isupper()])
        minusculasConsecuente = len([c for c in listaDeLista[1] if c.islower()])

        if (minusculasConsecuente>1):
            if mayusculasconsecuente==0:
                band=False
                error = lista2[x]
                texto="Existe mas de un terminal en el consecuente: NT->tt"
                break
            else:
                band = False
                error = lista2[x]
                texto = "Existe mas de un terminal en el consecuente: NT->ttNTNT"
                break


        if mayusculasconsecuente>1:
            band = False
            error = lista2[x]
            texto = "Existe mas de un no terminal en el consecuente : NT->NT NT"
            break

        if (mayusculasconsecuente  ==1):
            if (minusculasConsecuente==0):
                band = False
                error = lista2[x]
                texto = "Existe un no terminal en el consecuente, pero no un terminal: NT->NT"
                break
        else:
            if(mayusculasconsecuente > 1):
                    if minusculasConsecuente>1:
                        band = False
                        error = lista2[x]
                        texto = "Existe mas de un no terminal y mas de un terminal en el consecuente: NT->ntnt NTNT"
                        break

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
            break

        if mayusculasAntecedente > 1:
            band = False
            error = lista2[x]
            texto = "Existe mas de un no terminal en el antecedente: NTNT->t"
            break

    ListaRetornar.append(band)
    ListaRetornar.append(texto)

    if band:
        return (ListaRetornar)
    else:
        ExpresionErronea = error[0] + "->" + error[1]
        ListaRetornar.append(ExpresionErronea)
        return (ListaRetornar)


def DeterminarGrado1(cadena):
    """Para la clasificación de las gramáticas de tipo G1 se tomará el criterio de los autores Alfonseca y otros, el cual mencionaque: "no se permiten derivaciones por la palabra vacía (lambda) a
    excepción de que dicha palabra se encuentre en una única regla donde el antecedente sea el distinguido, siempre y cuando el distinguido no tenga ninguna recursión en el resto de sus reglas
    """

    error = []
    texto = " Es g1 porque el antecedente tiene que ser un único No terminal y en el consecuente cualquier combinación y el consecuente debe tener igual o mas simbolos que el antecedente o puede ser lamda "
    ListaCadena = cadena.split("\n")
    band = True
    ListaRetornar = []


    lista2 = []
    for x1 in range(0, len(ListaCadena)):
        lista2.append(ListaCadena[x1].split(":"))

    listaDeLista = []

    verificarDistinguido=False

    for x in range(0, len(lista2)):
        listaDeLista = lista2[x]

        mayusculasAntecedente = len([c for c in listaDeLista[0] if c.isupper()])
        minusculasAntecedente = len([c for c in listaDeLista[0] if c.islower()])

        mayusculasconsecuente = len([c for c in listaDeLista[1] if c.isupper()])
        minusculasConsecuente = len([c for c in listaDeLista[1] if c.islower()])

        cantant = mayusculasAntecedente + minusculasAntecedente
        cantconc = mayusculasconsecuente + minusculasConsecuente

        if verificarDistinguido:
            if listaDeLista[0]!= distinguido:
                if listaDeLista[1]== 'lambda':
                    band = False
                    error = lista2[x]
                    texto = "No se permite lambda en un atecedente que no sea el distinguido"
                    break
            else:
                if distinguido in listaDeLista[1]:
                    banderadistinguido=True

                if banderadistinguido:
                    if listaDeLista[1]=='lambda':
                        texto="no es g1 porque el distinguido deriva en lambda y posee recursión"
                        break
        else:
            distinguido= listaDeLista[0]
            if distinguido in listaDeLista[1]:
                banderadistinguido=True


        if (cantconc < cantant):
            band = False
            error = lista2[x]
            texto = "La cantidad del antecedente es mayor a la cantidad del concecuente"
            break

        verificarDistinguido=True

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
        diccionario['2'] = ''
        diccionario['1'] = ''
        diccionario['0'] = ''
        noes = True
    else:
        diccionario['3'] = Resultado[2], Resultado[1]
        ok=False

    if ok==False:
        Resultado = DeterminarGrado2(cadenaString)
        if Resultado[0]:
            diccionario['2'] = Resultado[1]
            diccionario['1'] = ''
            diccionario['0'] = ''
        else:
            diccionario['2'] =  Resultado[2], Resultado[1]
            ok = False
    if ok == False:
        Resultado = DeterminarGrado1(cadenaString)
        if Resultado[0]:
            diccionario['1'] = Resultado[1]
            diccionario['0'] = ''
            noes=True
        else:
            diccionario['1'] = Resultado[2],Resultado[1]
    if (noes == False):
        diccionario['0'] = "Es g0"

    return diccionario




"""S= clasificar_gramatica('A:b c N Y s\nA:A b\nA:lambda')"""




""""""


def apilar(simbolo,pila):
    """ Agrega el elemento x a la pila. """
    pila.append(simbolo)


def desapilar(pila):
    """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. """
    try:
        return pila.pop()
    except IndexError:
        raise ValueError("La pila está vacía")


def es_vacia(pila):
    """ Devuelve True si la lista está vacía, False si no. """
    return pila == []


def descomprimirDiccionario(diccionario):
    listaRetornar = []
    lista = []
    for x in diccionario:
        lista.append(x)
        var = diccionario[x]
        for transiciones in var:
            lista.append(transiciones)
        listaRetornar.append(lista)
        lista = []

    return listaRetornar


def validar_cadena(cadena, lista):
    pila = []
    pila.append('Z0')
    estadosAceptación = lista

    listaEstados_Transiciones = descomprimirDiccionario(
        {'a': [('(', 'Z0', ['(', 'Z0'], 'a'), ('(', '(', ['(', '('], 'a'), (')', '(', [''], 'b')],
         'b': [(')', '(', [''], 'b'), ('$', 'Z0', ['Z0'], 'b')]})
    resultado = True

    listaTransiciones= listaEstados_Transiciones[0]
    estado= listaTransiciones[0]

    for entrada in cadena:
        if len(pila)==1 and pila[0]=='Z0' and entrada=='$':
            desapilar(pila)
            if estado in estadosAceptación:
                resultado = True
            else:
                resultado=False
            break

        indice=0
        listaTrancionesEncontradasParaLaEntrada= []

        while indice <= (len(listaTransiciones)-1):
            transicion = listaTransiciones[indice]
            if transicion[0] == entrada:
                listaTrancionesEncontradasParaLaEntrada.append(transicion)
            indice= indice + 1

        if len(listaTrancionesEncontradasParaLaEntrada)==0:
            resultado = False
            break
        else:
            aplicarTransicion=[]
            ok=True

            for transicionEncontrada in listaTrancionesEncontradasParaLaEntrada:
                if ok:
                    if len(pila) ==1 and pila[0]=='Z0' and transicionEncontrada[1]=='Z0':
                        aplicarTransicion=transicionEncontrada
                        ok=False
                    else:
                        aplicarTransicion=transicionEncontrada

            if len(aplicarTransicion[2])==0 or aplicarTransicion[2]=='lambda' or aplicarTransicion[2]=='' or aplicarTransicion[2]=="" or aplicarTransicion[2]==[''] or aplicarTransicion[2]== [""]:
                if len(pila)!=1:
                    desapilar(pila)
                    estado= aplicarTransicion[3]
                else:
                    resultado=False
                    break

            else:
                verificar=desapilar(pila)
                if verificar=='Z0' and 'Z0'in aplicarTransicion[2]:
                    apilar('Z0',pila)
                    cont =0
                    sacar=0
                    for zo in aplicarTransicion[2]:
                        if zo=='Z0':
                            sacar=cont
                        cont = cont + 1
                    aplicarTransicion[2].pop(sacar)
                for i in aplicarTransicion[2]:
                    apilar(i,pila)
                estado= aplicarTransicion[3]


    return  resultado

s=validar_cadena('(())$',["b"])


class AutomataPila:


    """ Esta clase implementa un automáta de pila a partir de la definición de
    estados y transiciones que lo componen, pudiendo validar si una cadena dada
    puede ser reconocida por el mismo.
    """

    def __init__(self, estados, estados_aceptacion):
        """ Constructor de la clase.

        Args
        ----
        estados: dict
            Diccionario de estados que especifica en las claves los nombres de los
            estados y como valores una lista de transiciones salientes de dicho estado.
            Cada transición se compone de: (s,p,a,e) siendo
            s -> símbolo que se consume de la entrada para aplicar la transición.
            p -> símbolo que se consume del tope de la pila para aplicar la transición.
            a -> lista de símbolo/s que se apila una vez aplicada la transición.
            e -> estado de destino.

            Ejemplo:
            {'a': [
                   ( '(' , 'Z0', ['Z0'], 'a')  ,
                   ( '(' , '(' , ['('  , '(' ] , 'a') ,
                   ( ')' , '(' , ['']  , 'b')
                   ],
             'b': [
                   (')', '(', [''], 'b'),
                   ('$', 'Z0', ['Z0'], 'b')
                   ]
            }

        estados_aceptacion: array-like
            Estados que admiten fin de cadena.

            Ejemplo:
            ['b']
        """



        self.estados = []
        self.estado_actual = None
        self.cadena_restante = ''

        self.pila=[]







