class DescricaoProdutoInexistente(Exception):
    def __init__(self, mensagem, id):
        super().__init__(mensagem)
        self.id = id

    def __str__(self):
        return super().__str__() + "\n" + "ID....: " + str(self.id)
