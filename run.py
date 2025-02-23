import subprocess
import platform
import os
import time
import re
import sys
def initi():
    try:
      import colorama
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    
    try:
        import netmiko
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "netmiko"])

initi()

from colorama import init, Fore
from netmiko import ConnectHandler
init()




def clear_console():
    system_name = platform.system().lower()
    
    if system_name == "windows":
        os.system("cls") 
    else:
        os.system("clear")
def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    command = ["ping", param, "1", host]
    
    try:
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if response.returncode == 0:
            return True
        else:
           return False
    except Exception as e:
        print(f"An error occurred: {e}")
def anlayze_response(a,b,c):
    cpu_j = False
    memo_j = False
    power_j = False
    try:
        model_name = re.search(r'ModelName\s*=\s*(\S+)', a).group(1)
        manufacturer = re.search(r'Manufacturer\s*=\s*(.*)', a).group(1)
        uptime = re.search(r'UpTime\s*=\s*(\d+)', a).group(1)
        cpu_used = re.search(r'CpuUsed\s*=\s*(\d+)', b).group(1)
        mem_used = re.search(r'MemUsed\s*=\s*(\d+)', b).group(1)
        optic_temp = re.search(r'Temperature\s*:\s*(\d+)', c).group(1)
        optic_voltage = re.search(r'Voltage\s*:\s*(\d+)', c).group(1)
        tx_power = re.search(r'TxPower\s*:\s*(\S+)', c).group(1)
        rx_power = re.search(r'RxPower\s*:\s*(\S+)', c).group(1)
    except:
        print("error in macth re model")

    
    print(f"              Check device health for {model_name}")
    print("---------------------------------------------------------------------------------")
    print("                          device information")
    print(f"Manufacturer: {manufacturer}")
    print(f"Model Name: {model_name}")
    print(f"Up Time: {uptime} seconds")
    print("---------------------------------------------------------------------------------")
    print("                          system information")
    print(f"CPU Used: {cpu_used} Percent(s)")
    print(f"Memory Used: {mem_used} Percent(s)")
    print("---------------------------------------------------------------------------------")
    print("                          optical information")
    print(f"Temperature: {optic_temp} (C)")
    print(f"Voltage: {optic_voltage} (mV)")
    print(f"Tx Power: {tx_power} (dBm)")
    print(f"Rx Power: {rx_power} (dBm)")
    print("---------------------------------------------------------------------------------")
    print("                          device health")
    try:
        if int(cpu_used) > 80:
            print("CPU is overloaded")
            cpu_j = True
        if int(mem_used) > 90:
            print("Memory is overloaded")
            memo_j = True
        if int(optic_temp) > 40:
            print("Optical temperature is high")
    
        if int(optic_voltage) > 3500:
            print("Optical voltage is high")
        if tx_power == "--" or rx_power == "--":
            print("Optical power is not detected")
            power_j = True
        if tx_power != "--" and rx_power != "--":
            if rx_power > -17 or rx_power < -30:
                print("Rx power is out of range")
                if rx_power > -29:
                    power_j = True
    except:
        print("error in state condtion")
    print("---------------------------------------------------------------------------------")
    if cpu_j or memo_j or power_j:
        print("                      Device state is: "+ Fore.RED + "Critical")
    else:
        print("                         Device state is: " + Fore.GREEN +"Good")
    print(Fore.WHITE+"----------------------------------------------------------------------------------")


def telnet_ssh_client():
    device = {
        "device_type": "cisco_ios_telnet",
        'host': '192.168.100.1',
        'username': 'root',
        'password': 'admin',
        'port': 23,  
    }
    host = "192.168.100.1"

    while True:
         clear_console()
         if not ping(host):
             input("no onu/ont found press enter to re try:")
             continue
         try:
             connection = ConnectHandler(**device)
     
             a = connection.send_command('display deviceinfo')
     
             b = connection.send_command('display sysinfo')
     
             c = connection.send_command('display optic')
             connection.disconnect()
             anlayze_response(a,b,c)
         except Exception as e:
            print(f"An error occurred: {e}")
         input(Fore.WHITE+"onu/ont check complet press enter to check another one:")


    

def welcome():
    clear_console()
    print(Fore.RED + "********************************************")
    print(Fore.YELLOW + "        This code written by Taif     ")
    print(Fore.GREEN + "        onu/ont Device Check health   ")
    print(Fore.CYAN + "    Please follow me on TikTok @taifallhyby   ")
    print(Fore.MAGENTA + "        For any help, contact me!        ")
    print(Fore.WHITE + "                    ")
    print(Fore.RED + "********************************************")
    print(Fore.WHITE+"")
    time.sleep(10)


welcome()
telnet_ssh_client()
