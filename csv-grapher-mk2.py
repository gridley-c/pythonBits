from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

All_files = glob('*.csv')

for file in All_files:

    name = file.split('.csv')[0]

    df = pd.read_csv(file)

    x = df.index
    y = df.total_bytes_per_sec
    plt.scatter(x, y)

    fig, ax = plt.subplots(figsize=(15,5))

    ax.plot(x,y)

    z = np.polyfit(x, y, 30)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")

    j = np.polyfit(x, y, 1)
    k = np.poly1d(j)
    plt.plot(x,k(x),"y--")

    ax.set_xlabel('October 1st to 31st')
    ax.set_ylabel('Bytes per second, max 1GB/s')
    ax.set_ylim([0,1000000000])

 
    plt.savefig(name+'LinearAndPoly.png', dpi=300)
