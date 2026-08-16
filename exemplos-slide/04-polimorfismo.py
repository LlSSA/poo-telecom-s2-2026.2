from Room import Room, SquareRoom

def switch_on(r: Room):
    r.switch_light(True)
    print('Is the room illuminated?', r.is_illuminsted())

for i in range(6):
    if i % 2 == 0:
        r = Room()
    else:
        r = SquareRoom()

    switch_on(r)

