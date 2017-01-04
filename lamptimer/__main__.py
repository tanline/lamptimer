import argparse
import datetime
from .lamptimer import LampTimer

def main(args=None):
    args = parse_and_validate_args(args)
    lamptimer = LampTimer('Toronto', args.from_date, args.to_date, args.shutoff_after)
    print_times_for_lamp_change(lamptimer, args.with_dusk)

def parse_and_validate_args(args):
    parser = create_parser()

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    if not validate_date_pair(args.from_date, args.to_date):
        msg = 'The From Date must be before, or equal to, the To Date'
        parser.error(msg)

    return args

def create_parser():
    description_str = ('Calculate on and off times for an outdoor lamp,'
                       ' based off the time of dusk.')

    parser = argparse.ArgumentParser(description=description_str)

    from_date_help = 'The start of the range. A date of the form YYYY-MM.'
    to_date_help = ('The end of the range. '
                    'A date of the form YYYY-MM. '
                    'It must be greater than or equal to the from_date.')
    parser.add_argument('from_date', help=from_date_help, type=valid_date)
    parser.add_argument('to_date', help=to_date_help, type=valid_date)

    parser.add_argument('--with-dusk', action='store_true', help='show time of dusk in ouput')

    shutoff_help = 'how many hours the lamp should stay on for. defaults to 4'
    parser.add_argument('--shutoff-after', help=shutoff_help, default=4, type=int)

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

def print_times_for_lamp_change(lamptimer, with_dusk):
    str_format = '{}'

    if with_dusk:
        print 'Date, Dusk Time, Timer On, Timer Off'
        str_format = '{:with-dusk}'
    else:
        print 'Date, Timer On, Timer Off'

    for day in lamptimer.days_for_lamp_change():
        print str_format.format(day)

if __name__ == "__main__":
    main()
