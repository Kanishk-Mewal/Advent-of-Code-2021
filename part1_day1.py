def main():
    count = 0
    x = 0
    y = 0
    for i in range(2000):
        y = int(input())
        if(y-x != y):
            if(y > x):
                count+=1
        x = y
    print(count)

main()
