# Public IP Address checker

This script get an IP Address as an input and returns the Azure Public IP Ranges to which this IP belongs.
It is useful for troubleshooting private link issues.

```
#CHECK PYTHON DEPENDENCIES
$ python azure_public_ip_service_mapper.py "40.80.59.34"
IP: 40.80.59.34 in service: AzurePortal in region: Global
IP: 40.80.59.34 in service: AzurePortal.JapanWest in region: japanwest
IP: 40.80.59.34 in service: AzureCloud.japanwest in region: japanwest
IP: 40.80.59.34 in service: AzureCloud in region: Global
```

The script will get the latest Azure Public IP Range file available in the installation folder and use it.
If you want a more recent file, download it to the base directory
Azure Public IP range files are JSON based, which the following naming pattern:

```
$ ls -1 *.json
ServiceTags_Public_20220919.json
ServiceTags_Public_20230605.json
```