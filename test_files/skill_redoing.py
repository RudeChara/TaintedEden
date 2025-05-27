import sys

data = "".join(list(sys.stdin))
data2 = ""
for item in data:
    if item != " " and item != "\n":
        data2 = data2 + item
data2 = data2.split(",")
print(data2)
