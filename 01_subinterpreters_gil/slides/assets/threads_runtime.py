import matplotlib.pyplot as plt

labels = ["1 thread", "2 threads", "4 threads", "8 threads"]
values = [7.60, 7.76, 7.8, 7.76]
color = "#1f77b4"

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(labels, values, color=color)
ax.bar_label(bars, fmt="%.2f", padding=3, fontsize=12)

ax.set_title("Runtime (in seconds)")
ax.set_ylim(0, 9)
ax.grid(True, axis="y", linestyle=":", alpha=0.6)

fig.tight_layout()
plt.savefig("threads_runtime.png", dpi=150)
