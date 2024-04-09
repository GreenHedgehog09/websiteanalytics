import csv
import time


def get_data_csv(path: str) -> list:
    data = []
    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if not i:
                continue
            variables = row[0].split(';')[:2]
            try:
                variables[0] = int(variables[0])
                variables[1] = int(variables[1])
            except ValueError as e:
                print(f'Error: Failed to convert type, {e}')
            data.append(variables)
    return data


def search_users(day1: list, day2: list) -> set:
    users_id = set()
    for row in day2:
        # Both days
        if row in day1:
            users_id.add(row[0])
        else:
            # Only second day
            users_id.add(row[0])
    return users_id


def main():
    file_day1 = '2024-04-08.csv'
    file_day2 = '2024-04-09.csv'
    # Get data
    data_day1 = get_data_csv(file_day1)
    data_day2 = get_data_csv(file_day2)
    print(f'Day 1 (user_id, product_id): {data_day1}')
    print(f'Day 2 (user_id, product_id): {data_day2}')
    # Search
    result = search_users(data_day1, data_day2)
    print(f'Users id: {result}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'Duration: {time.time() - start_time}')