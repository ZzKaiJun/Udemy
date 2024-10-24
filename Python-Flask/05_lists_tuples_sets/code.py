# list : 順序確定
# tuple : 不能修改元素，順序確定
# set : 可以新增元素，但不能出現重複元素，順序不確定

l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# print(l[0])
# print(t[2])
# print(s[0])

l[0] = "Smith"
l.append("Sandy")
l.remove("Rolf")
print(l)

s.add("Smith")
s.add("Smith")
print(s)