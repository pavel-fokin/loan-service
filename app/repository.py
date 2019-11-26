""" Repository to store and access loans
"""


class Repository:

    def __init__(self):
        self._loan = None

    def add(self, loan):
        self._loan = loan

    def get(self):
        return self._loan

    def is_empty(self):
        return self._loan is None
