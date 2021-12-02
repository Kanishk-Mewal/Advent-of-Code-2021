def main():
    horizontal = 0
    down = 0
    aim = 0
    for i in range(1000):
        str1 = str(input())
        if("down" in str1):
            aim += int(str1[4:])
        if("up" in str1):
            aim -= int(str1[2:])
        if("forward" in str1):
            horizontal += int(str1[8:])
            down += aim*int(str1[8:])


    print("horizontal: ", horizontal)
    print("aim:", aim)
    print("down: ", down)

main()
