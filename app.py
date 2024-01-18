import dearpygui.dearpygui as dpg
import sqlite3

# def list_items():
#     conexao = sqlite3.connect("DB/dbOrionLunar.db")
#     cursor = conexao.cursor()

#     # Selecionar todos os itens da tabela Itens
#     cursor.execute("SELECT * FROM Itens")
#     itens = cursor.fetchall()
    
#     dpg.delete_item("ver_itens")

#     with dpg.window(tag="ver_itens", label="Ver Itens", width=550, height=250, pos=[150, 150]):
#         dpg.add_input_text(tag="pesquisar_input", hint="Pesquisar")
#         dpg.add_button(label="Recarregar Tabela", callback=list_items)
#         # Exibir os itens
#         with dpg.table(header_row=True):
#             # Adicionar cabeçalhos
#             dpg.add_table_column(label="COD")
#             dpg.add_table_column(label="NOME")
#             dpg.add_table_column(label="QUANTIDADE")
#             dpg.add_table_column(label="CATEGORIA")

#             # Preencher a tabela com os dados recuperados
#             for item in itens:
#                 # Adicionar uma nova linha à tabela
#                 with dpg.table_row():
#                     # Adicionar células na linha com os valores do item
#                     dpg.add_text(item[0])  # COD
#                     dpg.add_text(item[1])  # NOME
#                     dpg.add_text(item[2])  # QUANTIDADE
#                     dpg.add_text(item[3])  # CATEGORIA

#         # Fechar a conexão
#     conexao.close()
    
def list_items(sender, app_data):
    conexao = sqlite3.connect("DB/dbOrionLunar.db")
    cursor = conexao.cursor()

    # Obter o texto da barra de pesquisa
    search_text = str(dpg.get_value("pesquisar_input"))

    # Construir a consulta SQL com base na pesquisa
    if search_text and search_text != "None":
        query = f"SELECT * FROM Itens WHERE NOME LIKE '%{search_text}%' OR QUANTIDADE LIKE '%{search_text}%' OR CATEGORIA LIKE '%{search_text}%'"
    else:
        query = "SELECT * FROM Itens"


    # Executar a consulta SQL
    cursor.execute(query)
    itens = cursor.fetchall()

    # Fechar a conexão
    conexao.close()
    
    # Limpar a janela existente
    dpg.delete_item("ver_itens_window")

    with dpg.window(tag="ver_itens_window", label="Itens Encontrados", width=550, height=250, pos=[250, 280]):
        with dpg.group(horizontal=True):
            dpg.add_input_text(tag="pesquisar_input", hint="Pesquisar")
            dpg.add_button(tag="pesquisar_btn", label="Pesquisar", callback=list_items)
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
                    dpg.add_text(item[3])  # CATEGORI
    
def add_item():
    conexao = sqlite3.connect("DB/dbOrionLunar.db")
    cursor = conexao.cursor()
    
    nome = "Pendrive"
    quantidade = 10
    categoria = "Armazenamento"

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


dpg.create_viewport(title="OrionLunar", x_pos=250, y_pos=80)
dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.set_primary_window("Main", True)
dpg.start_dearpygui()
dpg.destroy_context()