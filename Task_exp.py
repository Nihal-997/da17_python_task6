class SalesCompany:
    company_name = 'initial_company'
    company_id = 0

    def __init__(self, company_name, company_id):
        print('SalesCompany init called')
        self.company_name = company_name
        self.company_id = company_id

    def getCompanyInfo(self):
        return self.company_name + ' - ' + str(self.company_id)


class Product(SalesCompany):  # Product inherits from SalesCompany
    product_id = 0
    product_name = 'initial_product'
    product_category = 'not_assigned'

    def __init__(self, product_id, product_name, company_name, company_id):
        print('Product init called')
        super().__init__(company_name, company_id)
        self.product_id = product_id
        self.product_name = product_name


class Customer(SalesCompany):  # Customer also inherits from SalesCompany
    customer_name = 'anonymous_customer'
    customer_id = 0

    def __init__(self, customer_name, customer_id, company_name, company_id):
        print('Customer init called')
        super().__init__(company_name, company_id)
        self.customer_name = customer_name
        self.customer_id = customer_id



company_name = 'Tesla Inc.'
company_id = 501


prod1 = Product(1001, 'CyberTruck', company_name, company_id)
print('----- Product Info -----')
print('Product ID:', prod1.product_id)
print('Product Name:', prod1.product_name)
print('Product Category:', prod1.product_category)
print('Company Name:', prod1.company_name)
print('Company Info:', prod1.getCompanyInfo())


cust1 = Customer('Elon Musk', 301, company_name, company_id)
print('----- Customer Info -----')
print('Customer Name:', cust1.customer_name)
print('Customer ID:', cust1.customer_id)
print('Company ID:', cust1.company_id)
print('Company Name:', cust1.company_name)
print('Company Info:', cust1.getCompanyInfo())