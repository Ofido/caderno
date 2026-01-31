from contextlib import contextmanager
from dataclasses import dataclass
from functools import lru_cache
from io import TextIOWrapper
from typing import Any, Generator


@contextmanager
def arquivo_temporario() -> Generator[TextIOWrapper, Any, None]:
    f = open("temp.txt", "w")
    try:
        yield f
    finally:
        f.close()


@dataclass
class Produto:
    nome: str
    preco: float


@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
