

def psp(string: str) -> bool:
    stack = []
    for symbol in string:
        if symbol in "({[":
            stack.append(symbol)

        if symbol in ")}]":
            if not len(stack):
                return False
            last_symbol_in_stack = stack.pop()

            if symbol == ")" and last_symbol_in_stack != "(":
                return False
            if symbol == "]" and last_symbol_in_stack != "[":
                return False
            if symbol == "}" and last_symbol_in_stack != "{":
                return False

    return not stack


# Простые примеры
assert psp("()") is True
assert psp("[]") is True
assert psp("{}") is True

# Сложные примеры
assert psp("({[]})") is True
assert psp("[({})]") is True
assert psp("{[()]}") is True

# Несбалансированные скобки
assert psp("(") is False
assert psp(")") is False
assert psp("([)]") is False
assert psp("(((") is False
assert psp("}}}") is False

# Пустая строка
assert psp("") is True

# Некорректные скобочные последовательности
assert psp("{[}]") is False
assert psp("[(])") is False
assert psp("((())") is False
