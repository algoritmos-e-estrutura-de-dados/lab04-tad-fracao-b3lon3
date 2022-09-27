class Fracao:
    numerador = 1
    denominador = 1

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def add(self, fracao):
        num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador

        return Fracao(num, den)

    def sub(self, fracao):
        num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador

        return Fracao(num, den)

    def mult(self, fracao):
        num = self.numerador * fracao.numerador
        den = self.denominador * fracao.denominador

        return Fracao(num,den)

    def simplify (self,fracao):
        div = math.gcd(fracao.numerador , fracao.denominador)

        return f"{fracao.numerador/div}/{fracao.denominador/div}"

    def solve(self):
        return self.numerador / self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


fracao1 = Fracao(1, 2)
fracao2 = Fracao(1, 3)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao2.sub(fracao1)
fracao5 = fracao1.mult(fracao2)

fracao6 = Fracao(2,4)

print(fracao3)
print(fracao4)
print(fracao5)

fracao7 = fracao6.simplify()
print(fracao7)
