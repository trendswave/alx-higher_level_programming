#!/usr/bin/python3
def remove_char_at(str, n):
    n_str = str

    if len(str) <= n or n < 0:
        return n_str
    n_str = n_str[0: n:] + n_str[n + 1:]
        return n_str
