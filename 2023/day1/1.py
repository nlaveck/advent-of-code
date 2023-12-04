
def calibrate(line: str):
    number = ''

    for c in line:
        if '0' <= c <= '9':
            number += c
            break
    for c in line[::-1]:
        if '0' <= c <= '9':
            number += c
            break
    return int(number)
    


sum = 0
with open("input.txt", "r") as inFile:
    while line := inFile.readline():
        sum += calibrate(line)
print(sum)
