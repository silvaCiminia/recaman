#!/usr/bin/env python3

'''
Generate a recaman sequence.
'''


def seq(length: int,
        origin: int):
    largest = origin
    arr = [origin] * length

    for i in range(1, length):
        lower_candidate = arr[i-1] - i
        if lower_candidate >= 0 and lower_candidate not in arr:
            # Insert arr[i-1] - i if not already in arr
            arr[i] = lower_candidate
        else:
            # Otherwise, insert arr[i-1] + i
            higher_candidate = arr[i-1] + i

            # If we have a non-zero base, it is possible to have no valid
            # options for continuation. In this case, we end the sequence.
            if origin != 0 and higher_candidate in arr:
                return(arr[:i], largest)

            arr[i] = higher_candidate

            # Return the largest item to pass to plotting operations
            if higher_candidate > largest:
                largest = higher_candidate

    return arr, largest
