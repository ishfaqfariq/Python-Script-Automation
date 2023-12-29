import requests

def check_https_enforcement(host):
    # Send an HTTP GET request to the host
    response = requests.get(host, allow_redirects=False)

    # Check if the server responds with a redirect to HTTPS (HTTP status code 301 or 302)
    if response.status_code in [301, 302] and response.headers.get("Location", "").startswith("https://"):
        return True
    else:
        return False

if __name__ == "__main__":
    # List of hosts to check
    hosts = ["http://proveredirection.payactiv.com/", 
             "http://authstaging.payactiv.com:80/?request_code=6b0d32a4-435a-44b6-a087-96c67fe5c0ce&client_id=authModuleWeb&is_popup=False&login_mode=0&background_request=False/"
            ]

    for host in hosts:
        try:
            if check_https_enforcement(host):
                print(f"{host}: Enforces HTTPS")
            else:
                print(f"{host}: Does not enforce HTTPS")
        except requests.exceptions.RequestException as e:
            print(f"Error checking {host}: {e}")



