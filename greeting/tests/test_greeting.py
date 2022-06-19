import pytest
from lib.greeting import greeting

class Test_greeting:
    def  test_greet(self):
        greet = greeting("World")
        assert greet == "World"