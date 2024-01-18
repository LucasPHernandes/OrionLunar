import dearpygui.dearpygui as dpg
import sqlite3

def list_items():
    conexao = sqlite3.connect("DB/dbOrionLunar.db")
    cursor = conexao.cursor()

    # Selecionar todos os itens da tabela Itens
    cursor.execute("SELECT * FROM Itens")
    itens = cursor.fetchall()

    with dpg.window(label="Ver Itens"):
        # Exibir os itens
        with dpg.table(header_row=True):
            # Adicionar cabeçalhos
            dpg.add_table_column(label="COD")
            dpg.add_table_column(label="NOME")
            dpg.add_table_column(label="QUANTIDADE")
            dpg.add_table_column(label="CATEGORIA")

            # Preencher a tabela com os dados recuperados
            for item in itens:
                # Adicionar uma nova linha à tabela
                with dpg.table_row():
                    # Adicionar células na linha com os valores do item
                    dpg.add_text(item[0])  # COD
                    dpg.add_text(item[1])  # NOME
                    dpg.add_text(item[2])  # QUANTIDADE
                    dpg.add_text(item[3])  # CATEGORIA

        # Fechar a conexão
    conexao.close()
    
    
    
def add_item():
    conexao = sqlite3.connect("DB/dbOrionLunar.db")
    cursor = conexao.cursor()
    
    nome = "Cabo HDMI"
    quantidade = 12
    categoria = "Audio e Video"

    # Inserir dados na tabela Itens
    cursor.execute("INSERT INTO Itens (NOME, QUANTIDADE, CATEGORIA) VALUES (?, ?, ?)", (nome, quantidade, categoria))

    # Commit para salvar as alterações
    conexao.commit()

    # Fechar a conexão
    conexao.close()

dpg.create_context()

with dpg.window(tag="Main", label="Main Window"):
    
    dpg.add_text(tag="OrionLunar", default_value="OrionLunar")
    dpg.add_text(tag="description", default_value="Sistema para controle de empréstimo de itens da CTI - FW.")
    
    with dpg.group(horizontal=True):
        dpg.add_button(tag="Listar Itens", label="Listar todos os Itens", callback=list_items)
        dpg.add_button(tag="Adicionar Item", label="Adicionar Item", callback=add_item)
        # dpg.add_button(tag="Emprestar Item", label="Emprestar Item", callback=out_item)


dpg.create_viewport(title="OrionLunar", x_pos=640, y_pos=360)
dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.set_primary_window("Main", True)
dpg.start_dearpygui()
dpg.destroy_context()