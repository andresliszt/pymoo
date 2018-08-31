import numpy as np

from decomposition import cython_pbi
from pymoo.util.mathematics import Mathematics


def decompose(F, weights, method, **kwargs):
    if method == "pbi":
        return pbi(F, weights, **kwargs)
    elif method == "cython_pbi":
        return cython_pbi(F, weights, **kwargs)


def pbi(F, weights, ideal_point, theta=0.1, **kwargs):
    d1 = np.linalg.norm((F - ideal_point) * weights, axis=1) / np.linalg.norm(weights)
    d2 = np.linalg.norm(F - (ideal_point - d1[:,None] * weights), axis=1)
    return d1 + theta * d2


def moead(F, weights, ideal_point, alpha=0.1, **kwargs):
    v = (F - ideal_point) * (1 / F.shape[1] + alpha * weights)
    return np.max(v, axis=1)


def tchebi(F, weights, ideal_point, **kwargs):
    v = np.abs((F - ideal_point - Mathematics.EPS) * weights)
    return np.max(v, axis=1)


def weighted_sum(F, weights, **kwargs):
    return np.sum(F * weights, axis=1)
