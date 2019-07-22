#!/usr/bin/env python

"""Save sensor data."""

import os
import json
from time import time
from farmware_tools import get_config_value, device

def timestamp(value):
    """Add a timestamp to the pin value."""
    return {'time': time(), 'value': value}

def append(data):
    """Add new data to existing data."""
    existing_data = json.loads(os.getenv(LOCAL_STORE, '[]'))
    if data['value'] is not None:
        existing_data.append(data)
    return existing_data

if __name__ == '__main__':
    PIN = get_config_value('save-sensor-data', 'pin')
    LOCAL_STORE = 'pin_data_' + str(PIN)
    DATA = append(timestamp(device.get_pin_value(PIN)))
    device.set_user_env(LOCAL_STORE, json.dumps(DATA))
