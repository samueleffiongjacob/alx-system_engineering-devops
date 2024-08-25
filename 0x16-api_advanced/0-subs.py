# #!/usr/bin/python3
# """Function to query subscribers on a given Reddit subreddit."""
# import requests


# def number_of_subscribers(subreddit):
#     """Return the total number of subscribers on a given subreddit."""
#     url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
#     headers = {
#         "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
#     }
#     response = requests.get(url, headers=headers, allow_redirects=False)
#     if response.status_code == 404:
#         return 0
#     elif response.status_code != 200:
#         # Handle other potential HTTP errors (e.g., 500, 403, etc.)
#         return 0
    
#     try:
#         data = response.json().get("data", {})
#         return data.get("subscribers", 0)
#     except ValueError:
#         # Handle JSON decoding errors
#         return 0



#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
