from datetime import datetime


def date_adjustment(date):
    data = date.split('/')
    br_data = f'{data[1]}/{data[0]}/{data[2]}'
    ajusted_data = datetime.strptime(br_data, "%d/%m/%y")

    return ajusted_data.strftime("%d/%m")