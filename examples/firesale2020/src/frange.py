# def frange(x, y, jump):
# 	while x < y:
# 		yield x
# 		x += jump


import itertools
def frange(start, end=None, inc=0.1):
    "An xrange-like generator which yields float values"
    # imitate range/xrange strange assignment of argument meanings
    if end is None:
        end = start + 0.0     # Ensure a float value for 'end'
        start = 0.0
    assert inc                # sanity check
    for i in itertools.count( ):
        next = start + i * inc
        if (inc>0.0 and next>=end) or (inc<0.0 and next<=end):
            break
        yield next