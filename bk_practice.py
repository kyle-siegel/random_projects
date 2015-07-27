__author__ = 'kylesiegel'

from bokeh import plotting as plt
import numpy as np

def main():
    x = np.array([1,2,3])
    y = np.random.randn(3)

    fig = plt.figure()
    fig.line(x,y)

    plt.show(fig)

