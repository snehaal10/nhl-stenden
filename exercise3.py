import csv
import numpy as np
from typing import Set, Tuple, List
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from PIL import Image
import time

def swap(coords: np.ndarray):
    """
    Fixed: Used advanced indexing to swap columns correctly 
    without overwriting values mid-assignment.
    """
    # Swap x1 with y1 (0, 1) and x2 with y2 (2, 3)
    swapped = coords.copy()
    swapped[:, [0, 1, 2, 3]] = coords[:, [1, 0, 3, 2]]
    return swapped

# Testing
coords = np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0],
                   [5, 3, 13, 6, 1],
                   [4, 4, 13, 6, 1],
                   [6, 5, 13, 16, 1]])
swapped_coords = swap(coords)
print("Original:\n", coords)
print("Swapped:\n", swapped_coords)