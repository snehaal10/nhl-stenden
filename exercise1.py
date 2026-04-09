import csv
import numpy as np
from typing import Set, Tuple, List
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from PIL import Image
import time



def id_to_fruit(fruit_id: int, fruits: List[str]) -> str:
    """
    Fixed: Changed input type from set to list to maintain order.
    Sets are unordered, so list(set) results in random indexing.
    """
    idx = 0
    for fruit in fruits:
        if idx == fruit_id:
            return fruit
        idx += 1

# Testing
fruit_list = ["apple", "orange", "melon", "kiwi", "strawberry"]
name1 = id_to_fruit(1, fruit_list)
name3 = id_to_fruit(3, fruit_list)
name4 = id_to_fruit(4, fruit_list)
print(f"Index 1: {name1}, Index 3: {name3}, Index 4: {name4}")