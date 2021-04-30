from pathlib import Path
from typing import Generator

DATA_DIR = Path(__file__).resolve().parent.parent/"data"

# ETL: Extract, Transform, Load
def read_data(file_name: str) -> Generator:
    # große Datei einlesen
    with open(DATA_DIR / 'techcrunch.csv') as f:
        for line in f:
            yield line


def dictify(g: Generator):
    header = next(g)
    return (dict(zip(header, line)) for line in g)



def split_line(g: Generator) -> Generator:
    result = (line.strip().split(",") for line in g)

    return result


def load_data(file_name: str) -> Generator:
    file_generator = read_data(file_name)
    split_lines = split_line(file_generator)
    return dictify(split_lines)



if __name__ == '__main__':
    load_data('techcrunch.csv')


# Wir wollen einen Dictionary über jeden Header des Textes als Key erstellen