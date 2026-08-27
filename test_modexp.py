import random
import pytest
from modexp import mod_pow, mod_inverse


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

def test_known_case_from_hand_trace():
    # From the worked example: extended_gcd(17, 5) -> x = -2, so
    # mod_inverse(17, 5) should be -2 % 5 = 3
    assert mod_inverse(17, 5) == 3
    # and check it actually satisfies e * d ≡ 1 (mod phi_n)
    assert (17 * mod_inverse(17, 5)) % 5 == 1
 
 
def test_small_hand_pickable_cases():
    cases = [
        (3, 11),   # small coprime pair
        (7, 40),   # RSA-flavoured: e=7, phi_n=40 (e.g. p=5, q=11)
        (17, 3120),  # e=17 against a slightly bigger phi_n
    ]
    for e, phi_n in cases:
        d = mod_inverse(e, phi_n)
        assert (e * d) % phi_n == 1, f"mod_inverse({e}, {phi_n}) = {d} failed check"
        assert 0 <= d < phi_n, f"mod_inverse({e}, {phi_n}) = {d} not reduced into range"
 
 
def test_random_coprime_pairs():
    random.seed(0)
    count = 0
    while count < 100:
        phi_n = random.randint(2, 100_000)
        e = random.randint(2, phi_n - 1)
        if __import__("math").gcd(e, phi_n) != 1:
            continue  # skip non-coprime pairs, try another
        d = mod_inverse(e, phi_n)
        assert (e * d) % phi_n == 1, f"mod_inverse({e}, {phi_n}) = {d} failed check"
        count += 1
 
 
def test_non_coprime_raises_value_error():
    # gcd(6, 9) = 3, not 1 -> no inverse should exist
    with pytest.raises(ValueError):
        mod_inverse(6, 9)
 
    # gcd(10, 15) = 5, not 1
    with pytest.raises(ValueError):
        mod_inverse(10, 15)