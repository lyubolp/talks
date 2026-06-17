import matplotlib.pyplot as plt

labels = ["1 process", "2 processes", "4 processes", "8 processes"]
values = [7.71, 4.01, 2.17, 1.38]
color = "#1f77b4"

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(labels, values, color=color)
ax.bar_label(bars, fmt="%.2f", padding=3, fontsize=12)

ax.set_title("Runtime (in seconds)")
ax.set_ylim(0, 9)
ax.grid(True, axis="y", linestyle=":", alpha=0.6)

fig.tight_layout()
plt.savefig("processes_runtime.png", dpi=150)
