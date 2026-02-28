import matplotlib.pyplot as plt
from timeit import Timer

sizes = []
pop_head_times = []
append_times = []


pop_head = Timer("x.pop(0)", "from __main__ import x")
append_tail = Timer("x.append(0)", "from __main__ import x")
print(f"{'n':10s}{'pop(0)':>15s}{'append()':>15s}")
for i in range(1_000, 100_001, 5_000):
    sizes += [i]
    
    x = list(range(i))
    head_t = pop_head.timeit(number=1000)
    pop_head_times += [head_t]
    
    x = list(range(i))
    append_t = append_tail.timeit(number=1000)
    append_times += [append_t]
    
    print(f"{i:<10d}{head_t:>15.5f}{append_t:>15.5f}")
    
fig, ax = plt.subplots()
ax.scatter(sizes, pop_head_times, label="pop(0)")
ax.scatter(sizes, append_times, label="append(0)")
ax.set_xlabel("Queue size")
ax.set_ylabel("Time [ms]")
ax.set_title("Comparison between pop(0) and append()")
ax.legend()
ax.grid(True)
plt.show()
