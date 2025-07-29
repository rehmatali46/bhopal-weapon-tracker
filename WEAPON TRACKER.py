pip install pandas matplotlib seaborn openpyxl
import pandas as pd

# Load CSV file
df = pd.read_csv("bhopal_weapon_license_data.csv")

# Show the first 5 records
df.head()
# Total records
print("Total records:", len(df))

# Count of weapon types
print(df['gun_type'].value_counts())

# Weapon status summary
print(df['weapon_status'].value_counts())

# Submission summary
print(df['is_submitted'].value_counts())
import seaborn as sns
import matplotlib.pyplot as plt

# Weapon status bar chart
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='weapon_status', palette='Set2')
plt.title('Weapon Status Distribution')
plt.show()

# Gun type per area
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='gun_type', hue='area')
plt.title('Gun Types per Area')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
# Weapons not yet submitted
pending = df[df['is_submitted'] == False]

# View top 10
pending[['holder_name', 'mobile_number', 'area', 'gun_type', 'weapon_status']].head(10)
# Simulate generating reminder messages
pending['reminder_message'] = pending.apply(
    lambda x: f"Dear {x['holder_name']}, please submit your {x['gun_type']} ({x['weapon_model']}) at {x['police_station']} due to upcoming events.", axis=1
)

# View sample message
pending[['holder_name', 'mobile_number', 'reminder_message']].head(5)