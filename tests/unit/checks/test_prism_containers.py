#!/usr/bin/env python3
# Copyright (C) 2023 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest

from tests.testlib import Check

from .checktestlib import assertCheckResultsEqual, BasicCheckResult, CheckResult, PerfValue

pytestmark = pytest.mark.checks


def test_fileinfo_min_max_age_levels() -> None:
    check = Check("prism_containers")

    item = "prism-item"
    parsed = check.run_parse(
        [
            ["name", "usage", "capacity"],
            ["prism-item", "5", "10"],
        ]
    )

    output_expected = [
        BasicCheckResult(
            0,
            "Total: 10 B",
        ),
        BasicCheckResult(
            1,
            "Used: 5 B (warn/crit at 4 B/6 B)",
            [
                PerfValue("fs_used", 5, 4, 6, None, None),
            ],
        ),
    ]

    # percent levels
    output_perc_levels = check.run_check(item, {"levels": (40.0, 60.0)}, parsed)
    assertCheckResultsEqual(
        CheckResult(output_perc_levels),
        CheckResult(output_expected),
    )

    # absolute levels
    output_abs_levels = check.run_check(item, {"levels": (4, 6)}, parsed)
    assertCheckResultsEqual(
        CheckResult(output_abs_levels),
        CheckResult(output_expected),
    )
