import string

def right_justify(s):
    a=len(s)
    b=s.rjust(70-a,' ')
    print("the change string",b)


def main():
    s = input("Enter the string character")
    right_justify(s)


if __name__ == '__main__':
    main()