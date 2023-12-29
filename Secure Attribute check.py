import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3

# Suppress only the InsecureRequestWarning caused by unverified HTTPS requests
urllib3.disable_warnings(InsecureRequestWarning)

# List of URLs to test
urls = [
    "https://aus.payactiv.com/",
    "https://mobileaus.payactiv.com/",
    "https://authstaging.payactiv.com:443/?request_code=ee97792e-2ee9-46b5-b808-a1e8ef0a8034&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False",
    "https://accounts.payactiv.com/",
    "https://brazil.payactiv.com/",
    "https://onshiftstaging.payactiv.com/",
    "http://authstaging.payactiv.com:80/?request_code=f4f7a38b-d8a6-4c58-a603-345f2683058c&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
]

for url in urls:
    try:
        # Make a request to the website with SSL certificate verification disabled
        response = requests.get(url, verify=False)

        # Check if the 'Set-Cookie' header is present and missing the 'Secure' attribute
        if (
            "Set-Cookie" in response.headers
            and "Secure" not in response.headers["Set-Cookie"]
        ):
            print(f"Session cookie for {url} is missing 'Secure' attribute.")
        else:
            print(f"Session cookie for {url} has 'Secure' attribute or is not present.")
    except requests.exceptions.SSLError as e:
        print(f"SSL verification error for {url}: {e}")
    except Exception as e:
        print(f"Error for {url}: {e}")
