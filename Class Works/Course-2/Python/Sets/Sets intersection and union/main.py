setx = {"green", "blue"}
sety = {"blue", "red"}
print(setx)
print(sety)
setz = setx.intersection(sety)
print("Intersection of two sets:", setz)

seta = sety.union(setx)
print("Union of setx and sety:", seta)