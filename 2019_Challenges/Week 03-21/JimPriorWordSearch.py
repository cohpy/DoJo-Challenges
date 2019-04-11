"""
Jim Prior's solution to the DoJo problem of March 21,2019.
"""

from itertools import chain

def is_word_in_array(word, array):
    left_to_right_strings = (''.join(row) for row in array)
    top_to_bottom_strings = (''.join(column) for column in zip(*array))
    all_strings = chain(left_to_right_strings, top_to_bottom_strings)
    return any (word in candidate for candidate in all_strings)

def is_word_in_array2(word, array):
    rows = map(lambda  row: ''.join(row), array)
    columns = map(lambda column: ''.join(column), zip(*array))
    return (
        any(map(lambda row: word in row, rows))
        or
        any(map(lambda column: word in column, columns))
    )


def is_word_in_array3(word, array):
    return any (
        word in s
        for s in [
            ''.join(row) for row in array
        ] + [
            ''.join(column) for column in zip(*array)
        ]
    )

if __name__ == '__main__':
    matrix = [
        ['F', 'A', 'C', 'I', ],
        ['O', 'B', 'O', 'P', ],
        ['A', 'N', 'O', 'B', ],
        ['M', 'A', 'S', 'S', ],
    ]

    print(is_word_in_array('FOAM', matrix))
    print(is_word_in_array('MASS', matrix))
    print(is_word_in_array2('FOAM', matrix))
    print(is_word_in_array2('MASS', matrix))
    print(is_word_in_array3('FOAM', matrix))
    print(is_word_in_array3('MASS', matrix))
