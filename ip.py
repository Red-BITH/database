rabite = input("İP daxil et")
url = "https://ipinfo.io/" + rabite
response = urlopen(url)
data = json.load(response)
table_data = [
       ["IP", data["ip"]],
       ["city", data["city"]],
       ["Region", data["region"]],
       ["Country", data["country"]],
       ["Postal Code", data["postal"]],
       ["Organization", data["org"]],
       ["ASN", data.get("asn", ["N/A"])[0]],
       ["IP Range", data.get("ip_range", "N/A")],
       ["Local Time", data.get("timezone", "N/A")],
       ["Timezone", data.get("timezone", "N/A")],
       ["Coordinates", data.get("loc", "N/A")],
       ["Privacy Detection", data.get("privacy", "N/A")]
       ]
      
from tabulate import tabulate
table = tabulate(table_data, headers=["Field", "Value"], tablefmt="grid")
print_colored(table, Colors.BLUE)
