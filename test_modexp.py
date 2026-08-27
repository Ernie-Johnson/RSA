import random
from modexp import mod_pow


def test_matches_builtin_pow_small_cases():
    cases = [
        (5, 3, 7),
        (2, 10, 1000),
        (7, 0, 13),      # exp = 0 should give 1
        (10, 1, 7),      # exp = 1 should give base % mod
        (3, 4, 5),
        (100, 2, 7),     # base > mod
    ]
    for base, exp, mod in cases:
        expected = pow(base, exp, mod)
        actual = mod_pow(base, exp, mod)
        assert actual == expected, (
            f"mod_pow({base}, {exp}, {mod}) = {actual}, expected {expected}"
        )


def test_matches_builtin_pow_random_cases():
    random.seed(0)  # reproducible failures
    for _ in range(200):
        base = random.randint(0, 10_000)
        exp = random.randint(0, 10_000)
        mod = random.randint(1, 10_000)
        expected = pow(base, exp, mod)
        actual = mod_pow(base, exp, mod)
        assert actual == expected, (
            f"mod_pow({base}, {exp}, {mod}) = {actual}, expected {expected}"
        )


def test_large_key_sized_numbers():
    # Roughly RSA-key-sized numbers, to sanity check performance and
    # correctness at the scale this function is actually meant for.
    base = random.randint(2, 2**2048)
    exp = random.randint(2, 2**2048)
    mod = random.randint(3, 2**2048) | 1  # ensure odd, nonzero
    assert mod_pow(base, exp, mod) == pow(base, exp, mod)