points=[]
n=int(input("enter the number:"))
for i in range(n):
    x,y,z=map(int,input(f"enter the co-ordinates of {i+1}: ").split())
    points.append((x,y,z))
print(points) 
min_distance=float('inf')
closest_pair=None
for i in range(n):
    for j in range(n):
        if j != i:
            xi, yi, zi = points[i]
            xj, yj, zj = points[j]
            d = (((xi - xj) ** 2) + ((yi - yj) ** 2) + ((zi - zj) ** 2)) ** 0.5
            if d <min_distance :
                min_distance=d
                closest_pair = [points[i], points[j]]
print(f"closest pair is:{closest_pair}")
