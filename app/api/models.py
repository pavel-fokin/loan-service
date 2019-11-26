""" Request/response API models
"""
import datetime

from money.money import Money
from pydantic import BaseModel, validator


def _validate_amount(amount):
    if amount == 0:
        raise ValueError('Amount cannot be zero')
    if amount < 0:
        raise ValueError('Amount cannot be negative')


class LoanInitRequest(BaseModel):
    amount: float
    annual_rate: float
    start_date: datetime.date

    @validator('amount')
    def validate_amount(cls, val):
        _validate_amount(val)
        return Money(str(val))


class LoanInitResponse(BaseModel):
    amount: str
    annual_rate: float
    start_date: datetime.date


class AddPaymentRequest(BaseModel):
    amount: float
    date: datetime.date

    @validator('amount')
    def validate_amount(cls, val):
        _validate_amount(val)
        return Money(str(val))


class AddPaymentResponse(BaseModel):
    status: str


class GetBalanceRequest(BaseModel):
    date: datetime.date


class GetBalanceResponse(BaseModel):
    amount: float
