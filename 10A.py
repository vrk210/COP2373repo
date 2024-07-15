class Money:
    def __init__(self, amount: float):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount
        return NotImplemented

    def __str__(self):
        return f"${self.amount:.2f}"

    def __repr__(self):
        return f"Money(amount={self.amount})"

    def test_money_operations():
        m1 = Money(50.00)
        m2 = Money(20.00)
        m3 = Money(30.00)

        # Test addition
        assert (m1 + m2) == Money(70.00), "Addition Test Failed"
        assert (m2 + m3) == Money(50.00), "Addition Test Failed"

        # Test subtraction
        assert (m1 - m2) == Money(30.00), "Subtraction Test Failed"
        assert (m2 - m3) == Money(-10.00), "Subtraction Test Failed"

        # Test multiplication
        assert (m1 * 2) == Money(100.00), "Multiplication Test Failed"
        assert (3 * m2) == Money(60.00), "Multiplication Test Failed"

        print("All tests passed.")

    # Run the test function
    test_money_operations()

