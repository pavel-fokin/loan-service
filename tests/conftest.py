import pytest

from money.money import Money

from app.utils import str2date
from app.loan import Loan


@pytest.fixture
def start_date():
    return str2date('2019-12-01')


@pytest.fixture
def payment_date():
    return str2date('2019-12-05')


@pytest.fixture
def end_date():
    return str2date('2020-01-01')


@pytest.fixture
def loan(start_date):
    return Loan(Money('1000'), 10, start_date)
