class Invoice:
    __currency = "USD"

    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def setCurrency(cls, currency):
        cls.__currency = currency
    @classmethod
    def getCurrency(cls):
        return cls.__currency

if __name__ == '__main__':
    invoice1 = Invoice(100)
    invoice2 = Invoice(200)
    print(f"Invoice 1: {invoice1.amount} {Invoice.getCurrency()}")
    print(f"Invoice 2: {invoice1.amount} {Invoice.getCurrency()}")
    Invoice.setCurrency("EUR")
    print(f"Invoice 1: {invoice1.amount} {Invoice.getCurrency()}")
    print(f"Invoice 2: {invoice1.amount} {Invoice.getCurrency()}")
