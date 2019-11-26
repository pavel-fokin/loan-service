# pylint: disable=redefined-outer-name
import pytest

from money.money import Money
from starlette.testclient import TestClient
from app.utils import str2date

from app.loan import Loan, Payment
from app.main import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return TestClient(app)


@pytest.fixture
def loan():
    return Loan(Money('1000'), 13, str2date('2019-11-23'))


@pytest.fixture
def payment():
    return Payment(Money('1000'), str2date('2020-01-01'))


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_init_loan_success(client):
    payload = {
        'amount': 1000,
        'annual_rate': 13.0,
        'start_date': '2019-11-23',
    }
    resp = client.post('/api/loan', json=payload)

    assert resp.status_code == 200

    resp_payload = resp.json()
    assert resp_payload['amount'] == '1000.0'
    assert resp_payload['annual_rate'] == 13
    assert resp_payload['start_date'] == '2019-11-23'


def test_add_payment_success(client, app, loan):
    app.repository.add(loan)
    payload = {
        'amount': '1000',
        'date': '2020-01-01'
    }
    resp = client.post('/api/loan/payment', json=payload)
    assert resp.status_code == 200

    resp_payload = resp.json()
    assert resp_payload['status'] == 'success'


def test_add_payment_fail(client):
    payload = {
        'amount': '1000',
        'date': '2020-01-01'
    }
    resp = client.post('/api/loan/payment', json=payload)
    assert resp.status_code == 404


def test_get_balance_fail(client):
    payload = {
        'date': '2020-01-01'
    }
    resp = client.post('/api/loan/balance', json=payload)
    assert resp.status_code == 404


def test_get_balance_success(client, app, loan, payment):
    app.repository.add(loan)
    loan.add_payment(payment)
    payload = {
        'date': '2020-01-01'
    }
    resp = client.post('/api/loan/balance', json=payload)
    assert resp.status_code == 200

    resp_payload = resp.json()
    assert resp_payload['amount'] == 14.04
