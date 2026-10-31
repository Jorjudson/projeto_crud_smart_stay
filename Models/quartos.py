class Quarto:
    CATEGORIAS_VALIDAS = {"Standard", "Luxo", "Suíte"}

    def __init__(
        self, 
        id_quarto: int | None, 
        numero_quarto: str, 
        categoria: str, 
        preco_diaria: float
    ):
        if not numero_quarto or not numero_quarto.strip():
            raise ValueError("O número do quarto não pode ser vazio.")
        
        if categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError(
                f"Categoria inválida ('{categoria}'). "
                f"Escolha entre: {', '.join(self.CATEGORIAS_VALIDAS)}"
            )
        
        if preco_diaria <= 0:
            raise ValueError("O preço da diária deve ser maior que zero.")

        self.id_quarto = id_quarto
        self.numero_quarto = numero_quarto.strip()
        self.categoria = categoria
        self.preco_diaria = float(preco_diaria)

    def __repr__(self) -> str:
        return (
            f"Quarto(id={self.id_quarto}, "
            f"numero='{self.numero_quarto}', "
            f"categoria='{self.categoria}', "
            f"preco=R${self.preco_diaria:.2f})"
        )