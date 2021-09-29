import os


def test_entrypoint(capsys):
    exit_status = os.system('exrates --help')
    out, err = capsys.readouterr()

    assert exit_status == 0
    assert out in "--help"
    assert out in "usage: exrates < command > [ < args >]"


def test_history_entrypoint(capsys):
    exit_status = os.system('exrates history --help')
    out, err = capsys.readouterr()

    assert exit_status == 0
    assert out in "--help"
    assert out in "exrates history --start 2021-02-01 --end 2021-02-02 --base USD --symbol EUR CAD"


def test_convert_entrypoint(capsys):
    exit_status = os.system('exrates convert --help')
    out, err = capsys.readouterr()

    assert exit_status == 0
    assert out in "exrates convert --date 2021-02-01 --base USD --symbol EUR --amount 50"


def test_history_success(capsys):
    exit_status = os.system('exrates history --symbol INR --start 2021-09-27 --end 2021-09-27 --base USD')
    out, err = capsys.readouterr()

    assert exit_status == 0
    assert out in "{'amount': 1.0, 'base': 'USD', 'start_date': '2021-09-27', 'end_date': '2021-09-27', 'rates': {'2021-09-27': {'INR': 73.859}}}\n"


def test_convert_success(capsys):
    exit_status = os.system('exrates convert --symbol INR --amount 1.0 --base USD --date 2021-09-28')
    out, err = capsys.readouterr()

    assert exit_status == 0
    assert out in "{'amount': 1.0, 'base': 'USD', 'date': '2021-09-28', 'rates': {'INR': 74.122}}\n"


def test_history_raises_exception(capsys):
    exit_status = os.system('exrates history --symbol AAA')
    out, err = capsys.readouterr()

    assert exit_status == 1
    assert err in "Exception: Something went wrong! Please try again with different input"


def test_convert_raises_exception(capsys):
    exit_status = os.system('exrates convert --symbol AAA --amount 1.0 --base USD --date 2021-09-28')
    out, err = capsys.readouterr()

    assert exit_status == 1
    assert err in "Exception: Something went wrong! Please try again with different input"


def test_history_invalid_date(capsys):
    exit_status = os.system('exrates history --symbol INR --start 2021-09-28 --end 2021-09-27 --base USD')
    out, err = capsys.readouterr()

    assert exit_status == 1
    assert err in "Exception: Invalid date, start date cannot be greater than end date"


def test_convert_invalid_amount(capsys):
    exit_status = os.system('exrates convert --symbol INR --amount xyz --base USD --date 2021-09-28')
    out, err = capsys.readouterr()

    assert exit_status == 1
    assert err in "Invalid amount, amount must be integer/float"


def test_convert_invalid_date(capsys):
    exit_status = os.system('exrates convert --symbol INR --amount 10 --base USD --date 2021-13-28')
    out, err = capsys.readouterr()

    assert exit_status == 1
    assert err in "Incorrect data format, should be YYYY-MM-DD"


def test_history_invalid_start_date(capsys):
    exit_status = os.system('exrates history --symbol INR --start 2021-27 --end 2021-09-28 --base USD')
    out, err = capsys.readouterr()

    assert exit_status == 1
    assert err in "Incorrect data format, should be YYYY-MM-DD"


def test_history_invalid_end_date(capsys):
    exit_status = os.system('exrates history --symbol INR --start 2021-09-aa --end 2021-09-28 --base USD')
    out, err = capsys.readouterr()

    assert exit_status == 1
    assert err in "Incorrect data format, should be YYYY-MM-DD"
