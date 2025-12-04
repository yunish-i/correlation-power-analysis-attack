import matplotlib.pyplot as plt
import numpy as np

# Please modify the path to your data files if necessary
traces = np.loadtxt('./data/traces.txt')

plt.plot(traces[0])
plt.title('Power Trace of First Encryption')
plt.xlabel('Number of Sampled Points')

plt.show()