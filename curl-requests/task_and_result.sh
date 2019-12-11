#!/usr/bin/env bash

###################
# Create a new example task and then poll for the result
###################

# send http request to API to start new long_task
response=$(bash curl-requests/long_task.sh | grep Location)

# get the header containing the location(url) of the task status
location=$(echo $response | grep Location)

# Trim the header so that only the status url is remaining
status_url=${location#*: }
# remove trailing symbol for use with curl
status_url=${status_url%$'\r'}

# poll for the task status until it is successful
status=unknown
while [[ "$state" != "SUCCESS" ]]; do
  response=`curl -s $status_url`
  echo $response
  state=$(echo $response | jq -r '.state')
  sleep 4
done
