class Invoice:
    """Class to represent Invoice"""

    # Constructor:
    def __init__(self, date, amount, client, payment_method):
        self.date = date
        self.amount = amount
        self.client = client
        self.payment_method = payment_method


    #Setter Getter functions:
    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date


    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount


    def set_client(self, client):
        self.client = client

    def get_client(self):
        return self.client


    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def get_payment_method(self):
        return self.payment_method


    #Function to generate invoice:
    def generate_invoice(self):
        print(f"Invoice generated for {self.client._name} on {self.date} with amount {self.amount}.")

