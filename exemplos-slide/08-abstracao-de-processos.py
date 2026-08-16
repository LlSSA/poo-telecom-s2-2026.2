class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __lt__(self, other: "Produto") -> bool:
        return self.preco < other.preco

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Produto):
            return NotImplemented
        return self.preco == other.preco
    def __repr__(self) -> str:
        return f"Produto(nome={self.nome}, preco={self.preco})"

if __name__ == "__main__":
    produtos = [
        Produto("Notebook", 3500.00),
        Produto("Mouse", 150.00),
        Produto("Teclado", 300.00),
    ]

    ordenados = sorted(produtos)
    print("Produtos ordenados por preço (crescente):")
    for produto in ordenados:
        print(f"{produto}")

