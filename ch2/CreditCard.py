class CreditCard:
    """ A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.

        The inital balance is zero.

        customer: str, the name of the customer
        bank: str, the name of the bank
        acnt: str, the account identifier
        limit: float, the credit limit (in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return name of the bank."""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number (str)"""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuing sufficient credit limit.

            Return True if charge was processed; False if charge was denied"""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance +=price
            return True

    def make_payment(self, amount):
        """Processes customer payment that reduces balance"""
        self._balance -= amount



class PredatoryCreditCard(CreditCard): #this syntax shows that this class is a CreditCard
    """An extension to CreditCard that compounds interest and has fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

            Inital balance is zero.
            
            apr, float, greater than 0, annual percentage rate. """
        super().__init__(customer, bank, acnt, limit) #call the constructor from CreditCard
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

            Return True if charge was processed.
            Return False and assess $5 fee if charge is denied."""

        success = super().charge(price) #check if it is a success
        if not success:
            self._balance +=5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    val = 17
    print(wallet[0].get_balance())
    wallet[0].charge(val)
    print(wallet[0].get_balance())
    wallet[0].make_payment(5)
    print(wallet[0].get_balance())

#The class isn't entirely robust as of yet - need type checking to prevent make_payment('candy') for instance

