import matplotlib.pyplot as plt
import numpy as np

workers = [1, 2, 4, 8]
threads = [5.05, 5.04, 5.04, 5.03]
process = [5.10, 2.62, 1.53, 1.14]
subinterpreters = [5.07, 2.58, 1.50, 1.09]
baseline = 5.04

x = np.arange(len(workers))
width = 0.25

fig, ax = plt.subplots(figsize=(9, 6))

bars_threads = ax.bar(x - width, threads, width, label="Threads")
bars_process = ax.bar(x, process, width, label="Process")
bars_subinterpreters = ax.bar(
    x + width, subinterpreters, width, label="Subinterpreters"
)

for bars in (bars_threads, bars_process, bars_subinterpreters):
    ax.bar_label(bars, fmt="%.2f", padding=2, fontsize=12)

ax.axhline(
    baseline,
    color="gray",
    linestyle="--",
    linewidth=1.5,
    label=f"Baseline ({baseline}s)",
)

ax.set_xlabel("Workers")
ax.set_ylabel("Time (seconds)")
ax.set_title("Performance by Concurrency Strategy")
ax.set_xticks(x)
ax.set_xticklabels(workers)
ax.set_ylim(0, max(process + threads + subinterpreters) * 1.1)
ax.grid(True, axis="y", linestyle=":", alpha=0.6)
ax.legend()

fig.tight_layout()
plt.savefig("performance_2.png", dpi=150)
