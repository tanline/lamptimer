import sys
from lamptimer import print_days_and_times_for_lamp_change

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print args
    print_days_and_times_for_lamp_change(9,12,2016)

if __name__ == "__main__":
    main()
