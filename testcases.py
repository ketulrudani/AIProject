import random

def main():
    n=int(input("enter value of n"))
    f = open(str(n)+"QueensTest.txt", "wb")
    testCaseCount = 1000
    board = ""
    while testCaseCount > 0:
        testCaseCount -= 1
        for col in range(0,n-1):
            board += str(random.randint(0,n-1)) + ' '
        board += str(random.randint(0,n-1)) + '\n'
    f.write(board)
    f.close()
    
if __name__ == '__main__':
    main()