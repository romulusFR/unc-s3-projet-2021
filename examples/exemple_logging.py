"""Exemple d'utilisation de la bibliothèque logging"""

# pylint: disable=logging-fstring-interpolation

#%%
import logging

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def primes(n: int):
    """Calcule les n premiers nombres premiers"""
    if n < 1:
        s = f"n doit être positif (n={n})"
        logger.error(s)
        raise ValueError(s)
    logger.info(f"primes({n})")
    res = [2, 3]
    i = 5
    while len(res) < n:
        logger.debug(f"i={i}, len(res)={len(res)}")
        divisible = False
        for d in res:
            logger.debug(f"\td={d}")
            if i % d == 0:
                divisible = True
                break
        if not divisible:
            res.append(i)
        i += 2
    return res[:n]


# assert primes(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
