# 1
from datetime import datetime


class Email:
    """
        Simple email model with custom object behavior.
    """
    def __init__(self, sender, recipient, subject, body, time):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = time

    def __str__(self):
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body}-"
        )

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())

    def __gt__(self, other):
        return self.date > other.date




e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

print(e1)
print()

print(e2)
print()

print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)


# 2


class Money:
    """
        Simple money class with arithmetic operations.
    """
    def __init__(self, amount):
        self.amount = amount
        self.currency = 0

    def __str__(self):
        return f"${self.amount}"

    def __add__(self, other):
        return Money(other.amount + self.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        if result < 0:
            result = 0
        return Money(result)



money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)