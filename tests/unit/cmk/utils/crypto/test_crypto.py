#!/usr/bin/env python3
# Copyright (C) 2022 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from typing import Any, AnyStr

import pytest
from cryptography.hazmat.primitives import hashes

from cmk.utils.crypto import HashAlgorithm, Password


@pytest.mark.parametrize(
    "password",
    [
        "",
        "test 😹",
        "long" * 100,
        b"\xf0\x9f\x98\xb9",
    ],
)
def test_valid_password(password: AnyStr) -> None:
    Password(password)


@pytest.mark.parametrize(
    "password",
    ["\0", b"\0", b"\0".decode()],
)
def test_invalid_password(password: AnyStr) -> None:
    with pytest.raises(ValueError, match="Invalid password"):
        Password(password)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (Password("😹"), Password("😹"), True),
        (Password("😹"), Password(b"\xf0\x9f\x98\xb9"), True),
        (Password("     "), Password(" "), False),
        (Password(""), "", False),
        (Password("123"), 123, False),
    ],
)
def test_password_eq(a: Password, b: Any, expected: bool) -> None:
    assert (a == b) == expected


def test_hash_algorithms_from_cryptography() -> None:
    algo = HashAlgorithm.from_cryptography(hashes.SHA512())
    assert algo == HashAlgorithm.Sha512
    assert algo.name.lower() == hashes.SHA512().name.lower()


def test_hash_algorithms_from_cryptography_unsupported() -> None:
    with pytest.raises(ValueError):
        HashAlgorithm.from_cryptography(hashes.MD5())
