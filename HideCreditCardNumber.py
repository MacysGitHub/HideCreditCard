def hidecreditcard():
    print("Enter Credit Card Number")
    ccnumber = input()
    if(len(ccnumber) != 16):
        print("Card number not 16 characters!")
        exit(-1)
    iterator = 12
    hidecc = "*" * 12
    arr = []
    splitcc = ccnumber.split()
    for i in splitcc:
        arr += i

    while(iterator < 16):
        hidecc += arr[iterator]
        iterator += 1
    print("Credit Card Number: ", hidecc)


def main():
    hidecreditcard()


main()