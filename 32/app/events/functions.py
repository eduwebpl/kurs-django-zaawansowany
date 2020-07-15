from datetime import timedelta


def get_dates_for_range(date_from, date_to):
    assert date_from <= date_to

    start_date = date_from
    while start_date <= date_to:
        yield start_date
        start_date = start_date + timedelta(days=1)
