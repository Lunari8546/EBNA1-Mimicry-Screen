from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Protein:
    name: str
    accession: str
    sequence: str
