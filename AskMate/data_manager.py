import connection
from _datetime import datetime

def display_info(filename):
    data = connection.read_file(filename)
    for row in data:
        row['view_number'] = int(row['view_number'])
        row['vote_number'] = int(row['vote_number'])
        row['submission_time'] = float(row['submission_time'])
        row['submission_time'] = datetime.utcfromtimestamp(float(row['submission_time'])).strftime('%Y-%m-%d %H:%M:%S')
    return data

def display_anw(filename):
    data = connection.read_anwsers(filename)
    for row in data:
        row['vote_number'] = int(row['vote_number'])
        row['submission_time'] = float(row['submission_time'])
        row['submission_time'] = datetime.utcfromtimestamp(float(row['submission_time'])).strftime('%Y-%m-%d %H:%M:%S')
    return data

