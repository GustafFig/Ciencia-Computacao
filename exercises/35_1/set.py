permission = {"member", "group"}
permission.add("user")
permission.add("member")

print(permission)

print(permission.union({"user"}))

print(permission.intersection({"member"}))

print(permission.difference({"member"}))
