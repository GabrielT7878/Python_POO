import tkinter as tk
from dominio.Loja import Loja
from dominio.Endereco import Endereco
from dominio.execoes.DescricaoProdutoInexistente import DescricaoProdutoInexistente
from dominio.pagamento.Operadora import Operadora
from dominio.servicos.calculadora_juros_simples import CalculadoraJurosSimples

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermercado Preço Bão")
        self.root.geometry("800x600")

        # Criando a loja e as registradoras
        endereco = Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000")
        self.loja = Loja("Supermercado Preço Bão", endereco)
        self.registradoras = [self.loja.get_registradora("R01"), self.loja.get_registradora("R02"), self.loja.get_registradora("R03")]
        self.current_registradora = 0

        # Criando a interface gráfica
        self.create_widgets()

    def create_widgets(self):
        # Tabela de produtos
        self.product_table = tk.LabelFrame(self.root, text="Produtos")
        self.product_table.pack(side=tk.LEFT, padx=10, pady=10)

        # Descrição, preço unitário, quantidade e subtotal em tabelas lado a lado
        tk.Label(self.product_table, text="Descrição").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.product_table, text="Preço Unitário").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.product_table, text="Quantidade").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self.product_table, text="Subtotal").grid(row=0, column=3, padx=5, pady=5)

        # Botões de alternar registradoras
        self.change_registradora_frame = tk.LabelFrame(self.root, text="Registradoras")
        self.change_registradora_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(self.change_registradora_frame, text="Registradora Atual:").grid(row=0, column=0, padx=5, pady=5)
        self.current_registradora_label = tk.Label(self.change_registradora_frame, text=f"{self.registradoras[self.current_registradora].get_id()}")
        self.current_registradora_label.grid(row=0, column=1, padx=5, pady=5)

        self.prev_registradora_button = tk.Button(self.change_registradora_frame, text="Anterior", command=self.prev_registradora)
        self.prev_registradora_button.grid(row=1, column=0, padx=5, pady=5)

        self.next_registradora_button = tk.Button(self.change_registradora_frame, text="Próxima", command=self.next_registradora)
        self.next_registradora_button.grid(row=1, column=1, padx=5, pady=5)

    def prev_registradora(self):
        self.current_registradora = (self.current_registradora - 1) % len(self.registradoras)
        self.update_current_registradora_label()

    def next_registradora(self):
        self.current_registradora = (self.current_registradora + 1) % len(self.registradoras)
        self.update_current_registradora_label()

    def update_current_registradora_label(self):
        self.current_registradora_label.config(text=f"{self.registradoras[self.current_registradora].get_id()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
