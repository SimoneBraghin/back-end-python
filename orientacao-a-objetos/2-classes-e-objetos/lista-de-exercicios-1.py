# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro: # Convenção para nomes de classes: PascalCasing
    def __init__(self):
        self.ligado = False
        self.cor = "verde"
        self.modelo = "Volkswagen"
        self.velocidade = 0
        self.velocidadeMin = 0
        self.velocidadeMax = 180

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def velocidade_aumentar(self):
        if not self.ligado:
            return

        if self.velocidade < self.velocidadeMax:
            self.velocidade += 5

    def velocidade_reduzir(self):
        if not self.ligado:
            return

        if self.velocidade > self.velocidadeMin:
            self.velocidade -= 5
        
    def __str__(self) -> str:
        return f'Televisao - ligada {self.ligada} - canal {self.canal} - volume {self.volume}'


# Crie uma instância da classe carro.
carro_1 = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
carro_1.ligar()
print('O Carro está ligado? {}'.format(carro_1.ligado))

for _ in range(6):
    carro_1.velocidade_aumentar()

print('O Carro está ligado? {}'.format(carro_1.ligado))
print('Qual a velocidade atual? {}'.format(carro_1.velocidade))
print()


# Faça o carro "parar" utilizando os métodos da sua classe.

for _ in range(6):
    carro_1.velocidade_reduzir()

print('O Carro está ligado? {}'.format(carro_1.ligado))
print('Qual a velocidade atual? {}'.format(carro_1.velocidade))
carro_1.desligar()
print('O Carro está ligado? {}'.format(carro_1.ligado))