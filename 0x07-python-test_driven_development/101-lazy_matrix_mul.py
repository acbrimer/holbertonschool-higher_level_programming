#!/usr/bin/python3
import numpy as np


""" Module for calling numpy matmul """


def lazy_matrix_mul(m_a, m_b):
    """  Function to call numpy matmul and return result """
    return np.matmul(m_a, m_b)
