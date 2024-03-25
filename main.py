import os
from src.access_shift import retrieve_last_gateway_positions
from datetime import datetime
import matplotlib.pyplot as plt
from dotenv import load_dotenv


def shift_retrieval():
    # Day 17 time
    start_datetime = datetime(2023, 11, 17, 10, 0, 0)
    end_datetime = datetime(2023, 11, 17, 17, 0, 0)

    # Day 18 time
    start_datetime2 = datetime(2023, 11, 18, 10, 0, 0)
    end_datetime2 = datetime(2023, 11, 18, 17, 0, 0)

    # API information
    gateway_id = 187723572702721
    api_key = os.getenv("API_KEY")

    # Retrieve information from API for day 17
    positions_data = retrieve_last_gateway_positions(gateway_id, start_datetime, end_datetime, api_key)
    if positions_data:
        print("Positions data retrieved successfully.\n")

        # Count each beacon occurrence
        beacon_counts = count_beacon_ids(positions_data)
        # Iterate over the dictionary and print each key-value pair
        for beacon_id, count in beacon_counts.items():
            print(f"Beacon ID: {beacon_id}, Count: {count}")

        print("\n")
        # Time Average spent on each beacon
        total_time_spent = calculate_average_time_spent(positions_data)

        # Iterate over the beacon_counts dictionary to calculate and print the average time spent for each beacon_id
        for beacon_id, count in beacon_counts.items():
            average_time_spent = total_time_spent[beacon_id] / count
            print(f"Beacon ID: {beacon_id}, Average Time Spent: {average_time_spent}")

        # Matplot graphic for average time spent
        plot_average_time_spent(beacon_counts, total_time_spent)
    else:
        print("Failed to retrieve positions data: Weekend")

    # Retrieve information from API for day 18
    positions_data = retrieve_last_gateway_positions(gateway_id, start_datetime2, end_datetime2, api_key)
    if positions_data:
        print("Positions data retrieved successfully.\n")

        # Count each beacon occurrence
        beacon_counts = count_beacon_ids(positions_data)
        # Iterate over the dictionary and print each key-value pair
        for beacon_id, count in beacon_counts.items():
            print(f"Beacon ID: {beacon_id}, Count: {count}")

        print("\n")
        # Time Average spent on each beacon
        total_time_spent = calculate_average_time_spent(positions_data)

        # Iterate over the beacon_counts dictionary to calculate and print the average time spent for each beacon_id
        for beacon_id, count in beacon_counts.items():
            average_time_spent = total_time_spent[beacon_id] / count
            print(f"Beacon ID: {beacon_id}, Average Time Spent: {average_time_spent}")

        # Matplot graphic for average time spent
        plot_average_time_spent(beacon_counts, total_time_spent)
    else:
        print("Failed to retrieve positions data: Weekend")


def count_beacon_ids(beacon_data):
    beacon_counts = {}

    for entry in beacon_data:
        beacon_id = entry.get('beacon_id', None)
        if beacon_id:
            beacon_counts[beacon_id] = beacon_counts.get(beacon_id, 0) + 1

    return beacon_counts


def calculate_average_time_spent(data):
    # Call the count_beacon_ids function and store the result in a variable
    beacon_counts = count_beacon_ids(data)

    # Create a dictionary to store the total time spent for each beacon_id
    total_time_spent = {}

    # Iterate over the data to calculate the total time spent for each beacon_id
    for entry in data:
        beacon_id = entry['beacon_id']
        last_seen_at = entry['last_seen_at']
        seen_at = entry['seen_at']
        time_spent = last_seen_at - seen_at
        if beacon_id in total_time_spent:
            total_time_spent[beacon_id] += time_spent
        else:
            total_time_spent[beacon_id] = time_spent

    return total_time_spent


def plot_average_time_spent(beacon_counts, total_time_spent):
    beacon_ids = list(beacon_counts.keys())
    average_times = [total_time_spent[beacon_id] / beacon_counts[beacon_id] for beacon_id in beacon_ids]

    plt.figure(figsize=(10, 6))
    plt.bar(beacon_ids, average_times, color='skyblue')
    plt.xlabel('Beacon ID')
    plt.ylabel('Average Time Spent')
    plt.title('Average Time Spent per Beacon ID')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Create the results directory if it doesn't exist
    save_dir = os.path.join(os.path.dirname(__file__), 'results')
    os.makedirs(save_dir, exist_ok=True)

    # Save the plot in the results directory
    save_path = os.path.join(save_dir, 'average_time_spent.png')
    plt.savefig(save_path)
    plt.show()

if __name__ == "__main__":
    load_dotenv()
    shift_retrieval()
