import argparse
import datetime
from .lamptimer import LampTimer

def main(args=None):
    parser = create_parser()

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    if not validate_date_pair(args.from_date, args.to_date):
        msg = "The From Date must be before, or equal to, the To Date"
        parser.error(msg)

    lamptimer = LampTimer('Toronto', args.from_date, args.to_date)
    if args.only_rounded:
        print_rounded_times_for_lamp_change(lamptimer)
    else:
        print_times_for_lamp_change(lamptimer)

def create_parser():
    parser = argparse.ArgumentParser()
    from_date_help = 'a valid date of the form YYYY-MM'
    parser.add_argument('from_date', help=from_date_help, type=valid_date)
    to_date_help = from_date_help + ". NOTE: date must be greater than or equal to the from_date"
    parser.add_argument('to_date', help=to_date_help, type=valid_date)
    parser.add_argument('--only-rounded', action='store_true')
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

def print_times_for_lamp_change(lamptimer):
    print 'Date, Dusk Time, Rounded Dusk Time'
    for day in lamptimer.days_for_lamp_change():
        print '{}'.format(day)

def print_rounded_times_for_lamp_change(lamptimer):
    print 'Date, Dusk Time'
    for day in lamptimer.days_for_lamp_change():
        print '{:only-rounded}'.format(day)

if __name__ == "__main__":
    main()
