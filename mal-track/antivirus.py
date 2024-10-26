import os
import psutil
import winreg
import re

def kill_process():
    malicious_process_name = "maltrack.exe"
    for process in psutil.process_iter(['pid', 'name']):
        process_info = process.info
        process_name = process_info['name'].lower()
        if malicious_process_name in process_name:
            try:
                process.kill()  # Forcefully kill the process
                print(f"Terminated malicious process: {process_name}")
            except psutil.NoSuchProcess:
                print(f"Process {process_name} no longer exists.")
            except psutil.AccessDenied:
                print(f"Access denied when trying to terminate {process_name}.")
            except Exception as e:
                print(f"Error terminating process {process_name}: {str(e)}")

def delete_virus():
    possible_paths = [r'C:\Program Files', r'C:\Program Files (x86)', r'C:\Windows\System32', r'C:\Users']
    malicious_file_name = "maltrack.exe"
    
    for path in possible_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower() == malicious_file_name:
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, 'rb') as f:
                            data = f.read()
                        iplist = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4})', str(data))
                        if iplist:
                            print("Possible attacker IP address found:")
                            print(iplist)
                        else:
                            print("No IP addresses found!")
                        os.remove(full_path)
                        print(f"Deleted malicious file: {full_path}")
                    except FileNotFoundError:
                        print(f"File not found: {full_path}")
                    except PermissionError:
                        print(f"Permission denied when trying to delete {full_path}")
                    except Exception as e:
                        print(f"Error reading or deleting {full_path}: {str(e)}")

def remove_registry_entries():
    registry_keys = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]
    registries = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
    
    for registry in registries:
        for key_path in registry_keys:
            try:
                with winreg.OpenKey(registry, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
                    try:
                        winreg.DeleteValue(key, "Mal-Track")
                        print(f"Removed malicious entry from {key_path}")
                    except FileNotFoundError:
                        print(f"No such value 'Mal-Track' in {key_path}")
                    except OSError as e:
                        print(f"Error deleting registry value: {str(e)}")
            except FileNotFoundError:
                print(f"Registry key not found: {key_path}")
            except OSError as e:
                print(f"Error accessing registry key {key_path}: {str(e)}")

def main():
    if not os.path.exists('C:\\'):
        print("This script should be run on a Windows system.")
        return

    print("Starting malware removal process...")
    kill_process()
    remove_registry_entries()
    delete_virus()
    print("Virus removal completed.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

