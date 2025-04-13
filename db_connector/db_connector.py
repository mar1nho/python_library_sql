import mysql.connector


def connect():
    try:
        mydb = mysql.connector.connect(
            # O usuário deve ter a permissão de utilizar o banco de dados selecionado.
            host="localhost",  # Ou o endereço IP do seu servidor MySQL
            user="pythonlearning",  # Seu nome de usuário do MySQL
            password="pythondbpassword",  # Sua senha do MySQL
            database="library_python"  # O nome do seu banco de dados
        )
        print("Conexão ao MySQL estabelecida com sucesso!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        exit()


def create_table():
    db_connector = connect()
    cursor = db_connector.cursor()
    try:
        query_create_customer_table = """
            CREATE TABLE IF NOT EXISTS customer(
                id INT AUTO_INCREMENT PRIMARY KEY,
                client_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                isBanned BOOLEAN,
                clientSince DATE    
            )
        """
        cursor.execute(query_create_customer_table)
        db_connector.commit()
        print("Tabela criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar a tabela 'livros': {err}")
        db_connector.rollback()
    finally:
        if 'db_connector' in locals() and db_connector.is_connected():
            db_connector.close()
            cursor.close()
            print("Conexão fechada!")


if __name__ == "__main__":
    create_table()