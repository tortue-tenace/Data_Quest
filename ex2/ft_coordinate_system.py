import math

print("=== Game Coordinate System ===")


def get_player_pos() -> tuple[float, float, float]:
    prompt = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        coord_input = input(prompt).split(",")
        if len(coord_input) != 3:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        valid = True
        for c in coord_input:
            try:
                coords.append(float(c))
            except ValueError:
                stripped = c.strip()
                print(
                    f"Error on parameter '{stripped}':  "
                    f"could not convert string to float:  '{stripped}'"
                )
                valid = False
                break
        if valid:
            return (coords[0], coords[1], coords[2])


print("Get a first set of coordinates")
pos1: tuple[float, float, float] = get_player_pos()
print(f"Got a first tuple:  {pos1}")
print(f"It includes:  X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
dist_center: float = round(
    math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2), 4
)
print(f"Distance to center:  {dist_center}")

print()
print("Get a second set of coordinates")
pos2: tuple[float, float, float] = get_player_pos()
dist_between: float = round(
    math.sqrt(
        (pos2[0] - pos1[0])**2
        + (pos2[1] - pos1[1])**2
        + (pos2[2] - pos1[2])**2
    ),
    4
)
print(f"Distance between the 2 sets of coordinates:  {dist_between}")
