def solution(players, callings):
    ranks = {}
    for i, name in enumerate(players):
        ranks[name] = i

    for calling in callings:
        index = ranks[calling]
        players[index - 1], players[index] = players[index], players[index - 1]
        ranks[players[index - 1]] -= 1
        ranks[players[index]] += 1
    return players