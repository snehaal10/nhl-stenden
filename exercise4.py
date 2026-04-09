import csv
import numpy as np
from typing import Set, Tuple, List
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from PIL import Image
import time

def plot_data(csv_file_path: str):
    """
    Fixed: Converted the list of strings from CSV into a float numpy array.
    """
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader) # Skip header
        for row in csv_reader:
            results.append(row)
    
    # Convert string data to float for correct plotting
    results = np.array(results).astype(float)

    # plot precision-recall curve
    plt.plot(results[:, 1], results[:, 0])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.show()

# Generate dummy file for testing
with open("data_file.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["precision", "recall"])
    w.writerows([[0.013,0.951], [0.376,0.851], [0.441,0.839], [0.570,0.758],
                 [0.635,0.674], [0.721,0.604], [0.837,0.531], [0.860,0.453],
                 [0.962,0.348], [0.982,0.273], [1.0,0.0]])

plot_data('data_file.csv')