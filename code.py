import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data = np.random.randn(100, 2)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

def add_descriptive_statistics(ax, data, label, color):
    ax.bar(['Mean', 'Median'], [np.mean(data), np.median(data)], label=label, color=color, alpha=0.7)
    ax.legend()

def add_histogram(ax, data, label, color):
    ax.hist(data, bins=15, color=color, alpha=0.7, label=label)
    ax.legend()

# Descriptive Statistics 그래프 위치 조정
add_descriptive_statistics(axes[0, 0], a, 'Variable 1', 'blue')
add_descriptive_statistics(axes[0, 0], b, 'Variable 2', 'green')
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Heatmap x축, y축 레이블 추가
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1], cmap='coolwarm')
axes[0, 1].set_title('Correlation Analysis')
axes[0, 1].set_xlabel('Variable')
axes[0, 1].set_ylabel('Variable')

# 히스토그램 범례 관련 코드 제거
add_histogram(axes[1, 0], a, 'Variable 1', 'blue')
add_histogram(axes[1, 0], b, 'Variable 2', 'green')
axes[1, 0].set_title('Histogram of Variables')

axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

plt.tight_layout()
plt.show()