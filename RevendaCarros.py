

#responsavel por armazenar os veiculos em um catalogo, e tem metodos para repassar informações e printar
class RevendaCarros():
    def __init__(self):
        self.catalogo = []
        self.lista_nomes = []
        self.rodando = True

    def mostrar_catalogo(self):
        for i in self.catalogo:
            print(i.GetAtributos())

    def adicioar_ao_catalogo(self, args):
        self.catalogo.append(args)
        self.lista_nomes.append(args.GetNome())

    def get_catalogo(self):
        return self.catalogo


