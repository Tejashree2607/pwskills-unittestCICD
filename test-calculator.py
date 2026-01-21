import pytest
from calculator import add,divide

def testadd():
    #Assert -> Assertion(condition) => Putput result
    assert add(2,3) == 5

def testadd2():
    #False case
    assert add(2,2) == 5