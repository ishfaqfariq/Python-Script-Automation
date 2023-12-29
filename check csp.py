import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3

urllib3.disable_warnings(InsecureRequestWarning)


def check_csp(url):
    try:
        response = requests.get(url, verify=False)
        csp_header = response.headers.get("Content-Security-Policy")

        if csp_header:
            print(f"{url} has a Content Security Policy: {csp_header}")
        else:
            print(f"{url} does not have a Content Security Policy.")

    except requests.exceptions.SSLError as e:
        print(f"SSL verification error for {url}: {e}")
    except Exception as e:
        print(f"Error for {url}: {e}")


if __name__ == "__main__":
    # List of websites to check
    websites = [
        # "https://payactivate.payactiv.com:443/",
        # "https://aus.payactiv.com:443/",
        # "http://authstaging.payactiv.com:80/?request_code=f4f7a38b-d8a6-4c58-a603-345f2683058c&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
        # "https://onshiftstaging.payactiv.com/",
        # "https://hrisgateway.payactiv.com:443/index.html/",
        # "https://saml.payactiv.com:443/",
        # "https://brazilapi.payactiv.com:443/",
        # "https://authstaging.payactiv.com:443/?request_code=ee97792e-2ee9-46b5-b808-a1e8ef0a8034&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
        # "https://help1.payactiv.com:443/",
        # "https://apiaus.payactiv.com:443/",
        # "https://analytica.payactiv.com:443/",
        # "https://mbrazil.payactiv.com:443/",
        # "https://helpos.payactiv.com:443/",
        # "https://brazil.payactiv.com:443/",
        # "https://mobileaus.payactiv.com:443/",
        # "https://mwebstaging.payactiv.com:443/",
        # "https://webstaging.payactiv.com:443/",
        # # Add more websites as needed

        #29/12/2023 Ishfaq Fariq Same script additon of new Hosts to test 
        # new 1.1 additon of new hosts
        "https://payactivate.payactiv.com:443/",
        "https://d2c.payactiv.com:443/",
        "https://aus.payactiv.com:443/",
        "http://authstaging.payactiv.com:80/?request_code=6b0d32a4-435a-44b6-a087-96c67fe5c0ce&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
        "https://onshiftstaging.payactiv.com:443/",
        "https://hrisgateway.payactiv.com:443/index.html/",
        "https://saml.payactiv.com:443/",
        "https://brazilapi.payactiv.com:443/",
        "https://authstaging.payactiv.com:443/?request_code=67cd37a8-e0c4-40cd-850e-011bb6c86c82&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/",
        "http://proveredirection.payactiv.com/",
        "https://help1.payactiv.com:443/",
        "https://apiaus.payactiv.com:443/",
        "https://analytica.payactiv.com:443/",
        "https://mbrazil.payactiv.com:443/",
        "https://helpos.payactiv.com:443/",
        "https://brazil.payactiv.com:443/",
        "https://mobileaus.payactiv.com:443/",
        "https://mwebstaging.payactiv.com:443/",
        "https://webstaging.payactiv.com:443/",
    ]

    for website in websites:
        check_csp(website)
