import PySimpleGUI as sg
from RevendaCarros import *

class ViewRevendaCarros():
    def __init__(self,lista_carros, lista_nome_carros, login: str, senha: str,  revenda:RevendaCarros ):
        self.revenda = revenda
        self.lista_carros = lista_carros
        self.lista_nome_carros = lista_nome_carros
        self.rodando = True
        self.login = login
        self.senha = senha

#janela aberta no começo do programa. Assume-se que o sistema é interno, então o usuario é um funcionario que deve possuir uma conta
    def janela_login(self):
        layout = [[sg.Text("Insira o nome de usuario e a senha")],
                  [sg.Text('Login'), sg.Input(key='login', enable_events=True)],
                  [sg.Text("Senha"), sg.Input('', key='senha', enable_events=True, password_char="*")],
                  [sg.Button("Ok"), sg.Button('Exit')]
                  ]
        return sg.Window("Janela Login", layout, location=(800, 600), finalize=True)

#fornece a janela de catalogo, onde a lista de veiculos é apresentada
    def janela_catalogo(self):
        layout_janela_produtos = [[sg.Text('Revenda de carros')],
                                  [sg.Listbox(values=self.revenda.lista_nomes, size=(20, 12), key="LISTCARS",
                                              enable_events=True)],
                                  [sg.Button('Consultar'), sg.Button('Exit')]]
        return sg.Window('Theme Browser', layout_janela_produtos, location = (800,600), finalize=True)


#permite ver os dados de algum veiculo especifico, e se necessario, altera-los
    def janela_consulta(self, veiculo_a_ser_consultado):

        #a maneira de printar os atributos depende do Getter dos veiculos, recebendo uma tupla e repassando suas posições de atributos (tipo, nome, cor...)
        layout_janela_consulta = [[sg.Text(
        '''
Tipo de veículo: {0[0]}
Nome do carro: {0[1]}
Cor: {0[2]}
Preço: {0[3]} R$
Potência do Motor:{0[4]}
        '''.format(veiculo_a_ser_consultado.GetAtributos()))],
        [sg.Button("Editar"), sg.Button('Ok')]]

        return sg.Window("{}".format(veiculo_a_ser_consultado.GetNome()), layout_janela_consulta, location=(800,600), finalize=True)

#pop-up dentro de consulta, permite a alteração de preço e cor. Outros atributos (de carros) não fariam sentido serem alterados. Mas podem ser implementados sem grandes esforços, seguem a mesma lógica
    def janela_editar(self, veiculo_a_ser_consultado):
        col = [[sg.Text('Novo preço: '), sg.Input('', key='-preco-')],
               [sg.Text('Nova cor: '),   sg.Input('', key='cor')]
               ]

        layout_janela_editar = [[sg.Text( '''
Nome do carro: {0[1]}
Cor: {0[2]}
Preço: {0[3]} R$
        '''.format(veiculo_a_ser_consultado.GetAtributos())), sg.Column(col)],
                                [sg.Button('Confirmar'), sg.Button('Cancelar')]]
        return sg.Window('Editar veiculo', layout_janela_editar, location=(1200,800), finalize=True)


    def rodar(self):

#no geral, somente uma janela deve estar aberta por vez. É permitido em casos de pop-ups ter 2 janelas abertas, mas é aconselhado não permitir que elas fiquem abertas para não poluir a tela
        janela0,janela1,janela2,janela3 = self.janela_login(), None,None,None


        while self.rodando:
            window, event, values = sg.read_all_windows()
            #verifica o fechamento do programa
            if event in (sg.WIN_CLOSED, 'Exit'):
                self.rodando = False

#confere se o usuario inseriu a senha e o login corretos
            if window == janela0 and event == "Ok":
                if (values['login'] == self.login) and (values['senha'] == self.senha):
                    janela1 = self.janela_catalogo()
                    window = janela1
                    janela0.close()
                else:
                    sg.popup("Login ou senha incorretos")

#abre a janela de consultas caso o botao Consulta seja pressionado após selecionar um carro
            if event == "Consultar":
                try:
                    for carros in self.revenda.catalogo:
                        if carros.GetNome() == values['LISTCARS'][0]:

                            carro_a_ser_editado = carros
                            janela2 = self.janela_consulta(carros)
                            janela1.close()
                            window = janela2
                except IndexError:
                    sg.popup("Você precisa clicar em um veiculo para ver suas informações")

#abre a janela de edições do veiculo selecionado, permitindo algumas alterações
            if event == 'Editar':
                janela3 = self.janela_editar(carro_a_ser_editado)
                janela2.close()

#confirma e repassa as mudanças de edição do veiculo
            if event == 'Confirmar':
                if values['cor'].isalpha() and values['-preco-'].isnumeric():
                    nova_cor = values['cor']
                    novo_preco = values['-preco-']
                    carro_a_ser_editado.preco = novo_preco
                    carro_a_ser_editado.cor = nova_cor
                    janela2 = self.janela_consulta(carro_a_ser_editado)
                    janela3.close()
                else:
                    sg.popup("Insira uma string para definir a cor e um número para definir o preço")

#cancela as mudanças de edição do veiculo
            if event == 'Cancelar':
                janela2 = self.janela_consulta(carro_a_ser_editado)
                janela3.close()

#
            if window == janela2 and event == 'Ok':
                janela1 = self.janela_catalogo()
                janela2.close()





