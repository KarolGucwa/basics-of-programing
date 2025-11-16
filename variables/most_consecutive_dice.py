def f(dice):
    max_count = 1
    current_count = 1
    most_rolled = dice[0]

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                most_rolled = dice[i - 1]
            current_count = 1

    if current_count > max_count:
        most_rolled = dice[-1]

    return most_rolled
