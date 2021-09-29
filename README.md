# exrates

A command line tool for currency conversion and provide with historical exchange rate.

## Usage
```
exrates history --start 2021-02-01 --end 2021-02-02 --base USD --symbol EUR CAD
exrates convert --date 2021-02-01 --base USD --symbol EUR --amount 50
```

There are 2 commands:
#### 1. `history` - Historical exchange rate for currencies 
- `--help` - displays help and usage
- `--start` - the start date, default today.
- `--end` - the end date, default today.
- `--base` - the base currency, default USD.
- `--symbol` - the list of currency symbols to convert to (space separated), required.
- `--output` - the file name to write the output to, optional.

#### 2. `convert` - Convert amount for currencies
- `--help` - displays help and usage
- `--date` - the currency exchange date, default today.
- `--base` - the base currency, default USD.
- `--symbol` - the currency symbol to convert to, required.
- `--amount` - the amount to convert, required.

## Installation
#### Step 1. Git clone repo to local
```
git clone https://github.com/hmadhwa1/cli-exchange-rates.git
```
#### Step 2. cd in repo folder.
```
cd cli-exchange-rates
```
#### Step 3. Execute command as
```
pip install -e .
```

#### As Developer/Contributor
```
pip install -e .[dev]
```
For enhancements please raise an issue/PR.
