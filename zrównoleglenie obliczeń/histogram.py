from random import randint
import threading
import time

data = []
for i in range(100):
    data.append(randint(-11, 10))

min_val = min(data)
max_val = max(data)
hist_vals = [0] * (max_val - min_val + 1)
for d in data:
    hist_vals[d+min_val] += 1


print("1 thread result:", hist_vals)

minval = min(data)
maxval = max(data)
hist_vals1 = [0] * (maxval - minval + 1) #tablice na histogram
hist_vals2 = [0] * (maxval - minval + 1)


def histogram_thread(input_tab, min, output_tab):
    for d in input_tab:
        output_tab[d+min] += 1

data_size = len(data)
part_list1 = data[0:int(data_size/2)]
part_list2 = data[int(-data_size/2):]
time.sleep(5)
t1 = threading.Thread(target=histogram_thread, args=(part_list1, minval, hist_vals1,))
t2 = threading.Thread(target=histogram_thread, args=(part_list2, minval, hist_vals2,))

t1.start()
t2.start()

t1.join()
t2.join()

result_multithread = []
for i in range(len(hist_vals1)):
    result_multithread.append(hist_vals1[i] + hist_vals2[i])
print("2 threads result:", result_multithread)
