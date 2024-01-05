import ctypes
import sys
import psutil
import subprocess
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def find_process(process_name):
    for proc in psutil.process_iter(['name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

def run_process(process_path):
    subprocess.Popen(process_path, shell=True)

def minimize_console_window():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 6)  # SW_MINIMIZE = 6

def main():
    process_name = "steamcommunity_302.exe"
    process_path = r"C:\Users\Administrator\Desktop\steamcommunity_302\steamcommunity_302.exe"
    minimize_console_window()
    while True:
        if find_process(process_name):
            print(f"{process_name} is running.")
        else:
            print(f"{process_name} not found, running {process_path}.")

            # Terminate old process
            for proc in psutil.process_iter(['name']):
                if process_name.lower() in proc.info['name'].lower():
                    proc.terminate()
                    break

            # Run new process
            run_process(process_path)

        time.sleep(5)

if __name__ == "__main__":
    run_as_admin()
    main()
