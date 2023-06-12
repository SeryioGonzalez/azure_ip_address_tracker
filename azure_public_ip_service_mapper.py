import ipaddress
import json
import os
import sys

ip_address=sys.argv[1]

try:
    ip_address_of_interest=ipaddress.ip_address(ip_address)
except:
    print("ERROR: IP Address {} is not valid".format(ip_address))
    sys.exit(1)

json_ip_files = [file_name for file_name in os.listdir('.') if 'ServiceTags_Public_20' in file_name ]
json_ip_files.sort(reverse=True)
latest_json_ip_file = json_ip_files[0]

file_pointer = open(latest_json_ip_file)
json_data = json.load(file_pointer)

ip_address_range_list=[]

# Iterating through the json
for service_range in json_data['values']:

    service_range_name = service_range['name']
    service_region     = service_range['properties']['region']
    if service_region == '':
        service_region = 'Global'

    service_prefixes   = service_range['properties']['addressPrefixes']

    for service_prefix in service_prefixes:
        ip_network_prefix=ipaddress.ip_network(service_prefix)
        ip_range={'ip_network_range': ip_network_prefix, 'service_range_name': service_range_name, 'service_region':service_region}
        ip_address_range_list.append(ip_range)

file_pointer.close()
  
potential_ranges = [ range for range in ip_address_range_list if ip_address_of_interest in range['ip_network_range']]

for potential_range in potential_ranges:
    print('IP: {} in service: {} in region: {}'.format(ip_address_of_interest, potential_range['service_range_name'], potential_range['service_region']))

