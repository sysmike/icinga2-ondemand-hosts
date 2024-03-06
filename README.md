# icinga2-ondemand-hosts

### What does it do?

This script checks if certain hosts have turned on and enables them in Icinga2 using the API.

### How to run?

* Clone the repo
* Add a API user to Icinga2
* Edit the script to change to request domain and add username and password (base64 encoded)
* Add servers to hosts file
* Test with ```python3 main.py```
* Setup cronjob to run the script how often you want

- - - -

WARNING: Credentials stored in this script are not secure so make sure to set correct permissions and limit API access as far as you can to mitigate some risks.
