import pymysql.cursors

con = pymysql.connect(
    host= "localhost",
    user= "root",
    password= "",
    port = 3306,
    db= "learnsql",
    charset= "utf8mb4",
    cursorclass= pymysql.cursors.DictCursor

)

def CreateTab(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {nomeTabela} (Nome VARCHAR(50))")
            print('Tabela criada com sucesso')
    except Exception as e:
        print(f'Erro: {e}')

def RemoveTab(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
            print('Tabela REMOVIDA com sucesso')
    except Exception as e:
        print(f'Erro: {e}')

def InsertTab(nomeTabela, nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO {nomeTabela} (Nome) VALUES ('{nome}')")
            con.commit()
            print('Registro inserido com sucesso')
    except Exception as e:
        print(f'Erro: {e}')

def modificaTab(nomeTabela, nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE {nomeTabela} SET Nome = '{nome}' WHERE Nome = 'João'")
            con.commit()
            print('Registro modificado com sucesso')
    except Exception as e:
        print(f'Erro: {e}')

modificaTab('teste', 'marco')

con.close()
