"""
CP1404 - programming language class
"""


class ProgrammingLanguage:

    def __init__(self, typing, reflection, _year):
        self.typing = typing
        self.reflection = reflection
        self._year = _year

    def is_dynamic(self):
        if self.typing == 'dynamic':
            return True
        else:
            return False
