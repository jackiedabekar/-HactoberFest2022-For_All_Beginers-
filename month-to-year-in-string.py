def convert_months_to_years_months_string(months):
    if not months:
        return
    period = get_years_and_months_int(months)
    year = 'year '
    month = 'month'
    if int(period[0]) > 1:
        year = 'years '
    if int(period[1]) > 1:
        month ='months'

    total = ''
    if period[0] > 0:
        total += period[0]+year
    if period[1] > 0:
        total += period[1]+month
    return tota
