
CREATE TABLE IF NOT EXISTS hospede (
    id_hospede INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    documento_passaporte TEXT NOT NULL UNIQUE,
    telefone TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS quarto (
    id_quarto INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_quarto TEXT NOT NULL UNIQUE,
    categoria TEXT NOT NULL CHECK(categoria IN ('Standard', 'Luxo', 'Suíte')),
    preco_diaria REAL NOT NULL CHECK(preco_diaria > 0)
);

CREATE TABLE IF NOT EXISTS reserva (
    id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
    id_hospede INTEGER NOT NULL,
    id_quarto INTEGER NOT NULL,
    data_checkin TEXT NOT NULL,
    data_checkout TEXT NOT NULL,
    valor_total REAL NOT NULL CHECK(valor_total >= 0),
    FOREIGN KEY (id_hospede) REFERENCES hospede(id_hospede) ON DELETE RESTRICT,
    FOREIGN KEY (id_quarto) REFERENCES quarto(id_quarto) ON DELETE RESTRICT,
    CHECK(data_checkout > data_checkin)
);

CREATE INDEX IF NOT EXISTS idx_reserva_quarto ON reserva(id_quarto);
CREATE INDEX IF NOT EXISTS idx_reserva_hospede ON reserva(id_hospede);