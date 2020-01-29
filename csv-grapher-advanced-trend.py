from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gc

All_files = glob('*.csv')

for file in All_files:

    name = file.split('.csv')[0]

    df = pd.read_csv(file)

    x = df.index
    y = df.total_bytes_per_sec
    plt.scatter(x, y)

    fig, ax = plt.subplots(figsize=(7,4))

    ax.plot(x,y)

    z = np.polyfit(x, y, 30)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")

    ax.set_xlabel('October 1st to 31st')
    ax.set_ylabel('Bytes per second')

 
    plt.savefig(name+'.png', dpi=600)

    plt.close()
    del x, y, z, p
    gc.collect()
