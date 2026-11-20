import requests
import os
import time
import csv
from dotenv import load_dotenv

load_dotenv()

Api_url = os.getenv("API_URL")

if not Api_url:
    raise ValueError("Api url not found in .env")


def getapi(url, page, limit):
    params = {"_page": page, "_limit": limit}

    try:
        for attempt in range(3):
            response = requests.get(url, params=params, timeout=10)

            response.raise_for_status()

            data = response.json()

            return data
    except requests.exceptions.Timeout:
        timeout = 2**attempt
        print(f"Retrying after {timeout} seconds")

        time.sleep(timeout)


all_users = []
page = 1
limit = 4

try:
    while True:
        users = getapi(Api_url, page, limit)

        if not users:
            break

        all_users.extend(users)

        print(f"{page} has {len(users)} length of data")

        page += 1
except requests.exceptions.RequestException as error:
    print("Error in fetching the data as error occured", error)

print("Total records extracted:", len(all_users))

with open("users.csv", "w") as file:
    fieldname = ["id", "name", "username", "email", "city", "zipcode"]
    writer = csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()

    for ele in all_users:
        writer.writerow(
            {
                "id": ele["id"],
                "name": ele["name"],
                "username": ele["username"],
                "email": ele["email"],
                "city": ele["address"]["city"],
                "zipcode": ele["address"]["zipcode"],
            }
        )
