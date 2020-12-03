# Write a function that
# takes two lists as input and produces one list as output.
# The function should have the signature `def apply_port_exclusions(include_ports, exclude_ports)`.
# The function should expect that the input lists will be a list of low-high pairs which are lists of length two.
# The function should return a minimized and
# ordered list of include port ranges that result after processing the exclude port ranges.
# Include whatever tests and comments you normally provide for completed code.
# Helper Function to try to remove duplicate excludes


def apply_port_exclusions(include_ports, exclude_ports):

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
