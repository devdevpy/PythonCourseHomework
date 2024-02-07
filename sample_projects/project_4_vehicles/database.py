import csv

db = []


from typing import List


def get_database() -> List:
    return db


def empty_database() -> None:
    global db
    db = []


def add_vehicle(make: str, model: str, year: int, color: str, range: float):
    db.append((make, model, year, color, range))


def delete_vehicle(id: int):
    db.pop(id)


def view_vehicle(id: int):
    return db[id]


def update_vehicle(id: int,
                make: str,
                model: str,
                year: int,
                color: str,
                range: float):
    db[id] = (make, model, year, color, range)


def export_data(filepath: str):
    with open(filepath, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in get_database():
            spamwriter.writerow(row)
