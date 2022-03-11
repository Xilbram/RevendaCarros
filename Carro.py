from Veiculo import *
from Motor import *

#É possivel criar outros veiculos, como motos ou caminhoes. Como o projeto não exigia variadade, não expandi, mas a possibilidade é de facil aplicação
class Carro(Veiculo):
    def __init__(self, nome_carro, classificao_veiculo, cor, preco, motor):
        super().__init__(classificao_veiculo, cor, preco, motor)
        self.nome_carro = nome_carro

    def GetAtributos(self):
        return [self.classificacao,self.nome_carro, self.cor, self.preco, self.motor.get_tipo()]
    def GetNome(self):
        return self.nome_carro