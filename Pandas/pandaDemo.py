import pandas as pd

data = {
    "Name": ["Lalit", "Rahul", "Aman"],
    "Age": [25, 23, 24],
    "Marks": [85, 72, 91]
}

df = pd.DataFrame(data)

print(df)

# d=pd.DataFrame([10,15,20],columns=['Marks'])
# print(d)

print(df.head(2))
print(df.tail(1))
print(df.shape)
print(df.columns()) 