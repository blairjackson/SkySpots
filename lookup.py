def lookup(file):
    for line in file:
        line = barbCheck(line[0])
        return line


def barbCheck(barbCode):
    #replace barb code with channel name
    with open('barbcodes') as codes:
        if len(barbCode) > 6:
            barbCode = barbCode[1:]
        for line in codes:
            code = line.split(',')
            if code[0] == barbCode:
                return code[1]
