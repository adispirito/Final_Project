# Customary Imports:
import numpy as np
import os
import matplotlib.pyplot as plt
import utils.history_utils
##################################################################################################################################
'''
MODEL HISTORY FUNCTIONS:
'''
def save_history(history, output_dir):
    directory = os.path.join(os.getcwd(), output_dir)
    if not os.path.exists(directory):
        os.mkdir(directory)
    filepath = os.path.join(directory, 'history')
    np.savez(filepath, **history.history)

def load_history_from_saved(directory):
    direct = os.path.join(os.getcwd(), directory)
    filepath = os.path.join(direct, 'history.npz')
    array = dict(np.load(filepath, allow_pickle=True, fix_imports=True))
    return array

def show_history(hist, offset=0, hist_keys=None):
    if hist_keys is None:
        hist_keys = hist.history.keys()
    hist_keys = [key for key in hist_keys if key[:3] != 'val']
    for metric in hist_keys:
        data1 = hist.history[metric][offset:]
        epochs = range(offset,len(data1)+offset)
        plt.plot(epochs, data1)
        data2 = hist.history[f'val_{metric}'][offset:]
        plt.plot(epochs, data2)
        plt.title(f'Model {metric}')
        plt.ylabel(metric)
        plt.xlabel('Epoch')
        plt.legend(["train", "test"], loc = "upper left")
        #plt.xticks(epochs)
        plt.show()
