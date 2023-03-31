BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text = text[start:]
    if len(text) < size:
        return (text, len(text))
    while text[size] != ' ':
        size -= 1
    s = text[:size]
    while not s[-1].endswith(tuple(',!:;?.')):
        s = s[:-1]
    return (s, len(s))


def prepare_book(path: str) -> None:
    start = 0
    key = 1
    with open(path) as b:
        b = b.read()
        while b[start:]:
            text, count = _get_part_text(b, start, PAGE_SIZE)
            book[key] = text.lstrip()
            key += 1
            start += count


prepare_book(BOOK_PATH)
