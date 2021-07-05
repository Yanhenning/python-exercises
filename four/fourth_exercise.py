mapping = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def all_brackets_closed(string):
    brackets_stack = []
    for bracket in string:
        if bracket in mapping.keys():
            brackets_stack.append(bracket)
        else:
            if not brackets_stack:
                return False
            current_bracket = brackets_stack.pop()
            if current_bracket and mapping[current_bracket] != bracket:
                return False

    if brackets_stack:
        return False
    return True
