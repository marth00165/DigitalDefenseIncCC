# Write a function that
# takes two lists as input and produces one list as output.
# The function should have the signature `def apply_port_exclusions(include_ports, exclude_ports)`.
# The function should expect that the input lists will be a list of low-high pairs which are lists of length two.
# The function should return a minimized and
# ordered list of include port ranges that result after processing the exclude port ranges.
# Include whatever tests and comments you normally provide for completed code.
# Helper Function to try to remove duplicate excludes


# Written using python3


def reduce_ports(include_range, exclude_range):
    # Remove all excluded Ports
    safe_ports = [port for port in include_range if port not in exclude_range]

    outlist = []
    cleared_ports = []
    templist = [safe_ports.pop(0)]

    # Create Ranges of new safe ports
    while len(safe_ports) > 0:
        new_port = safe_ports.pop(0)
        # if the current port range difference is greater than 1 create new range
        if new_port - templist[-1] > 1:
            outlist.append(templist)
            templist = [new_port]
        else:  # else if difference is not greated than 1 include in range
            templist.append(new_port)
    outlist.append(templist)

    # Get 2 value pairs for ranges
    for port_list in outlist:
        cleared_ports.append([port_list[0], port_list[-1]])

    return cleared_ports


def apply_port_exclusions(include_ports, exclude_ports):

    # If no ports included return empty
    if len(include_ports) == 0:
        return []

    include_range_list = []
    exclude_range_list = []

    # Get every included port's range
    for port in include_ports:
        include_min = port[0]
        include_max = port[1] + 1
        port_range = range(include_min, include_max)
        include_range_list.append(port_range)

    # Get every excluded port's range
    for port in exclude_ports:
        exclude_min = port[0]
        exclude_max = port[1] + 1
        port_range = range(exclude_min, exclude_max)
        exclude_range_list.append(port_range)

    # Flatten all available ports into one array
    include_range = [
        port for sublist in include_range_list for port in sublist]

    exclude_range = [
        port for sublist in exclude_range_list for port in sublist]

    # Sort arrays for order
    include_range.sort()
    exclude_range.sort()

    # Function Removes all excluded ports and returns possible ports
    answer = reduce_ports(include_range, exclude_range)
    return answer


# Test Cases and Tests

include1 = [[80, 80], [22, 23], [8000, 9000]]
exclude1 = [[1024, 1024], [8080, 8080]]

answer1 = [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]


include2 = [[8000, 9000], [80, 80], [22, 23]]
exclude2 = [[1024, 1024], [8080, 8080]]

answer2 = [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]

include3 = [[1, 65535]]
exclude3 = [[1000, 2000], [500, 2500]]

answer3 = [[1, 499], [2501, 65535]]


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


# If all test answer's match given answer every test passes
print(f'Test 1 matches the answer 1: {test1 == answer1}')
print(f'Test 2 matches the answer 2: {test2 == answer2}')
print(f'Test 3 matches the answer 3: {test3 == answer3}')
print(f'Test 4 matches the answer 4: {test4 == answer4}')
print(f'Test 5 matches the answer 5: {test5 == answer5}')
