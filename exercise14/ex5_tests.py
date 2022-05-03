from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
import pytest

def is_prime(n: int) -> bool:
  if n == 2:
      return True
  elif n < 2 or n % 2 == 0:
      return False
  else:
      x = math.floor(math.sqrt(n)) + 1
      i = 3
      while i < x:
          if n % i == 0:
              return False
          i += 2
      return True

## Aufgabe 5 (Tests) ###########################################################

def test_is_prime():
    n = 2
    assert is_prime(n) == True
    n = 1 
    assert is_prime(n) == False
    n = 4
    assert is_prime(n) == False
    n = 8
    assert is_prime(n) == False
    n = 3
    assert is_prime(n) == True
    n = 9
    assert is_prime(n) == False
    n = 15
    assert is_prime(n) == False
    n = 7673
    assert is_prime(n) == True