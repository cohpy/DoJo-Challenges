"""
Daily Coding Problem #27.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def brackets(input_string):
    lst = list()
    result = True

    left_chars = '([{'

    for char in input_string:
        if char in left_chars:
            lst.append(char)
        else:
            compare_char = lst.pop()
            if compare_char == '{':
                if char == '}':
                    continue
                else:
                    result = False
                    break
            elif compare_char == '[':
                if char == ']':
                    continue
                else:
                    result = False
                    break
            elif compare_char == '(':
                if char == ')':
                    continue
                else:
                    result = False
                    break
            else:
                result = False
                break

    if len(lst) == 0:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    input_string = '((()'
    result = brackets(input_string)
    print(result)

# EOF
