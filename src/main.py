import uniprot

EBNA1 = "P03211"
GLIALCAM = "Q14CZ8"

def main():
    proteins = uniprot.fetch(EBNA1, GLIALCAM)

    for protein in proteins:
        print(protein)


if __name__ == "__main__":
    main()
