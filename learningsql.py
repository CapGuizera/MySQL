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

#Cria uma tabela no MySQL
def CreateTab(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {nomeTabela} (Nome VARCHAR(50))")
            print('Tabela criada com sucesso')
    except Exception as e:
        print(f'Erro: {e}')

#Remove uma tabela no MySQL
def RemoveTab(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
            print('Tabela REMOVIDA com sucesso')
    except Exception as e:
        print(f'Erro: {e}')
#Insere um registro no MySQL
def InsertTab(nomeTabela, nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO {nomeTabela} (Nome) VALUES ('{nome}')")
            con.commit()
            print('Registro inserido com sucesso')
    except Exception as e:
        print(f'Erro: {e}')
#Modifica um Registro no MySQL
def modificaTab(nomeTabela, nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE {nomeTabela} SET Nome = '{nome}' WHERE Nome = 'João'")
            con.commit()
            print('Registro modificado com sucesso')
    except Exception as e:
        print(f'Erro: {e}')
#Remove Registro do MySQL
def removeRegistro(nomeTabela, nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM {nomeTabela} WHERE Nome = '{nome}'")
            con.commit()
            print('Registro removido com sucesso')
    except Exception as e:
        print(f'Erro: {e}')

modificaTab('teste', 'marco')

con.close()
