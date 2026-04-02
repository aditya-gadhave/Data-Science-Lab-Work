import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Math': [85, 78, 92, 70, 88],
    'Science': [90, 76, 89, 65, 91],
    'English': [88, 82, 94, 72, 85]
}

df = pd.DataFrame(data)

print(df)

df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
print(df)

df.plot(x='Name', y=['Math', 'Science', 'English'], kind='bar')
plt.title("Student Marks Analysis")
plt.show()
