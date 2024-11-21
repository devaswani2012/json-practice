#!/bin/bash

URL="https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85"

DATA=$(curl -s "$URL")

echo "$DATA" | jq -r '..|.receiptTime? | select(. != null)' | head -n 6

