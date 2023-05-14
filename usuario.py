import mysql.connector

#inicia conexao
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Chor@o1009',
    database='bdusuarios',
)
#iniciaizar a conexao e depoois usar essa conexao para criar o cursor
cursor = conexao.cursor()

#CRUD

#DELETE

nome = "Jennyfer"

comando = f'DELETE FROM cadastro WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit()#Quando precisa editar o banco de dados



#Fechar conexao
cursor.close()
conexao.close()

#CREATE
#comandos entre '' e conteudo dentro do comando ""
# nome = "Lamego"
# email = "teste@teste.com.br"
# senha = "54321"
# telefone = "2199999999"
# data_cadastro = 14

# comando = f'INSERT INTO cadastro (nome, email, senha, telefone, data_cadastro) VALUES ("{nome}", "{email}", "{senha}", "{telefone}", {data_cadastro})'
# cursor.execute(comando)

#Em cada etapa do crud, vamos escolher qual das duas etapas abaixo vamos usar, 
#se for uma edição, faço um commit, se for leitura, faz um fetchall

# conexao.commit()#Quando precisa editar o banco de dados
#resultado = cursor.fetchall()#ler o banco de dados

#READ

# comando = f'SELECT * FROM cadastro'
# cursor.execute(comando)
# # conexao.commit()#Quando precisa editar o banco de dados
# resultado = cursor.fetchall()#ler o banco de dados
# print(resultado)

#UPDATE

# nome = "Jennyfer"
# senha = 111111

# comando = f'UPDATE cadastro SET senha = {senha} WHERE nome = "{nome}"'
# cursor.execute(comando)
# conexao.commit()#Quando precisa editar o banco de dados

#DELETE

# nome = "Jennyfer"

# comando = f'DELETE FROM cadastro WHERE nome = "{nome}"'
# cursor.execute(comando)
# conexao.commit()#Quando precisa editar o banco de dados