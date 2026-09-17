from protein import Protein

import requests

BASE_URL = "https://rest.uniprot.org/uniprotkb/{accession}"
FIELDS = "accession,protein_name,sequence"

def fetch(*accessions: str) -> list[Protein]:
    proteins: list[Protein] = []

    with requests.Session() as session:
        for accession in accessions:
            response = session.get(
                BASE_URL.format(accession=accession),
                params={"format": "json", "fields": FIELDS},
                timeout=30,
            )

            response.raise_for_status()
            entry = response.json()

            proteins.append(
                Protein(
                    name=entry["proteinDescription"]["recommendedName"]["fullName"]["value"],
                    accession=entry["primaryAccession"],
                    sequence=entry["sequence"]["value"],
                )
            )

    return proteins
