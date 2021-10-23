"""
TESTS is a dict with all of your tests.

Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [['a', 1], ['b', 2]],
            "answer": {'a': 1, 'b': 2}
        },
        {
            "input": [['a', 1], ['a', 2]],
            "answer": {'a': 3,}
        },
        {
            "input": [['a', 1], ['b', 2], ['c', 3], ['a', 5]],
            "answer": {'a': 6, 'b': 2, 'c': 3}
        },
        {
            "input": [['a', 1]],
            "answer": {'a': 1}
        },
    ],
    "Extra": [
        {
            "input": [["bob", 1], ["mark", 2], ["jack", 3], ["jack", 7]],
            "answer": {'bob': 1, 'mark': 2, 'jack': 10}
        },
        {
            "input": [["bob", 1], ["mark", 1], ["bob", 1], ["mark", 1], ["bob", 1], ["mark", 1]],
            "answer": {'bob': 3, 'mark': 3}
        },
    ]
}
