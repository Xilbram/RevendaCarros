from Veiculo import *
from ViewRevenda import *
from RevendaCarros import RevendaCarros
from Carro import *
from Motor import *



revendedora = RevendaCarros()
viewRevenda = ViewRevendaCarros(revendedora.catalogo, revendedora.lista_nomes, "user", "123", revendedora)


#Instancia de alguns carros e alguns veiculos
motor_V6 = Motor("V6",6, 65)
motor_V8 = Motor("V8", 8, 135)
Kappa_l3 = Motor("Kappa l3", 3, 75)
motor_1_6 = Motor("1.6", 4, 80)
outlander = Carro("Mitsubishi Outlander", "SUV", "Preto", 130000, motor_V6)
santa_fe = Carro("Santa Fé", "SUV", "Prata", 110000, motor_V6)
hb20 = Carro("HB20", "Sedan", "Preto", 60000, Kappa_l3)
fox = Carro("Fox", "Popular", "Branco", 44000, motor_1_6)
cruze = Carro("Cruze", "Sedan", "Branco", 102000, motor_V6)
saveiro = Carro("Saveiro", "Picape", "Vermelha", 74000, motor_V6)
fusion = Carro("Fusion", "Sedan", "Preto", 82500, motor_V6)

lista_carros = [outlander,santa_fe,hb20,fox,cruze,saveiro,fusion]

for carros in lista_carros:
    revendedora.adicioar_ao_catalogo(carros)




viewRevenda.rodar()