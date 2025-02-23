# ONT/ONU Device Health Check

This Python script is designed to check the health status of ONT (Optical Network Terminals) or ONU (Optical Network Units) devices connected to a network. It performs several checks on device health, including CPU usage, memory usage, optical power, temperature, and voltage levels.

## Features

- Installs required libraries (`colorama`, `netmiko`) if not already installed.
- Supports both **Telnet** and **SSH** connections to devices.
- Pings the device before attempting to connect to ensure it is reachable.
- Analyzes device health information, including:
  - CPU Usage
  - Memory Usage
  - Optical Temperature and Voltage
  - Tx Power and Rx Power
- Provides color-coded health status output to indicate if the device is in **Critical** or **Good** state.

## Requirements

- Python 3.x
- `colorama` library
- `netmiko` library
- A Cisco-compatible device that supports Telnet or SSH (the script currently uses Telnet to connect to the device).

## Installation

To install the necessary dependencies, simply run the script, and it will automatically install `colorama` and `netmiko`:

## Example Output

```bash

python run.py
********************************************
        This code written by Taif     
        onu/ont Device Check health   
    Please follow me on TikTok @taifallhyby   
        For any help, contact me!        
********************************************

Check device health for Cisco Model X
----------------------------------------------------
                      device information
Manufacturer: Cisco
Model Name: Model X
Up Time: 3600 seconds
----------------------------------------------------
                      system information
CPU Used: 75%
Memory Used: 60%
----------------------------------------------------
                      optical information
Temperature: 32 (C)
Voltage: 3300 (mV)
Tx Power: -10.5 (dBm)
Rx Power: -20.2 (dBm)
----------------------------------------------------
                      device health
Device state is: Critical
----------------------------------------------------

```
## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any issues or help, contact the author:

TikTok: @taifallhyby

Email: tyfhmyd2@gmail.com


