import csv
import sys

import pyrde
from pyrde import reviewdog_pb2


class CSVDiagnosticListener(pyrde.DiagnosticListener):
    def __init__(self, destination):
        self.writer = csv.DictWriter(destination, fieldnames=[
            "message",
            "severity",
            "path",
            "start_line",
            "start_column",
            "end_line",
            "end_column",
            "code",
            "code_url",
        ])
        self.writer.writeheader()

    def send(self, diagnostic: reviewdog_pb2.Diagnostic):
        self.writer.writerow({
            "message": diagnostic.message,
            "severity": diagnostic.severity,
            "path": diagnostic.location.path,
            "start_line": diagnostic.location.range.start.line,
            "start_column": diagnostic.location.range.start.column,
            "end_line": diagnostic.location.range.end.line if diagnostic.location.range.end else None,
            "end_column": diagnostic.location.range.end.column if diagnostic.location.range.end else None,
            "code": diagnostic.code.value if diagnostic.code else None,
            "code_url": diagnostic.code.url if diagnostic.code else None,
        })
