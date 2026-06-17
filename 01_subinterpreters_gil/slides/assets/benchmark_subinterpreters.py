import matplotlib.pyplot as plt
import numpy as np

workers = [1, 2, 4, 8]
baseline = 7.53

gil = [7.77, 4.01, 2.15, 1.32]
no_gil = [7.84, 4.09, 2.25, 1.67]

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
