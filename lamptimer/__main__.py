import argparse
import datetime
from lamptimer import print_days_and_times_for_lamp_change

def main(args=None):
    parser = create_parser()

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    if not validate_date_pair(args.from_date, args.to_date):
        msg = "The From Date must be before, or equal to, the To Date"
        parser.error(msg)

    print args
    # print_days_and_times_for_lamp_change(from_month,to_month,year)

def create_parser():
    parser = argparse.ArgumentParser()
    date_help = 'a valid date of the form YYYY-MM'
    parser.add_argument('from_date', help=date_help, type=valid_date)
    parser.add_argument('to_date', help=(date_help + ". NOTE: date must be greater than or equal to the from_date"), type=valid_date)
    return parser

def valid_date(string):
    try:
        date = datetime.datetime.strptime(string, '%Y-%m')
    except ValueError:
        msg = "%r is not a valid date. Dates should be of the form YYYY-MM" % string
        raise argparse.ArgumentTypeError(msg)
    else:
        return date

def validate_date_pair(from_date, to_date):
    return from_date <= to_date

if __name__ == "__main__":
    main()
