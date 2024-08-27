import psycopg
#print (psycopg)
class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe(usuario):
    #Abrir conexão com o PostgreSQL
    with psycopg.connect(host = "localhost",
                        dbname = "20242_fatec_ipi_pdbi_stephanie",
                        user = "postgres",
                        password = "123456"
    ) as conexao:
    #Por meio da conexão, obter uma abstração do tipo cursor
      with conexao.cursos() as cursor:
        #Por meio do cursor, executar um comando SELECT
        cursor.execute( #in-place
                        'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s', 
                       (usuario.login, usuario.senha)
        )
        #Usar um método do cursor para verificar o resultado produzido pelo SELECT
        result = cursor.fetchone()
        #Devolver True ou False, conforme o resultado.
        return result != None
        '''return True if result != None else False'''
        '''if result != None:
            return True
        return False'''