from   dataclasses import dataclass
from   typing      import Any, Optional, Union
# import math
# import pytest

## Aufgabe 3 (Strings) #########################################################

def is_strong(pw):
    zz = ["!", "?", "+", "*"]
    if len(pw) <= 8:
        return False
    digits = 0
    s_sym = 0
    alpha = 0
    for el in pw:
        if el.isdigit() == True:
            digits += 1
            continue
        if el.isupper() == True:
            alpha += 1
            continue
        if el in zz:
            s_sym += 1
            continue

    match digits:
        case 0:
            return False
        case digits if digits <= 3:
            if s_sym < 1:
                return False

    match alpha:
        case alpha if alpha < 3 and digits <= 3 and s_sym == 1:
            return False
        
    return True

if __name__ == "__main__":
    print(is_strong("12345678AA??"))