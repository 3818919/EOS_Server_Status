import EndlessOnline as EL
import time
import requests
import config
import json

# Check server status, alert when a change is detected
def server_alert():

  # Get status data
  webhook_data = EL.check_server()

  # If the server state changes
  if webhook_data is not None:
    urls = config.get_list()
    if urls is not None:
      for webhook in urls:
        send_data_to_server(webhook, webhook_data)
    else:
      return


# Send data to discord server
def send_data_to_server(webhook, webhook_data):

  # Setup alert settings
  ping_data = {
    "username": "Recharge Checker",
    "content": "@here" #To use a custom role, you must use a role ID like so: <@&1124903637517352960>
  }

  # Send role ping
  requests.post(webhook, json=ping_data)

  # Send alert embed
  requests.post(webhook, json=webhook_data)


# Main loop
while True:
  server_alert()
  # Check runs every 30 seconds
  time.sleep(30)
