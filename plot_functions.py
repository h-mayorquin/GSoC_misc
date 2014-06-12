import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def plot_mutliplot_bilinear(N,ims):
    '''
    Plot a series (N) of matrices with the standard color scheme 
    
    '''

    cdict1 = {'red':   ((0.0, 0.0, 0.0),
                   (0.5, 0.0, 0.1),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 1.0),
                   (0.5, 0.1, 0.0),
                   (1.0, 0.0, 0.0))
        }

    blue_red1 = LinearSegmentedColormap('BlueRed1', cdict1)

    n = int(np.sqrt(N))
    print n
    number = n * n
    print number
    for i in range(number):
        plt.subplot(n,n,i + 1)
        plt.imshow(ims[i,:,:], interpolation='bilinear', cmap=blue_red1)
        plt.colorbar()