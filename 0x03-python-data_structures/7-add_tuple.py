#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    ta_0 = tuple_a[0] if len(tuple_a) >= 1 else 0
    ta_1 = tuple_a[1] if len(tuple_a) >= 2 else 0
    tb_0 = tuple_b[0] if len(tuple_b) >= 1 else 0
    tb_1 = tuple_b[1] if len(tuple_b) >= 2 else 0
    ta = (ta_0, ta_1)
    tb = (tb_0, tb_1)
    return (tuple(map(sum, zip(ta, tb))))
