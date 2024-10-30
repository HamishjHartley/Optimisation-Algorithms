import matplotlib.pyplot as plt
import numpy as np

# Genetic Algorithm Results - Small Matrix
ga_small_values = [0.9940740740740741, 0.9938271604938271, 0.994320987654321, 0.9938271604938271, 0.994320987654321]
ga_small_mean = np.mean(ga_small_values)
ga_small_std = np.std(ga_small_values)

# Genetic Algorithm Results - Big Matrix
ga_big_values = [0.9947890922508198, 0.9953669217006287, 0.9937587457620038, 0.9930764893031934, 0.9931112983061939]
ga_big_mean = np.mean(ga_big_values)
ga_big_std = np.std(ga_big_values)

# Hill Climber Results - Small Matrix
hc_small_values = [0.9911111111111112, 0.9932098765432099, 0.9929629629629629, 0.9932098765432099, 0.9934567901234568]
hc_small_mean = np.mean(hc_small_values)
hc_small_std = np.std(hc_small_values)

# Hill Climber Results - Big Matrix
hc_big_values = [0.9957567825342346, 0.9958264005402357, 0.9968149762254509, 0.9959238657486372, 0.9949283282628218]
hc_big_mean = np.mean(hc_big_values)
hc_big_std = np.std(hc_big_values)

# Random Search Results - Small Matrix
rs_small_values = [0.9832098765432099, 0.9896296296296296, 0.990246913580247, 0.9907407407407407, 0.9920987654320987]
rs_small_mean = np.mean(rs_small_values)
rs_small_std = np.std(rs_small_values)

# Random Search Results - Big Matrix
rs_big_values = [0.9751916235615179, 0.9791459263023788, 0.9846527105770636, 0.9858988728844829, 0.9901246858487479]
rs_big_mean = np.mean(rs_big_values)
rs_big_std = np.std(rs_big_values)

# Organize data for plotting
data = [
    ga_small_values, ga_big_values,
    hc_small_values, hc_big_values,
    rs_small_values, rs_big_values
]
labels = [
    "Genetic Algorithm - Small Matrix", "Genetic Algorithm - Big Matrix",
    "Hill Climber - Small Matrix", "Hill Climber - Big Matrix",
    "Random Search - Small Matrix", "Random Search - Big Matrix"
]
means = [ga_small_mean, ga_big_mean, hc_small_mean, hc_big_mean, rs_small_mean, rs_big_mean]
std_devs = [ga_small_std, ga_big_std, hc_small_std, hc_big_std, rs_small_std, rs_big_std]

# Plot boxplots with means and standard deviations
plt.figure(figsize=(12, 6))
plt.boxplot(data, labels=labels, patch_artist=True, showmeans=True, meanline=True)

# Add mean and standard deviation annotations
for i, (mean, std_dev) in enumerate(zip(means, std_devs), 1):
    plt.text(i, mean, f'Mean: {mean:.4f}\nStd Dev: {std_dev:.4f}', ha='center', va='bottom', fontsize=9)

plt.title("APFD Value Distributions with Mean and Standard Deviation for Each Result Set")
plt.ylabel("APFD Value")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
