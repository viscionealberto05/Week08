from dataclasses import dataclass

@dataclass
class Parola:
    id: int
    nome: str

    def __eq__(self, other):
        return isinstance(other, Parola) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome}"

    def __repr__(self):
        return f"{self.id} | {self.nome}"