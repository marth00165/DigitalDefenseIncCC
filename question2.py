# Write a function that
# takes two lists as input and produces one list as output.
# The function should have the signature `def apply_port_exclusions(include_ports, exclude_ports)`.
# The function should expect that the input lists will be a list of low-high pairs which are lists of length two.
# The function should return a minimized and
# ordered list of include port ranges that result after processing the exclude port ranges.

# Include whatever tests and comments you normally provide for completed code.

# Examples:
# input:
# include_ports: [[80, 80], [22, 23], [8000, 9000]]
# exclude_ports: [[1024, 1024], [8080, 8080]]
# output: [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]


# input:
# include_ports: [[8000, 9000], [80, 80], [22, 23]]
# exclude_ports: [[1024, 1024], [8080, 8080]]
# output:
# [[22, 23], [80, 80], [8000, 8079], [8081, 9000]]

# input:
# include_ports: [[1,65535]]
# exclude_ports: [[1000,2000], [500, 2500]]
# output:
# [[1, 499], [2501, 65535]]

# input:
# include_ports: [[1,1], [3, 65535], [2, 2]]
# exclude_ports: [[1000, 2000], [500, 2500]]
# output:
# [[1, 499], [2501, 65535]]

# input:
# include_ports: []
# exclude_ports: [[8080, 8080]]
# output:
# []

def reduce_exclude_ports(exclude_ports):
    current_port_range = exclude_ports[0]

    for portList in exclude_ports:
        if current_port_range == portList:
            continue
        if set(range(portList[0], portList[-1])).issubset(set(range(current_port_range[0], current_port_range[-1]))):
            exclude_ports.remove(portList)
        else:
            current_port_range = portList

    return exclude_ports


def reduce_include_port(include_ports):
    # print(include_ports)
    return include_ports


def port_reducer(include_range, exclude_range):
    safe_ports = [port for port in include_range if port not in exclude_range]
    outlist = []
    cleared_ports = []
    templist = [safe_ports.pop(0)]
    while len(safe_ports) > 0:
        x = safe_ports.pop(0)
        if x - templist[-1] > 1:
            outlist.append(templist)
            templist = [x]
        else:
            templist.append(x)
    outlist.append(templist)

    for port_list in outlist:
        cleared_ports.append([port_list[0], port_list[-1]])

    return cleared_ports


def apply_port_exclusions(include_ports, exclude_ports):
    answer = []

    if len(include_ports) == 0:
        return []

    include_ports.sort()
    exclude_ports.sort()

    for include_port in include_ports:
        clear_counter = 0
        clear_target = len(exclude_ports)
        for exclude_port in exclude_ports:
            exclude1 = exclude_port[0]
            exclude2 = exclude_port[1] + 1

            include1 = include_port[0]
            include2 = include_port[1] + 1

            exclude_range = range(exclude1, exclude2)
            include_range = range(include1, include2)

            if (set(exclude_range).issubset(set(include_range))):
                clear_ports = port_reducer(include_range, exclude_range)
                # print(clear_ports)
                for clear_port in clear_ports:
                    answer.append(clear_port)
            else:
                clear_counter = clear_counter + 1
                if clear_counter == clear_target:
                    answer.append(include_port)

    # answer.sort()
    return answer


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


test1 = apply_port_exclusions(include1, exclude1)

test2 = apply_port_exclusions(include2, exclude2)

test3 = apply_port_exclusions(include3, exclude3)

test4 = apply_port_exclusions(include4, exclude4)

test5 = apply_port_exclusions(include5, exclude5)


print("Test 1: ", test1)
print("Test 2: ", test2)
print("Test 3: ", test3)
print("Test 4: ", test4)
print("Test 5: ", test5)
