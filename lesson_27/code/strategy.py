from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} с помощью кредитной карты.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} с помощью PayPal.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} с помощью банковского перевода.")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)

# Использование
context = PaymentContext(CreditCardPayment())
context.pay(100)  # Оплата 100 с помощью кредитной карты.

context = PaymentContext(PayPalPayment())
context.pay(50)   # Оплата 50 с помощью PayPal.