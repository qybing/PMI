import time
from random import random


def get_hcv():
    """
    计算cookies中的_hc.v
    """
    def n():
        def n():
            return str(hex(int(65536 * (1 + random()))))[3:]
        return '-'.join([n()+n(), n(), n(), n(), n()+n()+n()])
    def i():
        return n() + '.' + str(int(time.time()))
    return i()
print(get_hcv())