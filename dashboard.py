import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("Cleaned_Data/sales_cleaned.csv")

# Calculate KPIs
total_passengers = len(df)
total_survivors = df["Survived"].sum()
survival_rate = df["Survived"].mean() * 100

# Create dashboard
fig = plt.figure(figsize=(14, 9))

# Title
fig.suptitle(
    "Titanic Data Analytics Dashboard",
    fontsize=20,
    fontweight="bold"
)

# KPI 1
ax1 = plt.subplot(2, 3, 1)
ax1.text(0.5, 0.5, f"{total_passengers}",
         ha="center", va="center", fontsize=28)
ax1.set_title("Total Passengers")
ax1.axis("off")

# KPI 2
ax2 = plt.subplot(2, 3, 2)
ax2.text(0.5, 0.5, f"{total_survivors}",
         ha="center", va="center", fontsize=28)
ax2.set_title("Total Survivors")
ax2.axis("off")

# KPI 3
ax3 = plt.subplot(2, 3, 3)
ax3.text(0.5, 0.5, f"{survival_rate:.2f}%",
         ha="center", va="center", fontsize=28)
ax3.set_title("Survival Rate")
ax3.axis("off")

# Survival by Gender
ax4 = plt.subplot(2, 3, 4)
gender_survival = df.groupby("Sex")["Survived"].mean() * 100
gender_survival.plot(kind="bar", ax=ax4)
ax4.set_title("Survival Rate by Gender")
ax4.set_ylabel("Survival Rate (%)")
ax4.set_xlabel("Gender")
ax4.tick_params(axis="x", rotation=0)

# Survival by Passenger Class
ax5 = plt.subplot(2, 3, 5)
class_survival = df.groupby("Pclass")["Survived"].mean() * 100
class_survival.plot(kind="bar", ax=ax5)
ax5.set_title("Survival Rate by Passenger Class")
ax5.set_ylabel("Survival Rate (%)")
ax5.set_xlabel("Passenger Class")
ax5.tick_params(axis="x", rotation=0)

# Passengers by Embarked Port
ax6 = plt.subplot(2, 3, 6)
embarked_count = df["Embarked"].value_counts()
embarked_count.plot(kind="bar", ax=ax6)
ax6.set_title("Passengers by Embarked Port")
ax6.set_ylabel("Passengers")
ax6.set_xlabel("Port")
ax6.tick_params(axis="x", rotation=0)

plt.tight_layout()

# Save dashboard
plt.savefig("Dashboard/titanic_dashboard.png", dpi=300)

print("Dashboard created successfully!")
print("Dashboard saved in Dashboard folder.")
pit.tight_layout()
plt.show()