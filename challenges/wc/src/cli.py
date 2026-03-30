import sys
from enum import Enum


class Flags(str, Enum):
    BYTES = "c"
    LINES = "l"
    WORDS = "w"
    CHARACTERS = "m"


class CLI:
    def __init__(self) -> None:
        self._args: list[str] = sys.argv[1:]
        self._flags: list[Flags] = []
        self._filenames: list[str] = []
        self._content: bytes | None = None
        self._stdin: bool = False

        self._get_content()

    def _get_content(self):
        for arg in self._args:
            if arg.startswith("-"):
                for ch in arg[1:]:
                    if ch not in Flags._value2member_map_:
                        continue
                    self._flags.append(Flags(ch))

            else:
                self._filenames.append(arg)

        if not len(self._flags):
            self._flags.extend([Flags.BYTES, Flags.LINES, Flags.WORDS])

        if not len(self._filenames):
            self._content = sys.stdin.buffer.read()
            self._stdin = True

    @property
    def flags(self) -> list[Flags]:
        return self._flags

    @property
    def filenames(self) -> list[str]:
        return self._filenames

    @property
    def through_stdin(self) -> bool:
        return self._stdin

    @property
    def content(self) -> bytes:
        if not self._content:
            raise ValueError("There is no content")
        return self._content
