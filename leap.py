import sys

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    year = int(sys.argv[1])   # take argument
    if is_leap_year(year):
        print("Leap Year")
    else:
        print("Not a Leap Year")
