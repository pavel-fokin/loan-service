"""Implements business rules to create loan
"""
import datetime
from collections import defaultdict
from dataclasses import dataclass
from datetime import timedelta
from money.money import Money


class DateError(Exception):
    pass


@dataclass
class Payment:
    amount: Money
    date: datetime.date


class Loan:
    def __init__(
            self, amount: Money, annual_rate: float, start_date
    ):
        self.amount = amount
        self.annual_rate = annual_rate
        self.start_date = start_date

        self.payments = defaultdict(list)

    def add_payment(self, payment: Payment):

        if payment.date < self.start_date:
            raise DateError

        self.payments[payment.date].append(payment)

    def get_balance(self, date) -> Money:

        if date < self.start_date:
            raise DateError

        days_from_start = (date - self.start_date).days
        balance = principal_balance = self.amount

        for day_num in range(1, days_from_start + 1):
            day = self.start_date + day_num * timedelta(days=1)

            interest_per_day = (
                self.annual_rate / 100 / 365 * principal_balance
            )

            balance += interest_per_day
            if day in self.payments:

                for payment in self.payments[day]:
                    balance -= payment.amount

                if balance < principal_balance:
                    principal_balance = balance

        return balance
