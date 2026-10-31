class Hospede:
    
    def __init__(
        self, 
        id_hospede: int | None, 
        nome: str, 
        documento_passaporte: str, 
        telefone: str | None = None, 
        email: str | None = None
    ):
        if not nome or not nome.strip():
            raise ValueError("O nome do hóspede não pode ser vazio.")
        if not documento_passaporte or not documento_passaporte.strip():
            raise ValueError("O documento/passaporte não pode ser vazio.")

        self.id_hospede = id_hospede
        self.nome = nome.strip()
        self.documento_passaporte = documento_passaporte.strip()
        self.telefone = telefone.strip() if telefone else None
        self.email = email.strip() if email else None

    def __repr__(self) -> str:
        return f"Hospede(id={self.id_hospede}, nome='{self.nome}', passaporte='{self.documento_passaporte}')"