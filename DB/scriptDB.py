import sqlite3

# Conectar ao banco de dados SQLite
conexao = sqlite3.connect("DB/dbOrionLunar.db")

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Comando SQL para criar a tabela de itens
comando_sql_itens = '''
    CREATE TABLE Itens (
        COD INTEGER PRIMARY KEY,
        NOME TEXT NOT NULL,
        QUANTIDADE INTEGER,
        CATEGORIA TEXT
    )
'''

# Comando SQL para criar a tabela de empréstimos
comando_sql_emprestimos = '''
    CREATE TABLE Emprestimos (
        PROTOCOLO INTEGER PRIMARY KEY,
        CPF TEXT,
        COD INTEGER,
        QUANTIDADE INTEGER,
        SAIDA TEXT,
        DEVOLUCAO TEXT,
        FOREIGN KEY (COD) REFERENCES Itens (COD)
    )
'''

# comando_select_items

# Executar os comandos SQL
cursor.execute(comando_sql_itens)
cursor.execute(comando_sql_emprestimos)

# Commit para salvar as alterações
conexao.commit()

# Fechar a conexão
conexao.close()
