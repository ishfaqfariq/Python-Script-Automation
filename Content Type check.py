import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3

# Disable SSL warnings for insecure requests
urllib3.disable_warnings(InsecureRequestWarning)

def test_x_content_type_options(domain):
    try:
        # Send a HEAD request to the given domain, disabling SSL verification
        response = requests.head(domain, verify=False)

        # Print information about the domain and its status code
        print(f"\nDomain: {domain}")
        print(f"Status Code: {response.status_code}")

        # Check for 'X-Content-Type-Options' header in the response
        x_content_type_options = response.headers.get("X-Content-Type-Options")
        if x_content_type_options is None:
            print("X-Content-Type-Options header: Missing")
        elif x_content_type_options.lower() != "nosniff":
            print(f"X-Content-Type-Options header: {x_content_type_options} (not 'nosniff')")
        else:
            print("X-Content-Type-Options header: 'nosniff'")

    except requests.exceptions.SSLError as e:
        # Handle SSL verification errors
        print(f"SSL verification error: {e}")
    except Exception as e:
        # Handle other unexpected errors
        print(f"Error: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Example list of domains to test
    domain_list = [
        "https://mwebstaging.payactiv.com:443/",
        "https://webstaging.payactiv.com:443/",
        "https://authstaging.payactiv.com:443/?request_code=ee97792e-2ee9-46b5-b808-a1e8ef0a8034&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
        "https://helpos.payactiv.com:443/",
        "http://authstaging.payactiv.com:80/?request_code=f4f7a38b-d8a6-4c58-a603-345f2683058c&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
        "https://saml.payactiv.com:443/",
        "https://payactivate.payactiv.com:443/",
        "https://apiaus.payactiv.com:443/",
        "https://onshiftstaging.payactiv.com:443/",
        "https://hrisgateway.payactiv.com:443/index.html/",
        "https://analytica.payactiv.com:443/",
        "https://ivr.payactiv.com:443/",
        "https://mbrazil.payactiv.com:443/",
        "https://brazil.payactiv.com:443/",
        "https://mobileaus.payactiv.com:443/",
        "https://brazilapi.payactiv.com:443/",
        "https://aus.payactiv.com:443/",
        "https://help1.payactiv.com:443/",
    ]

    # Iterate through the list of domains and test each one
    for domain in domain_list:
        test_x_content_type_options(domain)
