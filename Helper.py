def getOppositeSign(sign:int):
    if sign==0:
        return 1
    elif sign==1:
        return 0
    else:
        raise ValueError("Invalid sign value given")

def getOppositeSide(side:int):
    if side==0:
        return 1
    elif side==1:
        return 0
    else:
        raise ValueError("Invalid side value given")