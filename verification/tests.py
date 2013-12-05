"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": r"w@AABGWA>eehurrag",
            "answer": r"Password1",
            "explanation": ""
        },
        {
            "input": r"aGG*?^gZAihl",
            "answer": r"Monkey",
            "explanation": ""
        }
    ],
    "Extra": [
        {
            "input": ["rfegrjewoigfwaef"],
            "answer": ["TCDPTMLX"],
            "explanation": ""
        },
        {
            "input": ["jliajgawegireajger"],
            "answer": ["XINKKBS^B"],
            "explanation": ""
        },
        {
            "input": ["4grwefwfegdr"],
            "answer": ["FCURCQ"],
            "explanation": ""
        },
        {
            "input": ["wy4eu4ehxfh"],
            "answer": ["__LMP;"],
            "explanation": ""
        }
    ]
}
