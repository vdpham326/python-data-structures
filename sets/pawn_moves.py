def next_position(current_position, move):
    x, y = current_position # untuck the tuple into x and y variables
    if move == 'down':
        return (x, y - 1)
    if move == 'up':
        return (x, y + 1)
    if move == 'left':
        return (x - 1, y)
    if move == 'right':
        return (x + 1, y)


print(next_position((0, -3), 'left')) #should return (-1, -3)
print(next_position((5, 2), 'right')) #should return (6, 2)
print(next_position((-2, -1), 'up')) #should return (-2, 0)
print(next_position((-4, 3), 'down')) #should return (-4, 2)




