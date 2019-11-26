""" Use case connects business rules with API endpoints
"""
import logging
from dataclasses import dataclass

import app.api.models as api_models
from app.repository import Repository

from . import loan

log = logging.getLogger(__name__)  # pylint:disable=invalid-name


class AddPaymentError(Exception):
    pass


class GetBalanceError(Exception):
    pass


class MissingLoan(Exception):
    pass


@dataclass
class Loan:
    repository: Repository

    def init_loan(self, request):
        new_loan = loan.Loan(
            amount=request.amount,
            annual_rate=request.annual_rate,
            start_date=request.start_date,
        )
        self.repository.add(new_loan)
        return api_models.LoanInitResponse(
            amount=new_loan.amount.amount,
            annual_rate=new_loan.annual_rate,
            start_date=new_loan.start_date,
        )

    def add_payment(self, request):
        current_loan = self.repository.get()
        if current_loan is None:
            raise MissingLoan

        payment = loan.Payment(
            amount=request.amount,
            date=request.date
        )
        try:
            current_loan.add_payment(payment)
        except loan.DateError:
            log.error('Cannot add payment for a date (%s)', request.date)
            raise AddPaymentError
        return api_models.AddPaymentResponse(status='success')

    def get_balance(self, request):
        current_loan = self.repository.get()
        if current_loan is None:
            raise MissingLoan

        try:
            balance = current_loan.get_balance(request.date)
        except loan.DateError:
            log.error('Cannot get balance for a date (%s)', request.date)
            raise GetBalanceError
        return api_models.GetBalanceResponse(amount=balance.amount)
