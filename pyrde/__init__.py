import argparse
import sys

from pyrde import csv
from pyrde import diagnostics

def add_error_format_args(parser: argparse.ArgumentParser):
    parser.add_argument("--error-format", default="text", choices=["text", "csv"])


def get_diagnostic_builder_from_args(args: argparse.Namespace):
    if args.error_format == "csv":
        return diagnostics.DiagnosticBuilder(csv.CSVDiagnosticListener(sys.stdout))
    if args.error_format == "text":
        return diagnostics.DiagnosticBuilder(diagnostics.TextDiagnosticListener())
    assert False, f"unknown error format {args.error_format}"
