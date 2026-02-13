import requests
import json
import os


def get_github_user_activity(username, token=None):
    """
    Fetches and displays public GitHub activity for a given user.
    A personal access token is recommended to avoid rate limits.
    """
    url = f"https://api.github.com{username}/events/public"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        events = response.json()

        print(f"--- Recent Public Activity for {username} ---")
        for event in events[:10]:  # Displaying the last 10 events
            created_at = event['created_at']
            event_type = event['type']
            repo_name = event['repo']['name']
            print(f"- [{created_at}] {event_type} on {repo_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")


if __name__ == "__main__":
    # Replace 'YOUR_USERNAME' with the GitHub username you want to check
    # and set the GITHUB_TOKEN environment variable for authentication.
    github_username = "google"  # Example username
    # Get token from environment variable (recommended)
    github_token = os.environ.get("GITHUB_TOKEN")

    if not github_token:
        print("Warning: GITHUB_TOKEN environment variable not set. Proceeding without token (might hit rate limits).")

    get_github_user_activity(github_username, github_token)

