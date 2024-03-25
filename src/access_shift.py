import requests

def retrieve_last_gateway_positions(gateway_id, start_datetime, end_datetime, api_key):
    """
    Retrieve last gateway positions from the API endpoint.

    Args:
    - gateway_id (int): Gateway ID.
    - start_datetime (datetime): Start datetime object.
    - end_datetime (datetime): End datetime object.
    - api_key (str): API key for authentication.

    Returns:
    - dict: Last gateway positions retrieved from the API.
    """
    # Convert datetime objects to timestamps
    start_timestamp = int(start_datetime.timestamp())
    end_timestamp = int(end_datetime.timestamp())

    # Endpoint URL
    endpoint = f"https://ivt-api.azitek.io/position_logs/{gateway_id}/{start_timestamp}"

    # Request parameters
    params = {
        "timestamp_end": end_timestamp
    }

    # Headers
    headers = {
        "X-Api-Key": api_key
    }

    # Make GET request
    response = requests.get(endpoint, params=params, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        positions_data = response.json()
        return positions_data
    else:
        print(f"Failed to retrieve positions data. Status code: {response.status_code}")
        return None