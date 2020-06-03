# Digant Kumar

# A simple Credit Card program which keeps tracks of the customer payments, transactions etc.
class CreditClass:
    all_card_info = {}

    def __init__(self,name,bank_name,acc_num,upper_limit,balance):
        self.name = name
        self.bank_name = bank_name
        self.acc_num = acc_num
        self.upper_limit = upper_limit
        self.balance = balance
        CreditClass.all_card_info[self.acc_num] = [self.name, self.bank_name, self.balance]       # Keeping count of the customers

    def show_summary(self):
        new_dict = sorted(CreditClass.all_card_info.values())        # Sorting by name (alphabetically)
        print("%6s %6s %8s" %("Name","Bank","Balance"))
        for customer in new_dict:
            print("%6s %6s %6s" %(customer[0],customer[1],customer[2]))

    def get_balance(self):                   # Getter functions for returning the balance,name,bank name etc.
        return self.balance
    def get_name(self):
        return self.name
    def get_bankname(self):
        return self.bank_name
    def get_limit(self):
        return self.upper_limit
    def get_balance(self):
        return self.balance

    def charge(self,price):              # If amount to be deducted makes the account balance less than the limit, the transaction is cancelled
        if (self.balance - price) < self.upper_limit:                          # if successful, shows the updated balance
            print("Insufficient amounts")
        else:
            print("Payment successful")
            self.balance = self.balance - price
            return self.balance

    def make_payment(self,amount):                # Credits the account balance by the given amount.
        self.balance = self.balance + amount
        print("Payment successful")
        return self.balance
