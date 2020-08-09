d = {"tom": 79, "rob": 89, "joe": 94}
print(d)

print(d["tom"])

d["joe"] = 22
print(d["joe"])

d["sam"] = 56
print(d["sam"])

del d["sam"]
print(d)

for key in d:
    print("Key :", key, " value: ", d[key])

for key, value in d.items():
    print("Key :", key, " value: ", value)

print("sam" in d)
print("tom" in d)

d.clear()
print(d)
