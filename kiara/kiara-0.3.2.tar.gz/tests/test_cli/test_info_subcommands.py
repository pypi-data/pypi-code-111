# -*- coding: utf-8 -*-

#  Copyright (c) 2021, University of Luxembourg / DHARPA project
#
#  Mozilla Public License, version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)

import json
from click.testing import CliRunner

from kiara.interfaces.cli import cli


def test_info():

    runner = CliRunner()

    result = runner.invoke(cli, "info --json")

    assert "table.query.sql" in result.stdout
    json.loads(result.stdout)
