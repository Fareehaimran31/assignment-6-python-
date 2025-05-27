class Bank:
    bank_name = "National Bank of Pakistan"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()

print(b1.bank_name)
Bank.change_bank_name("Bank Alfalah")
print(b1.bank_name)