class Reserva:
    
    def __init__(
        self, 
        id_reserva: int | None, 
        id_hospede: int, 
        id_quarto: int, 
        data_checkin: str, 
        data_checkout: str, 
        valor_total: float
    ):
        if not id_hospede or id_hospede <= 0:
            raise ValueError("O ID do hóspede deve ser um valor válido e positivo.")
        if not id_quarto or id_quarto <= 0:
            raise ValueError("O ID do quarto deve ser um valor válido e positivo.")
            
        if not data_checkin or not data_checkin.strip():
            raise ValueError("A data de check-in não pode estar vazia.")
        if not data_checkout or not data_checkout.strip():
            raise ValueError("A data de check-out não pode estar vazia.")
        
        if valor_total < 0:
            raise ValueError("O valor total da reserva não pode ser negativo.")

        self.id_reserva = id_reserva
        self.id_hospede = id_hospede
        self.id_quarto = id_quarto
        self.data_checkin = data_checkin.strip()
        self.data_checkout = data_checkout.strip()
        self.valor_total = float(valor_total)

    def __repr__(self) -> str:
        return (
            f"Reserva(id={self.id_reserva}, "
            f"hospede_id={self.id_hospede}, "
            f"quarto_id={self.id_quarto}, "
            f"checkin='{self.data_checkin}', "
            f"checkout='{self.data_checkout}', "
            f"total=R${self.valor_total:.2f})"
        )