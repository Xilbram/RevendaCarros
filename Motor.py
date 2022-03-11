class Motor():
    def __init__(self, tipo,num_cilindros, angulo):
        self.__tipo = tipo
        self.cilindros = num_cilindros
        self.angulo = angulo
    def get_tipo(self):
        return self.__tipo