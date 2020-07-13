def get_parsed_value_to_int_or_none(number):
    try:
        return int(number)
    except (ValueError, TypeError):
        return
