#!/usr/bin/env python3

'''
Generate a recaman sequence.
'''

from enum import Enum


class Op(Enum):
    # Sequence types
    SUB = 1
    DIV = 2


def seq(length: int,
        origin: int,
        op: Op) -> ([], int):
    largest = origin
    arr = [origin] * length
    (_dec_op, _inc_op) = get_op(op)

    for i in range(1, length):
        lower_candidate = _dec_op(arr[i-1], i)
        if lower_candidate >= 0 and (i == 1 or lower_candidate not in arr):
            # Insert arr[i-1] - i if not already in arr
            arr[i] = lower_candidate
        else:
            # Otherwise, insert arr[i-1] + i
            higher_candidate = _inc_op(arr[i-1], i)

            # If we have a non-zero base, it is possible to have no valid
            # options for continuation. In this case, we end the sequence.
            if origin != 0 and higher_candidate in arr:
                return(arr[:i], largest)

            arr[i] = higher_candidate

            # Return the largest item to pass to plotting operations
            if higher_candidate > largest:
                largest = higher_candidate

    return arr, largest


def get_op(op: Op):
    if Op(op) == Op.SUB:
        return (lambda x, y: x - y,
                lambda x, y: x + y)

    elif Op(op) == Op.DIV:
        # Ensure that only factors of x are considered as candidates
        return (lambda x, y: (int)(x / y) if x % y == 0 else -1,
                lambda x, y: x * y)

k = 10

for i in range(0,50):
    a, l = seq(k, i, 1)
    if len(a) == k:
        print(str(i), ':)')
        continue
    #print(str(i), ': ', str(len(a)))
