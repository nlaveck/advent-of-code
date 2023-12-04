digits = {'one': '1', 'two': '2', 'three': '3', 'four':'4', 'five':'5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def calibrate(line: str):
    firstDigit = [999999, 'x']
    secondDigit = [999999,'x']

    for i, c in enumerate(line):
        if '0' <= c <= '9':
            firstDigit[0] = i
            firstDigit[1] = c
            break
    for i, c in enumerate(line[::-1]):
        if '0' <= c <= '9':
            secondDigit[0] = i
            secondDigit[1] = c
            break

    rev_line = line[::-1]
    for (k, v) in digits.items():
        try:
            idx = line.index(k)
        except:
            idx = -1
        if -1 < idx < firstDigit[0]:
            firstDigit[0] = idx
            firstDigit[1] = v
        try:
            idx2 = rev_line.index(k[::-1])
        except:
            idx2 = -1
        if -1 < idx2 < secondDigit[0]:
            secondDigit[0] = idx2
            secondDigit[1] = v
    return int(firstDigit[1] + secondDigit[1])
    


sum = 0
with open("input2.txt", "r") as inFile:
    while line := inFile.readline():
        res = calibrate(line)
        print(res)
        sum += res
print(sum)
