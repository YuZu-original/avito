from datetime import date


def calculate_age(born: date):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    # raised when birthdate is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)
    return today.year - born.year - 1 if birthday > today else today.year - born.year
