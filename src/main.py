import esm2, similarity, uniprot

import torch

EBNA1 = "P03211"
GLIALCAM = "Q14CZ8"

# Mimicry pair from Lanz et al. (2022)
EBNA1_EPITOPE = (386, 405)
GLIALCAM_EPITOPE = (370, 389)

def main():
    ebna1, glialcam = uniprot.fetch(EBNA1, GLIALCAM)

    scores = similarity.compare(
        esm2.embed(ebna1.sequence),
        esm2.embed(glialcam.sequence),
    )

    score, index = torch.max(scores.flatten(), 0)
    row, column = torch.unravel_index(index, scores.shape)

    reference = scores[EBNA1_EPITOPE[0] - 1, GLIALCAM_EPITOPE[0] - 1]

    print(f"{scores.shape[0]} x {scores.shape[1]} window pairs:")
    print(f"best      EBNA1 {int(row) + 1:>4} | GlialCAM {int(column) + 1:>4} | {float(score):.3f}")
    print(f"reference EBNA1 {EBNA1_EPITOPE[0]:>4} | GlialCAM {GLIALCAM_EPITOPE[0]:>4} | {float(reference):.3f}")

if __name__ == "__main__":
    main()
