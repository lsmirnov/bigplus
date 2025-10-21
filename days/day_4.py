"""days"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="pastel", font_scale=1.1)

df = pd.read_csv("data/titanic.csv")

# Theory

# Quick Recap: GroupBy

# Mean survival rate by gender
print(df.groupby("Sex")["Survived"].mean())

# Mean age by passenger class
print(df.groupby("Pclass")["Age"].mean())

# Combine multiple aggregations
print(df.groupby("Pclass").agg({"Age": "mean", "Fare": "median"}))

# Basic Plots with Matplotlib
plt.hist(df["Age"].dropna(), bins=20, edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.scatter(df["Age"], df["Fare"], alpha=0.5)
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

avg_fare = df.groupby("Pclass")["Fare"].mean()
x: np.ndarray = avg_fare.index.to_numpy(dtype=int)
y: np.ndarray = avg_fare.to_numpy(dtype=float)

plt.bar(x, y, color="teal")
plt.title("Average Fare by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")
plt.show()

# Seaborn (Simpler, Prettier)
sns.countplot(x="Sex", data=df)
plt.title("Count by Gender")
plt.show()

sns.histplot(x=df["Age"], kde=True, bins=20)
plt.title("Age Distribution (with Density)")
plt.show()

sns.boxplot(x="Pclass", y="Age", data=df)
plt.title("Age Distribution by Class")
plt.show()

sns.barplot(x="Pclass", y="Survived", data=df, ci=None)
plt.title("Survival Rate by Class")
plt.show()

corr = df[["Age", "Fare", "Survived"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Practice

sns.histplot(x=df["Fare"], kde=True, bins=20)
plt.title("Fare Distribution (with Density)")
plt.show()

sns.boxplot(x="Pclass", y="Fare", data=df)
plt.title("Fare by Class")
plt.show()

sns.barplot(x="Sex", y="Survived", data=df, ci=None)
plt.title("Survival Rate by Sex")
plt.show()

corr = df[["Age", "Fare", "Survived", "Pclass"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

sns.histplot(x=df["Age"], hue=df["Survived"], kde=True, bins=20)
plt.title("Age Distribution (with Density)")
plt.show()
