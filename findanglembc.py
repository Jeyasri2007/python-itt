import math
ab = int(input())
bc = int(input())
angle_rad = math.atan2(ab, bc)
angle_deg = math.degrees(angle_rad)
res = round(angle_deg)
print(f"{res}\u00b0")
