# This code used to produce the tables and plot
# in the companion blog post of this dataset release

from statistics import median, mean
from collections import Counter
from py_markdown_table.markdown_table import markdown_table
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np


# Prints statistics on the sizes of flows in each dataset
def sizes_table():
    table = []
    lifter = 'detailed'
    for i in range(1,6+1):
        sizes = []
        with open(f'{lifter}-lifter/dataset_{i}.txt', 'r') as f:
            for line in f:
                if line.startswith('t'):
                    sizes.append(0)
                if line.startswith('v'):
                    sizes[-1] += 1
        table.append({'Dataset' : i, 'Number of Flows' : len(sizes), 'Min Stages' : min(sizes), 'Max Stage' : max(sizes), 'Avg Stages' : f'{mean(sizes):.2f}', 'Median Stages' : int(median(sizes))})
    print(markdown_table(table).get_markdown())


# Plots the distribution of flow sizes across all datasets
def sizes_plot():
    all_names, all_sizes ,all_frequencies = [], [], []
    lifter = 'detailed'
    for i in range(1,6+1):
        all_names.append(f'Dataset {i}')
        sizes = []
        with open(f'{lifter}-lifter/dataset_{i}.txt', 'r') as f:
            for line in f:
                if line.startswith('t'):
                    sizes.append(0)
                if line.startswith('v'):
                    sizes[-1] += 1
        counter = Counter(sizes)
        sizes, frequencies = [], []
        for k,v in counter.items():
            sizes.append(k)
            frequencies.append(v)
        all_sizes.append(sizes)
        all_frequencies.append(frequencies)

    # Create the stacked histogram
    plt.rcParams.update({'font.size': 30})
    cm = plt.get_cmap("GnBu")
    colors = cm(np.linspace(0.2, 1, 6))
    tail = 60
    fig = plt.figure(figsize=(28, 12))
    plt.hist(all_sizes, weights=all_frequencies, stacked=True, bins=range(1, tail+1), label=all_names, color=colors)
    ax = fig.axes[0]
    plt.xlabel('Flow Size')
    plt.ylabel('Frequency')
    plt.xlim(1,tail+1)
    labels = [(str(x) if x%2==0 else '') for x in range(1,tail+1)] 
    plt.xticks([x+0.5 for x in range(1,tail+1)], labels)
    plt.legend()
    plt.tight_layout()
    plt.savefig('plot.png', dpi=300)


# Prints the number of unique labels for each dataset and lifter
def unique_labels():
    table = []
    for i in range(1,6+1):
        table.append({ 'Dataset' : i})
        for lifter in ['simple', 'detailed']:
            labels = set()
            with open(f'{lifter}-lifter/dataset_{i}.txt', 'r') as f:
                for line in f:
                    if line.startswith('v'):
                        labels.add(line.strip().split(' ')[2])
            table[-1][lifter.capitalize() + " Lifter"] = f'{len(labels):,}'
    print(markdown_table(table).get_markdown())


if __name__ == "__main__":
    sizes_table()
    sizes_plot()
    unique_labels()
