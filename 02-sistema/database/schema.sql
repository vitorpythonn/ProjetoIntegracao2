PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS localizacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    deposito TEXT NOT NULL,
    setor TEXT NOT NULL,
    posicao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 0,
    preco REAL NOT NULL,
    localizacao_id INTEGER NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categoria(id),
    FOREIGN KEY (localizacao_id) REFERENCES localizacao(id)
);

CREATE TABLE IF NOT EXISTS movimentacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('ENTRADA', 'SAIDA')),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    data TEXT NOT NULL,
    responsavel TEXT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES produto(id)
);

CREATE TABLE IF NOT EXISTS compra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    status TEXT NOT NULL,
    solicitante TEXT NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES produto(id)
);

CREATE TABLE IF NOT EXISTS nota_fiscal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL,
    data TEXT NOT NULL,
    validada INTEGER NOT NULL DEFAULT 0
);

INSERT OR IGNORE INTO categoria (nome) VALUES
('Eletrônicos'),
('Informática'),
('Acessórios');

INSERT OR IGNORE INTO localizacao (deposito, setor, posicao) VALUES
('Depósito A', 'Setor 1', 'A01'),
('Depósito A', 'Setor 1', 'A02'),
('Depósito B', 'Setor 2', 'B01');