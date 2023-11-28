#!/usr/bin/python3
''' Module 5 for task 4 '''


def text_indentation(text):
    ''' Indent a text '''
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")

    new_str = "".join([x if x not in ".?:" else x + "\n\n" for x in text])
    print("\n".join([x.strip() for x in new_str.split("\n")]), end="")
