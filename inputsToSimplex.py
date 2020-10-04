

def equationsCentral(h, aux, listArco):
    arcoSize = len(listArco)
    resultEQ = []
    emptyList = [0] * h
    for x in range(1, arcoSize + 1):
        if(x in aux.inputs):
            resultEQ.append(-1)
        elif (x in aux.outputs):
            resultEQ.append(1)
        else:
            resultEQ.append(0)

    emptyList.extend(resultEQ)
    return emptyList

def equationsHidro(h, aux, listArco, listHidro):
    arcoSize = len(listArco)
    resultEQ = []
    emptyList = [0] * h
    for x in range(1, arcoSize + 1):
        if(x in aux.outputs):
            resultEQ.append(1)
        else:
            resultEQ.append(0)

    emptyList[listHidro.index(aux)] = - aux.f
    emptyList.extend(resultEQ)
    return emptyList

def constraints(listCentral, h, listArco, listHidro):
    A = []
    for x in listHidro:
        A.append(equationsHidro(h, x, listArco, listHidro))
    for x in listCentral:
        A.append(equationsCentral(h, x, listArco))
    return A

def bounds(listHidro, listArco, R):
    bounds = []
    for x in listHidro:
        xi_bounds = (0, min(x.m/x.f, R))
        bounds.append(xi_bounds)
    for x in listArco:
        xi_bounds = (0, x.capacity)
        bounds.append(xi_bounds)
    return bounds

def vector(listHidro, listArco):
    c = []
    for x in listHidro:
        c.append(x.c)
    for x in listArco:
        c.append(x.cost)
    return c

def results(listHidro, listCentral):
    b = []
    for x in listHidro:
        b.append(0)
    for x in listCentral:
        b.append(-x.d)
    return b