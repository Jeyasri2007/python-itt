k = int(input())
rooms = list(map(int, input().split()))

unique_rooms = set(rooms)

# The mathematical formula to find the unique element
captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

print(captain_room)
