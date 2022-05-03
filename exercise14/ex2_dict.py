from   dataclasses import dataclass
from   typing      import Any, Optional, Union
import math
# import pytest

## Aufgabe 2 (Dict) ############################################################

def cluster_by_points(points):
    result = {}
    for item in sorted(points.values()):
        value = item / 10 
        result.update({math.floor(value) * 10 : []})
    
    for item in points:
        value2 = points[item] / 10
        for el in result:
            if math.floor(value2) * 10 == el:
                result[el].append(item)
        # if floor(value) in for el in result:
        #     print('yes')
    sorted(result)  
    return result


if __name__ == "__main__":
    points = {"Line": 9, "Daniel": 12, "Charlotte": 15, "Frank": 30}
    print(cluster_by_points(points))