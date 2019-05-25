def is_paired(input_string):
    brackets = []
    sanitized_input = list(filter(lambda x: x in "[]{}()", input_string))
    matching_brackets = {'(': ')', '[': ']', '{': '}'}

    for bracket in sanitized_input:
        if bracket in "([{":
            brackets.append(bracket)
        else:
            if len(brackets) == 0 or bracket != matching_brackets[brackets[-1]]:
                return False
            brackets.pop()

    return len(brackets) == 0
