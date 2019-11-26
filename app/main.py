import logging

from fastapi import FastAPI

from . import __version__, api, cases, repository

log = logging.getLogger(__name__)   # pylint: disable=invalid-name


def create_app():
    app = FastAPI(  # pylint: disable=invalid-name
        title='Toy Loan Simulator',
        description='Simple loan simulator',
        version=__version__,
    )
    app.include_router(api.router)
    app.repository = repository.Repository()
    app.cases = cases.Loan(app.repository)
    return app


app = create_app()
