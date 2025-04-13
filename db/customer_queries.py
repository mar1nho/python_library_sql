import mysql

def insert_customer_data(connector, customer):
    table_name = "customer"
    if connector:
        cursor = connector.cursor()
        try:
            name = customer.client_name
            email = customer.email
            is_banned = customer.is_banned
            client_since = customer.client_since

            query = f"INSERT INTO {table_name}(client_name, email, is_banned, client_since) VALUES(%s, %s, %s, %s)"
            values = (name, email, is_banned, client_since)
            cursor.execute(query, values)
            connector.commit()
            print(f'Customer {name} inserted successfully into Database')
        except mysql.connector.Error as error:
            print(f'Error while inserting customer {customer.client_name} data, error: {error}')
            connector.rollback()
        finally:
            cursor.close()
    else:
        print('Database connection failed.')
