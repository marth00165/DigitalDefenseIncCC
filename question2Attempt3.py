# Write a function that
# takes two lists as input and produces one list as output.
# The function should have the signature `def apply_port_exclusions(include_ports, exclude_ports)`.
# The function should expect that the input lists will be a list of low-high pairs which are lists of length two.
# The function should return a minimized and
# ordered list of include port ranges that result after processing the exclude port ranges.
# Include whatever tests and comments you normally provide for completed code.
# Helper Function to try to remove duplicate excludes


def merge_intervals(intervals):
    intervals.sort()

    # Merges intervals of 1

    i = 0

    while i < len(intervals) - 1:
        currentPort = intervals[i]
        nextPort = intervals[i+1]
        if nextPort[0] - currentPort[1] == 1:
            currentPort[1] = nextPort[1]
            intervals.remove(nextPort)
        else:
            i = i+1

     # Merges overlapping intervals

    i = 1

    while i < len(intervals):

        if intervals[i][0] <= intervals[i-1][1]:

            intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
            intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])

            intervals.pop(i)
        else:
            i = i+1

    return intervals


def merge_edge_cases(intervals):
    # Fix edge cases and merge those intervals
    x = 0

    while x < len(intervals)-1:
        currPort = intervals[x]
        nextPort = intervals[x+1]

        if currPort[0] > nextPort[0]:
            nextPort[0] = currPort[0]
            intervals.remove(currPort)
            x = x-1
        else:
            x = x+1

    return intervals


def create_imperfect_answer(merged_include_ports, merged_exclude_ports):

    answer = []
    # Creates imperfect answer array
    while len(merged_include_ports) > 0:
        includePort = merged_include_ports.pop(0)

        checks = 0

        for excludePort in merged_exclude_ports:
            if includePort[0] < excludePort[0] and includePort[1] < excludePort[0]:  # []()
                checks = checks + 1
            if includePort[0] > excludePort[1] and includePort[1] > excludePort[1]:  # ()[]
                checks = checks + 1
            # if overlap
            # [()]
            if includePort[0] < excludePort[0] and includePort[1] > excludePort[1]:
                answer.append([includePort[0], excludePort[0] - 1])
                answer.append([excludePort[1]+1, includePort[1]])
            # ([)]
            if includePort[0] > excludePort[0] and includePort[0] < excludePort[1] and includePort[1] > excludePort[1]:
                answer.append([excludePort[1]+1, includePort[1]])
            # [(])
            if includePort[0] < excludePort[0] and excludePort[0] < includePort[1] and excludePort[1] > includePort[1]:
                answer.append([includePort[0], excludePort[0] - 1])
            # If No overlap with exclude push port
            if checks == len(merged_exclude_ports):
                answer.append(includePort)
    return answer


def apply_port_exclusions(include_ports, exclude_ports):

    answer = None

    if len(include_ports) == 0:
        answer = []

    merged_include_ports = merge_intervals(
        include_ports)  # Merges Include Port intervals

    merged_exclude_ports = merge_intervals(
        exclude_ports)  # Merges Exclude Port intervals

    imperfectAnswer = create_imperfect_answer(  # Gets answer without edge cases solved
        merged_include_ports, merged_exclude_ports)

    # Gets answer with edge cases solved
    answer = merge_edge_cases(imperfectAnswer)

    return answer


# Test Cases and Tests
include1 = [[80, 80], [22, 23], [8000, 9000]]
exclude1 = [[1024, 1024], [8080, 8080]]

answer1 = [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]


# Fails this scenario

include2 = [[8000, 9000], [80, 80], [22, 23], [1010, 1060]]
exclude2 = [[1024, 1030], [1035, 1050], [8080, 8080]]

answer2 = [[22, 23], [80, 80], [1010, 1023],
           [1031, 1034], [1051, 1060], [8000, 8079], [8081, 9000]]


include3 = [[1, 65535]]
exclude3 = [[1000, 2000], [600, 3000], [500, 2500]]

answer3 = [[1, 499], [3001, 65535]]


include4 = [[1, 1], [2, 2], [3, 3], [4, 65535]]
exclude4 = [[1000, 2000], [500, 2500]]

answer4 = [[1, 499], [2501, 65535]]


include5 = []
exclude5 = [[8080, 8080]]
answer5 = []


test1 = apply_port_exclusions(include1, exclude1)  # Answer for Test input 1

test2 = apply_port_exclusions(include2, exclude2)  # Answer for Test input 2

test3 = apply_port_exclusions(include3, exclude3)  # Answer for Test input 3

test4 = apply_port_exclusions(include4, exclude4)  # Answer for Test input 4

test5 = apply_port_exclusions(include5, exclude5)  # Answer for Test input 5


def runTests():
    assert test1 == answer1, f'Should be {answer1}'
    assert test2 == answer2, f'Should be {answer2}'
    assert test3 == answer3, f'Should be {answer3}'
    assert test4 == answer4, f'Should be {answer4}'
    assert test5 == answer5, f'Should be {answer5}'

    print("All Tests Passed")


runTests()
