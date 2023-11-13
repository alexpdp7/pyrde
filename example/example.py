import argparse
import pathlib
import sys

import pyrde
from pyrde import diagnostics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="*", type=pathlib.Path)
    pyrde.add_error_format_args(parser)
    args = parser.parse_args()
    db = pyrde.get_diagnostic_builder_from_args(args)

    errors = False

    for file in args.file:
        content = file.read_text()
        bad_lines = [(number, line) for number, line in enumerate(content.splitlines()) if "foo" in line]
        for number, line in bad_lines:
            db.add_diagnostic("Line '{line}' contains foo", {"line": line}, diagnostics.Severity.ERROR, file, number, None, None, None, "BAD_LINE", None)
            errors = True

    db.finish()

    if errors:
        sys.exit(1)
