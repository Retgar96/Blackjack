from dataclasses import dataclass


@dataclass(frozen=True)
class Сard:
    name: str
    value: int


template = [
     Сard(name='A', value=11),
     Сard(name='2', value=2),
     Сard(name='3', value=3),
     Сard(name='4', value=4),
     Сard(name='5', value=5),
     Сard(name='6', value=6),
     Сard(name='7', value=7),
     Сard(name='8', value=8),
     Сard(name='9', value=9),
     Сard(name='10', value=10),
     Сard(name='J', value=10),
     Сard(name='D', value=10),
     Сard(name='K', value=10),
]