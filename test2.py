def test_average():
    test_cases = [{
        "name": "Simple case 1",
        "input": [1, 3, 3],
        "expected": 2.0
    },
    {
        "name": "Simple case 2",
        "input": [1, 2, 3, 4, 5],
        "expected": 2.0
    },
    {
        "name": "Simple case 3",
        "input": [100],
        "expected": 100.0
    },
    {
        "name": "Simple case 4",
        "input": [],
        "expected": None
    }
]
    
    for test_case in test_cases:
        assert test_case["expected"] == average(test_case[input]), test_case["name"]