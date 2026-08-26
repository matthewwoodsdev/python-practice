# Copying lists
# Matthew Woods - practice file

areas = [11.25, 18.0, 20.0]
areas_ref = areas
areas_copy = list(areas)

areas_ref[0] = 5.0
areas_copy[1] = 99.0

print(areas)
print(areas_ref)
print(areas_copy) 
