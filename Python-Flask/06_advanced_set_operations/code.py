friends = {"Bob", "Rolf", "Anne"}
aboard = {"Bob", "Anne"}   # 海外朋友

# local_friends = {"Rolf"}
local_friends = friends.difference(aboard)

print(local_friends)
print(aboard.difference(friends))

# 總朋友數

local = {"Rolf"}
aboard = {"Bob", "Anne"}

friends = local.union(aboard)
print(friends)

# 找交集
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)
