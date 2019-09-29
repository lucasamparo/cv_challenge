import numpy as np
from model.StarModel import StarModel

def findBlackHole(number, coordenates):
    success = []
    cases = np.split(np.array(coordenates), number)
    for i, case in enumerate(cases):
        star_1 = StarModel(case[0], case[2])
        star_2 = StarModel(case[1], case[3])
        position_black_hole = star_1.get_line().intersection(star_2.get_line())[0]
        msg = "Caso {0}#: ({1:.2f},{2:.2f})".format(i+1, float(position_black_hole[0]), float(position_black_hole[1]))
        success.append(msg)
    return success