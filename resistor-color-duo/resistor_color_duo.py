def value(colors):
    return int(''.join(str(colors_list().index(c)) for c in colors))


def colors_list():
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
