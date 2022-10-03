from os import mkdir
import matplotlib.pyplot as plt
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from utils.colors import backend_colors as c

def make_plot(data, ylabel, title):
    fig, ax = plt.subplots()
    
    ax.bar(columns, data, color=column_colors)
    ax.set_ylim([0, max(data) + (max(data) * 0.1)])
    ax.set_xlabel("")
    ax.set_ylabel(ylabel, fontweight='bold')
    ax.set_title(title)
    
    for index, data in enumerate(data):
        plt.text(x=index , y =data+(data * 0.01) , s=f"{data}" , fontdict=dict(fontsize=12), ha='center')
    
    plt.show()
    
def make_mean_std_plot(mean, std, title):
    f, ax1 = plt.subplots(1, 1, figsize=(10,5))

    ax1.bar(range(len(mean)), mean, label='Mean (ms)', alpha=0.5, color='b')
    ax1.bar(range(len(std)), std, bottom=mean, label='Standard Deviation (ms)', alpha=0.5, color='r')
    plt.sca(ax1)
    plt.xticks([0, 1, 2, 3, 4],  columns)
    ax1.set_ylabel("Mean +/- Standard Deviation (ms)")
    ax1.set_xlabel("")
    plt.title(title)
    plt.legend(loc='upper left')
    for i in range(len(std)):
        plt.text(x=i , y =mean[i] + std[i] + 10 , s=f"{mean[i]} +/- {std[i]}" , fontdict=dict(fontsize=12), ha='center')

    plt.show()

columns = ["Express", "Django", "Spring", "Gin", "ASP .NET Core"]
column_colors = [c["express"], c["django"], c["spring"], c["gin"], c["aspnet"]]
size = [32.9, 41.6, 72.8, 8.9, 112.1]

# Hello World test
hello_mean = [402, 607, 2200, 345, 2700]
hello_std = [84, 263, 823, 224, 1054]
hello_median = [391, 576, 1933, 287, 2363]
hello_requests = [2446.08, 1625.25, 140.62, 2787.37, 126.57]
hello_transfer_rate = [642.51, 528.17, 21.67, 555.19, 21.84]

# Fibonacci test
fib_mean = [894, 2960, 7652, 1600, 8847]
fib_std = [383.2, 2531.2, 9148, 643, 11845]
fib_median = [866, 2267, 5044, 1234, 5454]
fib_requests = [1092.96, 324.44, 92.51, 568.32, 67.73]
fib_transfer_rate = [29824.85, 34589.75, 10200.12, 15069.35, 7510.73]

# Plots
make_plot(size, "Size (MiB)", "Application size")

make_plot(hello_median, "ms", "Hello World test - Median speed")
make_plot(fib_median, "ms", "Fibonacci test - Median speed")

make_plot(hello_requests, "Requests/s", "Hello World test - Number of requests per second")
make_plot(fib_requests, "Requests/s", "Fibonacci test - Number of requests per second")

make_plot(hello_transfer_rate, "Kbytes/s", "Hello World test - Transfer rate")
make_plot(fib_transfer_rate, "Kbytes/s", "Fibonacci test - Transfer rate")

make_mean_std_plot(hello_mean, hello_std, "Hello World test - General performance")
make_mean_std_plot(fib_mean, fib_median, "Fibonnaci test - General performance")

