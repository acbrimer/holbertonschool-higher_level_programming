#!/usr/bin/python3
"""
   Matrix mul module
"""


def matrix_mul(m_a, m_b):
    """
       Function to multiply two matricies when
       pip issues prevent you from installing numpy
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(list(filter(lambda i: not isinstance(i, list), m_a))) > 0:
        raise TypeError("m_a must be a list of lists")
    if len(list(filter(lambda i: not isinstance(i, list), m_b))) > 0:
        raise TypeError("m_b must be a list of lists")
    if m_a is None or m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b is None or m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for r in m_a:
        for v in r:
            if not isinstance(v, (int, float)):
                raise ValueError("m_a should contain only integers or floats")
    for r in m_b:
        for v in r:
            if not isinstance(v, (int, float)):
                raise ValueError("m_b should contain only integers or floats")
    if max(map(lambda i: len(i), m_a)) != min(map(lambda i: len(i), m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if max(map(lambda i: len(i), m_b)) != min(map(lambda i: len(i), m_b)):
        raise TypeError("each row of m_b must be of the same size")
    try:
        w = (len(m_a) + (0, 1)[len(m_a) == 1])
        m_c = [(['x'] * w) for b in range(len(m_b[0]))]
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                s = 0
                for k in range(len(m_a[0])):
                    s += (m_a[i][k] * m_b[k][j])
                m_c[i][j] = s
        return list(filter(lambda r: r != (['x'] * w), m_c))
    except:
        raise ValueError("m_a and m_b can't be multiplied")
