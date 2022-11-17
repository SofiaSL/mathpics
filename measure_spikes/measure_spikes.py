#!/usr/bin/env python3
import csv 
import codecs
import matplotlib.pyplot as plt
import numpy as np

reader = csv.reader(codecs.open('C:/Users/55119/projects/measure_spikes.txt', 'rU', 'utf-16'), quoting=csv.QUOTE_NONNUMERIC)
    
data = list(reader)

data = list(map(list, zip(*data)))

l = []
for i in range(2001):
    l.append(3.0 + 0.0005 * i)

for i in range(10):
    for j in range(2001):
        if data[i][j] > 2.0:
            data[i][j] = 2.0

plt.figure(figsize=(40,30))

#plt.plot(l[-1000:], data[0][-1000:],  label="x_c")
plt.plot(l[-1000:], data[1][-1000:],  label="c_1(lambda)")
#plt.plot(l[-1000:], data[2][-1000:],  label="c_2(lambda)")
#plt.plot(l[-1000:], data[3][-1000:],  label="c_3(lambda)")
#plt.plot(l[-1000:], data[4][-1000:],  label="c_4(lambda)")
#plt.plot(l[-1000:], data[5][-1000:],  label="c_5(lambda)")
#plt.plot(l[-1000:], data[6][-1000:])
#plt.plot(l[-1000:], data[7][-1000:])
#plt.plot(l[-1000:], data[8][-1000:])
#plt.plot(l[-1000:], data[9][-1000:])

#plt.yscale("log")
#plt.yticks([])
plt.legend()

plt.show()