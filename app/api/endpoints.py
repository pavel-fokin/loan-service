import logging

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response

from app import cases
from . import models

log = logging.getLogger(__name__)   # pylint: disable=invalid-name
router = APIRouter()  # pylint: disable=invalid-name


def get_cases(request: Request) -> cases.Loan:
    return request.app.cases


@router.get('/', include_in_schema=False)
def index():
    return Response("I'm up", media_type='text/plain')


@router.post('/api/loan', response_model=models.LoanInitResponse)
async def init_loan(
        request: models.LoanInitRequest,
        case: cases.Loan = Depends(get_cases)
):
    log.info(request)
    try:
        response = case.init_loan(request)
    except Exception as exc:
        log.error(exc)
        raise HTTPException(status_code=400)
    else:
        log.info(response)
        return response


@router.post('/api/loan/payment', response_model=models.AddPaymentResponse)
async def add_payment(
        request: models.AddPaymentRequest,
        case: cases.Loan = Depends(get_cases)
):
    log.info(request)
    try:
        response = case.add_payment(request)
    except Exception as exc:
        log.error(exc)
        raise HTTPException(status_code=404)
    else:
        log.info(response)
        return response


@router.post('/api/loan/balance', response_model=models.GetBalanceResponse)
async def get_balance(
        request: models.GetBalanceRequest,
        case: cases.Loan = Depends(get_cases)
):
    log.info(request)
    try:
        response = case.get_balance(request)
    except Exception as exc:
        log.error(exc)
        raise HTTPException(status_code=404)
    else:
        log.info(response)
        return response
