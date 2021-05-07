#!/usr/bin/python3
"""
    Module for calling numpy matmul
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """  Function to call numpy matmul and return result """
    return np.matmul(m_a, m_b)
