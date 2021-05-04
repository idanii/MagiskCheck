from subprocess import PIPE, run
from colorama import Fore
import os

os.system('clear')

def check_for_magisk():
    device_rooted = False

    command = ['adb', 'shell', 'which', 'magisk']

    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)

    if "no devices" in result.stderr:
        print(Fore.RED + 'Device is not connected.')
    elif "unauthorized" in result.stderr:
        print(Fore.RED + 'Device is not authorized.')
    elif result.returncode == 1:
        device_rooted = False
    else:
        device_rooted = True        
    
    if device_rooted == False:
        command2 = ['adb', 'shell', 'magisk']

        result2 = run(command2, stdout=PIPE, stderr=PIPE, universal_newlines=True)

        if "not found" in result2.stderr:
            command3 = ['adb', 'shell', 'which', 'su']

            result3 = run(command3, stdout=PIPE, stderr=PIPE, universal_newlines=True)

            if result3.stdout == "":
                command4 = ['adb', 'shell', 'cd', '/sbin']

                result4 = run(command4, stdout=PIPE, stderr=PIPE, universal_newlines=True)

                if "Permission denied" in result4.stderr:
                    print(Fore.GREEN + 'Device is not rooted.')
                else:
                    device_rooted = True
            elif "/su" in result3.stdout:
                device_rooted = True
    
    if device_rooted == True:
        print(Fore.RED + 'Device is rooted with Magisk.')


if __name__ == '__main__':
    check_for_magisk()