from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    name: str
    value: int


template = {
    Card(name='A', value=11),
    Card(name='2', value=2),
    Card(name='3', value=3),
    Card(name='4', value=4),
    Card(name='5', value=5),
    Card(name='6', value=6),
    Card(name='7', value=7),
    Card(name='8', value=8),
    Card(name='9', value=9),
    Card(name='10', value=10),
    Card(name='J', value=10),
    Card(name='D', value=10),
    Card(name='K', value=10),
}
