import ipaddress
import sys
import requests
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Test the function
ip_address = input("Enter an IP address: ")
if is_valid_ip(ip_address):
    pass
else:
    print(f"\n{ip_address} is-------------invalid ip\n")
    print("exiting...\n")
    exit()

#end of test validity
    

address = ipaddress.ip_address(ip_address)
if is_valid_ip(ip_address):
    pass
else:
    print(f"\n{ip_address} -------------invalid ip\n")

if address.is_global:
    print(f"\n {ip_address} -------------global ip\n")

elif address.is_loopback:
    print(f"\n{ip_address} -------------loopback ip\n")
    sys.exit()

elif address.is_private:
    print(f"\n{ip_address} -------------private\n")
    sys.exit()


def get_location(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data.get('loc')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        return f"Location: {location}, City: {city}, Region: {region}, Country: {country}"
    else:
        return "Failed to retrieve location information."
location_info = get_location(ip_address)
print(location_info)
