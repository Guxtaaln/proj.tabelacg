import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('pessoas.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cidade TEXT NOT NULL
)
''')

# Dados a serem inseridos
dados = [
    ('Fabrício', 34, 'Vila Catarina'),
    ('Maria', 67, 'Trancoso'),
    ('Clarice', 26, 'Roma'),
    ('José', 58, 'Lisboa'),
    ('Eugênia', 41, 'Munique')
]

# Inserir os dados na tabela
cursor.executemany('INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)', dados)

# Salvar (commit) as mudanças
conn.commit()

# Fechar a conexão
conn.close()

print("Tabela criada e dados inseridos com sucesso.")