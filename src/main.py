import esm2, uniprot

EBNA1 = "P03211"
GLIALCAM = "Q14CZ8"

def main():
    proteins = uniprot.fetch(EBNA1, GLIALCAM)

    for protein in proteins:
        embeddings = esm2.embed(protein.sequence)

        print(protein.accession, embeddings.shape)


if __name__ == "__main__":
    main()
