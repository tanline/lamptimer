import sys
from lamptimer import print_days_and_times_for_lamp_change

# Arguments are as followed:
# lamptimer from-month to-month year
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if len(args) == 0:
        print 'usage: lamptimer from-month to-month year'
        return

    from_month = int(args[0])
    to_month = int(args[1])
    year = int(args[2])

    print_days_and_times_for_lamp_change(from_month,to_month,year)

if __name__ == "__main__":
    main()
