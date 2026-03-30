from __future__ import annotations

from dataclasses import dataclass


def count_bytes(content: bytes) -> int:
    return len(content)


def count_lines(content: bytes) -> int:
    return content.count(b"\n")


def count_words(content: bytes) -> int:
    text = content.decode("utf-8", errors="ignore")
    return len(text.split())


def count_characters(content: bytes) -> int:
    text = content.decode("utf-8", errors="ignore")
    return len(text)


@dataclass
class Counter:
    filename: str
    BYTES: int = 0
    LINES: int = 0
    WORDS: int = 0
    CHARACTERS: int = 0

    @classmethod
    def from_bytes(cls, content: bytes, name: str) -> Counter:
        return cls(
            filename=name,
            BYTES=count_bytes(content),
            LINES=count_lines(content),
            WORDS=count_words(content),
            CHARACTERS=count_characters(content),
        )
    
    def __add__(self, other: Counter) -> Counter:
        self.BYTES += other.BYTES
        self.LINES += other.LINES
        self.WORDS += other.WORDS
        self.CHARACTERS += other.CHARACTERS
        return self
    
    def get_width(self) -> int:
        return max([len(str(self.BYTES)), len(str(self.CHARACTERS)), len(str(self.LINES)), len(str(self.WORDS))])

    def print_res(
        self, bytes: bool, lines: bool, words: bool, characters: bool, width: int
    ) -> str:
        res = []

        if lines:
            res.append(f"{self.LINES:>{width}}")
        if words:
            res.append(f"{self.WORDS:>{width}}")
        if characters:
            res.append(f"{self.CHARACTERS:>{width}}")
        if bytes:
            res.append(f"{self.BYTES:>{width}}")

        res.append(f"{self.filename}" if self.filename != "stdin" else "")

        return " ".join(res)
