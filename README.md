# Correlation Power Analysis Attack

# How does it work?

This work recovers a full round key used in an AES encryption process. The methodology is that encryption process leaks information through power consumption, so by statistically correlate the measured power traces with hypothetical power models (in this work, Hamming Distance model and Hamming Weight model) for each key byte guess, we can eventually recover the key.

# To run the attack

Prepare the data set first. I used 7000 power traces, and 3125 points on each trace. Please modify the code if the size of your data is different.

Please run `python attack.py` in your terminal or IDE. You might need to install matplotlib, numpy, and scipy first.

You will get each byte of the 16-byte key printed out. Also there will be plotting a table of 16 subplotting for each of the byte.

# To run plot-trace

In plot-trace.py, I have a simple program to plot the first trace of the given traces.

# Attack if the leakage point is unknown

To implement the attack, I wrote a simply program notknowleakage.py, which is modified from attack.py. In the program, I tried to guess the first byte of key over 256 possiblities and 100 possible leakage point (we are recovering last round, so we have a rough range). The theory is that at the correct key byte and leak point, the power fluctuation would be most correlative to the actual samples (we have 7000 actual samples). So I picked the first byte of key as a test case, setting up a 2D matrix (256 possible key byte values over 100 possible leak point), trying to find the largest value in the matrix, which means the most correlative point. This point would locate at the correct key byte and the leakage point we are looking for.

Please run `python notknowleakage.py` in your terminal or IDE, and then it will print out the leakage point after calculation. I got 2663 printed out, so 2663 is the correct leakage point.

# Attack using Hamming Weight power model in this case

To implement extra credit 2, I have hammmingweight.py to get the leakage point, and hwattack.py The leakage point is 2484. I used the first byte of key as a test case. However, when I tried to get other key bytes from the hamming weight attack, it failed. It is probably because FPGA implementation does not have a strong correlation with hamming weight, so by only calculating hamming weight, it is hard to attack.
