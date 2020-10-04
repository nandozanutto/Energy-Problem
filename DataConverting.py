import myclasses as mc


def convertData(h, l, listHidro, listCentral, listArco, inputLines):
    for x in range(1, h + 1):
        linha = inputLines[x].split()
        mi = int(linha[0])
        fi = int(linha[1])
        ci = int(linha[2])
        listHidro.append(mc.Hidroeletrica(mi, fi, ci))

    indexLine = h + 1

    for x in range(indexLine,  indexLine + l):
        di = int(inputLines[x])
        listCentral.append(mc.Central(di))

    indexLine += l

    for x in range(1, h+1):
        ni = int(inputLines[indexLine])
        indexLine += 1
        for y in range(indexLine, indexLine + ni):
            linha = inputLines[y].split()
            inCentral = int(linha[0])
            capacity = int(linha[1])
            cost = int(linha[2])
            listArco.append(mc.Arco(capacity, cost))
            listCentral[inCentral-1].setInput(len(listArco))
            listHidro[x-1].setOutput(len(listArco))
        indexLine += ni

    for x in range(1, l+1):
        ni = int(inputLines[indexLine])
        indexLine += 1
        for y in range(indexLine, indexLine + ni):
            linha = inputLines[y].split()
            inCentral = int(linha[0])
            capacity = int(linha[1])
            cost = int(linha[2])
            listArco.append(mc.Arco(capacity, cost))
            listCentral[inCentral-1].setInput(len(listArco))
            listCentral[x-1].setOutput(len(listArco))
        indexLine += ni
