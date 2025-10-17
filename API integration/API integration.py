import requests
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Base URL of the API
API_BASE_URL = "https://api.example.com/v1"
API_KEY = "your_api_key_here"

# Default headers
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}


def send_request(method, endpoint, payload=None, params=None, retries=3):
    """
    Send a request to the API with retries and error handling.
    """
    url = f"{API_BASE_URL}{endpoint}"
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"{method} Request to {url} (Attempt {attempt})")
            response = requests.request(method, url, headers=HEADERS, json=payload, params=params)

            if response.ok:
                logging.info(f"Success: {response.status_code}")
                return response.json()
            else:
                logging.warning(f"Failed with status code {response.status_code}: {response.text}")
        except requests.RequestException as e:
            logging.error(f"Request exception: {e}")
        
        time.sleep(2)  # Wait before retry

    logging.error("Max retries exceeded.")
    return None


def get_resource(resource_id):
    """GET a specific resource"""
    endpoint = f"/resources/{resource_id}"
    return send_request("GET", endpoint)


def list_resources(query_params=None):
    """GET a list of resources with optional filters"""
    endpoint = "/resources"
    return send_request("GET", endpoint, params=query_params)


def create_resource(data):
    """POST to create a new resource"""
    endpoint = "/resources"
    return send_request("POST", endpoint, payload=data)


def update_resource(resource_id, data):
    """PUT to update an existing resource"""
    endpoint = f"/resources/{resource_id}"
    return send_request("PUT", endpoint, payload=data)


def delete_resource(resource_id):
    """DELETE a resource"""
    endpoint = f"/resources/{resource_id}"
    return send_request("DELETE", endpoint)


# Example usage
if __name__ == "__main__":
    # List all resources
    resources = list_resources()
    print("Resources:", resources)

    # Create a new resource
    new_data = {"name": "Test Item", "value": 100}
    new_resource = create_resource(new_data)
    print("Created:", new_resource)

    # Update the resource
    if new_resource:
        updated_data = {"name": "Updated Item", "value": 150}
        updated = update_resource(new_resource.get("id"), updated_data)
        print("Updated:", updated)

    # Delete the resource
    if new_resource:
        deleted = delete_resource(new_resource.get("id"))
        print("Deleted:", deleted)
