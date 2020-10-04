class Hidroeletrica:
    def __init__(self, m, f, c):

        self.m = m
        self.f = f
        self.c = c
        self.outputs = []

    def imprimir(self):
        print("Hidro with the values", self.m, self.f, self.c, "outputs:", self.outputs)

    def setOutput(self, x):
        self.outputs.append(x)


class Central:
    def __init__(self, d):
        self.d = d
        self.inputs = []
        self.outputs = []

    def imprimir(self):
        print("Central with the value", self.d, "inputs:", self.inputs, "outputs:", self.outputs)

    def setInput(self, x):
        self.inputs.append(x)

    def setOutput(self, x):
        self.outputs.append(x)


class Arco:
    def __init__(self, capacity, cost):
        self.capacity = capacity
        self.cost = cost

    def imprimir(self):
        print("Arco with the values", self.capacity, self.cost)
