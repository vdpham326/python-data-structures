sample_moves = [1, 2, 1, 3, 1, 2, 2]


def count_states(moves):
    current_state = (5, 5)
    past_levels = {(5, 5)}

    #iterate through the list moves 
    for move in moves:
        x, y = current_state
        if move == 1:
            current_state = (min(x + 1, 10), y)
        if move == 2:
            if x > 0 and y < 10:
                current_state = (x - 1, y + 1)
            else:
                current_state = (x, y)
        if move == 3:
            current_state = (x, max(y - 1, 0))
        
        if current_state in past_levels:
            return len(past_levels)
        else:
            past_levels.add(current_state)
    return -1

print(count_states(sample_moves))