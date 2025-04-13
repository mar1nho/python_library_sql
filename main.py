import db.customer_queries as queries
from db.models.Customer import Customer
from db import db_configurator as db_connector



if __name__ == '__main__':
    # customer_01 = Customer(None, 'Marinho', 'gustavomarinhosom@gmail.com', False, '2025-01-02')
    # queries.insert_customer_data(connector, customer_01)
    connector = db_connector.connect()
    allcustomers = queries.find_all_customers(connector)
    for customer in allcustomers:
        print(f'Customer {customer} successfully found in Database')


