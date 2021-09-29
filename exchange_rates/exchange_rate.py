import argparse
import json
import sys
from datetime import date, datetime

import requests


class ExchangeRate:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Performs currency conversion and provide with historical exchange rate",
            usage='''exrates <command> [<args>]
        
        Commands used for exchange rate class:
        history    Display the historical exchange rate for the base currency to required currency for a particular date range
        convert    Converts the rate for a amount from base currency to required currency ''')

        parser.add_argument('command', help='Command to run')

        # print(sys.argv[1:2])
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized command")
            parser.print_help()
            exit(1)

        getattr(self, args.command)()
        exit(0)

    def history(self):
        parser = argparse.ArgumentParser(description="Historical exchange rate for currencies",
                                         usage="please run this command for e.g. exrates history --start 2021-02-01 "
                                               "--end 2021-02-02 --base USD --symbol EUR CAD")

        parser.add_argument("--start", help="YYYY-MM-DD e.g: 2021-12-30", default=date.today().strftime('%Y-%m-%d'))
        parser.add_argument("--end", help="YYYY-MM-DD e.g: 2021-12-30", default=date.today().strftime('%Y-%m-%d'))
        parser.add_argument("--base", help="e.g: INR", default='USD')
        parser.add_argument("--symbol", nargs='+', help="e.g. INR EUR USD")
        parser.add_argument("--output", nargs='?', help="Enter the output file name e.g. historicalExchangeRate")

        args = parser.parse_args(sys.argv[2:])

        try:
            datetime.strptime(args.start, '%Y-%m-%d')
            datetime.strptime(args.end, '%Y-%m-%d')
        except ValueError:
            raise SystemExit("Incorrect data format, should be YYYY-MM-DD")

        if args.start > args.end:
            raise SystemExit("Invalid date, start date cannot be greater than end date")

        try:
            sym = ','.join(args.symbol)
            url = f"https://api.frankfurter.app/{args.start}..{args.end}?from={args.base}&to={sym}"
            response = requests.get(url)

            if args.output is None:
                print(response.json())
            else:
                with open(args.output + '.json', 'w', encoding='utf-8') as f:
                    json.dump(response.json(), f, ensure_ascii=False, indent=4)

        except Exception:
            raise SystemExit("Something went wrong! Please try again with different input")

    def convert(self):
        parser = argparse.ArgumentParser(description="Convert amount for currencies",
                                         usage="please run this command for e.g. exrates convert --date 2021-02-01 "
                                               "--base USD --symbol EUR --amount 50")

        parser.add_argument("--date", help="YYYY-MM-DD e.g: 2021-12-30", default=date.today().strftime('%Y-%m-%d'))
        parser.add_argument("--base", help="e.g: USD", default='USD')
        parser.add_argument("--symbol", help="e.g. INR")
        parser.add_argument("--amount", help="e.g 50")

        args = parser.parse_args(sys.argv[2:])

        try:
            amt = float(args.amount)
        except ValueError:
            raise SystemExit("Invalid amount, amount must be integer/float")

        try:
            datetime.strptime(args.date, '%Y-%m-%d')
        except ValueError:
            raise SystemExit("Incorrect data format, should be YYYY-MM-DD")

        try:
            url = f"https://api.frankfurter.app/{args.date}?from={args.base}&to={args.symbol}&amount={amt}"
            response = requests.get(url)
            print(response.json())
        except Exception:
            raise SystemExit("Something went wrong! Please try again with different input")


if __name__ == '__main__':
    ExchangeRate()
