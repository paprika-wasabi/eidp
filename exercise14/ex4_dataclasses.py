from   dataclasses import dataclass
from   typing      import Any, Optional, Union
# import math
# import pytest

## Aufgabe 4 (Dataclasses) #####################################################

@dataclass
class Ranking:
    club: str
    wins: int
    draws: int
    losses: int
    goals_achieved: int
    goals_conceded: int

    def show(self):
        return self.club +" "+ str(self.wins + self.draws + self.losses) +" "+str(self.wins) +" "+ str(self.draws) +" "+ str(self.losses) +" "+ str(self.goals_achieved) + ":" + str(self.goals_conceded) +" " + str(self.goals_achieved - self.goals_conceded) + " " + str(self.wins*3 + self.draws)


    def table_entry(self):
        return self.show()


    def __lt__(self, other):
        punkte = self.wins*3 + self.draws
        o_p = other.wins*3 + other.draws
        goals_dif_s = self.goals_achieved - self.goals_conceded
        goals_dif_o = other.goals_achieved - other.goals_conceded
        if punkte < (o_p):
            return True
        elif punkte == (o_p):
            if goals_dif_s < goals_dif_o:
                return True
            elif goals_dif_s == goals_dif_o:
                if self.wins < other.wins:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    r1 = Ranking("FC H.", 6, 2, 2, 23, 14)
    r2 = Ranking("FC U.", 5, 3, 2, 20, 15)
    print(r1.table_entry())
    print(r2.table_entry())
    print(r2 < r1)
    print(r1 < r1)