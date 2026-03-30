from .cli import CLI, Flags
from .counter import Counter


def main():
    cli = CLI()

    result: list[Counter] = []

    if cli.through_stdin:
        result.append(Counter.from_bytes(cli.content, "stdin"))

    else:
        for filename in cli.filenames:
            with open(filename, "rb") as file:
                result.append(Counter.from_bytes(file.read(), filename))
    
    if len(result) > 1:
        total = Counter(filename="total")
        for res in result:
            total += res
        
        result.append(total)
        
                
    width = max([res.get_width() for res in result])

    for res in result:
        print(
            res.print_res(
                bytes=Flags.BYTES in cli.flags,
                lines=Flags.LINES in cli.flags,
                words=Flags.WORDS in cli.flags,
                characters=Flags.CHARACTERS in cli.flags,
                width=width,
            )
        )
