import abc
import dataclasses
import sys
import typing

from pyrde import reviewdog_pb2


class Severity:
    ERROR = reviewdog_pb2.Severity.ERROR
    WARNING = reviewdog_pb2.Severity.WARNING
    INFO = reviewdog_pb2.Severity.INFO


SEVERITIES_AS_TEXT = {
    Severity.ERROR: "ERROR",
    Severity.INFO: "INFO",
    Severity.WARNING: "WARNING",
}


@dataclasses.dataclass
class Diagnostic:
    format: str
    args: typing.Dict[str, typing.Any]
    severity: Severity
    path: str
    start_line: int
    start_column: int = None
    end_line: int = None
    end_column: int = None
    code: str = None
    code_url: str = None

    def as_reviewdog_diagnostic(self):
        end = None
        if self.end_line:
            end = reviewdog_pb2.Position(
                line=self.end_line,
                column=self.end_column,
            )
        code_pb = None
        if self.code:
            code_pb = reviewdog_pb2.Code(
                value=self.code,
                url=self.code_url,
            )
        return reviewdog_pb2.Diagnostic(
            message=self.format.format(**self.args),
            location=reviewdog_pb2.Location(
                path=self.path,
                range=reviewdog_pb2.Range(
                    start=reviewdog_pb2.Position(
                        line=self.start_line,
                        column=self.start_column,
                    ),
                    end=end,
                ),
            ),
            severity=self.severity,
            code=self.code_pb,
            # TODO:
            source=None,
            suggestions=None,
            original_output=None
        )


class DiagnosticListener(abc.ABC):
    @abc.abstractmethod
    def send(self, diagnostic: Diagnostic):
        pass

    @abc.abstractmethod
    def finish(self):
        pass


class DiagnosticBuilder:
    def __init__(self, listener: DiagnosticListener):
        self.listener = listener

    def add_diagnostic(
            self,
            format: str,
            args: typing.Dict[str, typing.Any],
            severity: Severity,
            path: str,
            start_line: int,
            start_column: int = None,
            end_line: int = None,
            end_column: int = None,
            code: str = None,
            code_url: str = None,
    ):
        diagnostic = Diagnostic(format, args, severity, path, start_line, start_column, end_line, end_column, code, code_url)
        self.listener.send(diagnostic)

    def finish(self):
        self.listener.finish()


class TextDiagnosticListener(DiagnosticListener):
    def finish(self):
        pass

    def send(self, diagnostic: Diagnostic):
        message = diagnostic.format.format(**diagnostic.args)
        print(f"{SEVERITIES_AS_TEXT[diagnostic.severity]} {diagnostic.path} +{diagnostic.start_line} {message}", file=sys.stderr, flush=True)
