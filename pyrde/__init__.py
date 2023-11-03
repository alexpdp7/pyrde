import abc
import argparse


from pyrde import reviewdog_pb2


class Severity:
    ERROR = reviewdog_pb2.Severity.ERROR
    WARNING = reviewdog_pb2.Severity.WARNING
    INFO = reviewdog_pb2.Severity.INFO


class DiagnosticListener(abc.ABC):
    @abc.abstractmethod
    def send(self, diagnostic: reviewdog_pb2.Diagnostic):
        pass


class DiagnosticBuilder:
    def __init__(self, listener: DiagnosticListener):
        self.listener = listener

    def add_diagnostic(
            self,
            message: str,
            severity: Severity,
            path: str,
            start_line: int,
            start_column: int = None,
            end_line: int = None,
            end_column: int = None,
            code: str = None,
            code_url: str = None,
    ):
        end = None
        if end_line:
            end = reviewdog_pb2.Position(
                line=end_line,
                column=end_column,
            )
        code_pb = None
        if code:
            code_pb = reviewdog_pb2.Code(
                value=code,
                url=code_url,
            )
        diagnostic = reviewdog_pb2.Diagnostic(
            message=message,
            location=reviewdog_pb2.Location(
                path=path,
                range=reviewdog_pb2.Range(
                    start=reviewdog_pb2.Position(
                        line=start_line,
                        column=start_column,
                    ),
                    end=end,
                ),
            ),
            severity=severity,
            code=code_pb,
            # TODO:
            source=None,
            suggestions=None,
            original_output=None
        )
        self.listener.send(diagnostic)
