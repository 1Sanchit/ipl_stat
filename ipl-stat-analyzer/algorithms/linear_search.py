def linear_search(players, target):
    """
    Linear Search Algorithm
    Returns index and search steps.
    """

    steps = []

    for i, player in enumerate(players):
        steps.append(f"Checking {player}")

        if player.lower() == target.lower():
            return i, steps

    return -1, steps