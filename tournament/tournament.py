from collections import defaultdict

base_row = '{:30s} | {:2} | {:2} | {:2} | {:2} | {:2}'
win, loss, draw = 'win', 'loss', 'draw'


def tally(tournament_results: list) -> list:
    results = defaultdict(lambda: {win: 0, loss: 0, draw: 0})
    for match in tournament_results:
        team1, team2, result = match.split(';')
        if result == win:
            results[team1][win] += 1
            results[team2][loss] += 1
        elif result == loss:
            results[team2][win] += 1
            results[team1][loss] += 1
        elif result == draw:
            results[team1][draw] += 1
            results[team2][draw] += 1

    table = [base_row.format('Team', 'MP', ' W', ' D', ' L', ' P')]
    for team in sorted(results.keys(), key=lambda team: (-score(**results[team]), team)):
        table.append(base_row.format(
            team, sum(results[team].values()), results[team][win], results[team][draw], results[team][loss],
            score(**results[team])
        ))

    return table


def score(*, win, loss, draw) -> int:
    return 3 * win + draw
