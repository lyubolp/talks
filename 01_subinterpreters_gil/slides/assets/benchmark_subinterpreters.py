import matplotlib.pyplot as plt
import numpy as np

workers = [1, 2, 4, 8]
baseline = 5.04

gil = [5.07, 2.58, 1.50, 1.09]
no_gil = [5.05, 2.79, 1.76, 1.36]

x = np.arange(len(workers))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 6))

bars_gil = ax.bar(x - width / 2, gil, width, label="GIL")
bars_nogil = ax.bar(x + width / 2, no_gil, width, label="No GIL")

for bars in (bars_gil, bars_nogil):
    ax.bar_label(bars, fmt="%.2f", padding=2, fontsize=11)

ax.axhline(
    baseline,
    color="gray",
    linestyle="--",
    linewidth=1.5,
    label=f"Baseline ({baseline}s)",
)

ax.set_title("Subinterpreters")
ax.set_xlabel("Workers")
ax.set_ylabel("Time (seconds)")
ax.set_xticks(x)
ax.set_xticklabels(workers)
ax.set_ylim(0, max(gil + no_gil) * 1.15)
ax.grid(True, axis="y", linestyle=":", alpha=0.6)
ax.legend()

fig.tight_layout()
plt.savefig("benchmark_subinterpreters.png", dpi=150)
