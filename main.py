from src.access_shift import retrieve_last_gateway_positions
from datetime import datetime


def shift_retrieval():
    start_datetime = datetime(2023, 11, 17, 10, 0, 0)
    end_datetime = datetime(2023, 11, 17, 17, 0, 0)

    start_datetime2 = datetime(2023, 11, 18, 10, 0, 0)
    end_datetime2 = datetime(2023, 11, 18, 17, 0, 0)

    gateway_id = 187723572702721
    api_key = "4a47cf7cae0e9ffc6eb19404aaeb96b10f986f82ec2536afc1fcbe677ccff625"

    positions_data = retrieve_last_gateway_positions(gateway_id, start_datetime, end_datetime, api_key)
    if positions_data:
        print("Positions data retrieved successfully.")
        #print(positions_data)

        beacon_counts = count_beacon_ids(positions_data)
            # Iterate over the dictionary and print each key-value pair
        for beacon_id, count in beacon_counts.items():
            print(f"Beacon ID: {beacon_id}, Count: {count}")
    else:
        print("Failed to retrieve positions data: Weekend")

    positions_data = retrieve_last_gateway_positions(gateway_id, start_datetime2, end_datetime2, api_key)
    if positions_data:
        print("Positions data retrieved successfully.")
        #print(positions_data)

        beacon_counts2 = count_beacon_ids(positions_data)
        # Iterate over the dictionary and print each key-value pair
        for beacon_id, count in beacon_counts2.items():
            print(f"Beacon ID: {beacon_id}, Count: {count}")

    else:
        print("Failed to retrieve positions data: Weekend")


def count_beacon_ids(beacon_data):
    beacon_counts = {}

    for entry in beacon_data:
        beacon_id = entry.get('beacon_id', None)
        if beacon_id:
            beacon_counts[beacon_id] = beacon_counts.get(beacon_id, 0) + 1

    return beacon_counts


if __name__ == "__main__":
    shift_retrieval()
