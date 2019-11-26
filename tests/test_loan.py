from money.money import Money

from app.loan import Payment
from app.utils import str2date


def test_get_balance(loan):
    assert loan.get_balance(str2date('2020-12-01')) == Money('1098.82')


def test_add_payment(loan):
    loan.add_payment(Payment(amount=Money('110'), date=str2date('2020-01-01')))
    assert loan.get_balance(str2date('2020-01-01')) == Money('898.37')
