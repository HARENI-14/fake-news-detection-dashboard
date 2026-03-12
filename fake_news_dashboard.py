import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Source": ["Website A", "Website B", "Website C", "Website D"],
    "Fake_News_Count": [45, 30, 25, 20]
}

df = pd.DataFrame(data)

plt.bar(df["Source"], df["Fake_News_Count"])
plt.title("Fake News Distribution by Source")
plt.xlabel("News Source")
plt.ylabel("Fake News Count")

plt.show()
