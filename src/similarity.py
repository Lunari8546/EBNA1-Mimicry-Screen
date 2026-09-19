import torch
from torch.nn.functional import normalize

WINDOW_SIZE = 20

def _windows(embeddings: torch.Tensor) -> torch.Tensor:
    return embeddings.unfold(0, WINDOW_SIZE, 1).mean(dim=2)

def compare(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    for embeddings in (x, y):
        if len(embeddings) < WINDOW_SIZE:
            raise ValueError(f"Not enough residues for WINDOW_SIZE ({WINDOW_SIZE}): {len(embeddings)}")

    x_windows = normalize(_windows(x))
    y_windows = normalize(_windows(y))

    return x_windows @ y_windows.T
