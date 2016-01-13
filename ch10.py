# Look and Say sequence: 1, 11, 21, 1211, 111221, ...

def look(sequence):
    result = ''
    i = 0

    while i < len(sequence):
        counter = 1
        while i+counter < len(sequence) and sequence[i+counter] == sequence[i]:
            counter += 1
        result += str(counter) + sequence[i]
        i = i+counter

    return result


def look_say(position):
    result = '1'
    for i in range(position):
        result = look(result)
    
    return result

size = len(look_say(30))
print('Length of 30th element on the Look and Say sequence: {}'.format(size))