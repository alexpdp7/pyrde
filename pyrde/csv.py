import csv

from pyrde import diagnostics


class CSVDiagnosticListener(diagnostics.DiagnosticListener):
    def __init__(self, destination):
        self.destination = destination
        self.diagnostics = []

    def send(self, diagnostic: diagnostics.Diagnostic):
        self.diagnostics.append(diagnostic)

    def finish(self):
        extra_columns = []
        for diagnostic in self.diagnostics:
            for arg_name in diagnostic.args.keys():
                if arg_name not in extra_columns:
                    extra_columns.append(arg_name)

        writer = csv.DictWriter(self.destination, fieldnames=[
            "message",
            "severity",
            "path",
            "start_line",
            "start_column",
            "end_line",
            "end_column",
            "code",
            "code_url",
        ] + extra_columns)
        writer.writeheader()

        for diagnostic in self.diagnostics:
            row = {
                "severity": diagnostics.SEVERITIES_AS_TEXT[diagnostic.severity],
                "path": diagnostic.path,
                "start_line": diagnostic.start_line,
                "start_column": diagnostic.start_column,
                "end_line": diagnostic.end_line,
                "end_column": diagnostic.end_column,
                "code": diagnostic.code,
                "code_url": diagnostic.code_url,
                "message": diagnostic.format.format(**diagnostic.args),
            }

            for extra_column in extra_columns:
                row[extra_column] = diagnostic.args.get(extra_column)

            writer.writerow(row)
