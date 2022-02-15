import os
import click
import pytest
import requests

from utilitiespackage.settings import *


@click.group()
def cli():
    return None

@click.group(name="system")
def system_group():
    return None


@system_group.command(name="version")
def version_command():
    print(VERSION)


@system_group.command(name="selftest")
def selftest_command():
    os.chdir(TESTDIR)
    pytest.main(["-x", "-v", TESTDIR])


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    os.chdir(APPDIR)
    pytest.main([f"--cov-config={COVERAGERC_PATH}", "--cov=utilitiespackage", "--cov-report", "term-missing", APPDIR])

cli.add_command(system_group)
main = cli
