import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3

urllib3.disable_warnings(InsecureRequestWarning)

def check_hsts(domain):
    try:
        # Make an HTTPS request to the domain
        response = requests.get(domain, verify=False, timeout=5)

        # Check if the HSTS header is present in the response
        hsts_header = response.headers.get('Strict-Transport-Security', '')

        # Check if 'max-age' and 'includeSubDomains' are present in the HSTS header
        return 'max-age' in hsts_header and 'includeSubDomains' in hsts_header

    except requests.exceptions.SSLError as e:
        print(f"SSL verification error for {domain}: {e}")
    except Exception as e:
        print(f"Error for {domain}: {e}")


def main():
    # List of domains to check
    domains = [
        "https://help1.payactiv.com:443/",
        "https://apiaus.payactiv.com:443/",
        "https://lbgroup.payactiv.com:443/",
        "https://hrisgateway.payactiv.com:443/index.html/",
        "https://aus.payactiv.com:443/",
        "https://brazil.payactiv.com:443/",
        "https://connect.payactiv.com:443/",
        "https://webstaging.payactiv.com:443/",
        "https://ivr.payactiv.com:443/",
        "https://hrisgateway.payactiv.com:443/index.html/",
        "https://analytica.payactiv.com:443/",
        "https://quickbooks.payactiv.com:443/",
        "https://mwebstaging.payactiv.com:443/",
        "https://payactivate.payactiv.com:443/",
        "https://adp.payactiv.com:443/",
        "https://saml.payactiv.com:443/",
        "https://mbrazil.payactiv.com:443/",
        "https://helpos.payactiv.com:443/",
        "https://onshiftstaging.payactiv.com:443/",
        "https://brazilapi.payactiv.com:443/",
        "https://ukgwallet.payactiv.com:443/",
        "https://authstaging.payactiv.com:443/?request_code=ee97792e-2ee9-46b5-b808-a1e8ef0a8034&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
        "https://proveredirection.payactiv.com/",
        "https://mobileaus.payactiv.com:443/",
    ]

    # Iterate through each domain and check HSTS
    for domain in domains:
        # Check HSTS for the current domain
        hsts_enabled = check_hsts(domain)

        # Print the result for each domain
        if hsts_enabled:
            print(f'HSTS is enabled for {domain}')
        else:
            print(f'HSTS is not enabled for {domain}')

if __name__ == "__main__":
    main()
