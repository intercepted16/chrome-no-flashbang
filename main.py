import subprocess
import pygetwindow as gw
import os

path = None
possible_locations = [
    f"{os.environ('LOCALAPPDATA')}",
    f"{os.environ('ProgramFiles')}",
    f"{os.environ('ProgramFiles(x86)')}",
]

for location in possible_locations:
    if os.path.exists(f"{location}\\Google\\Chrome\\Application\\chrome.exe"):
        path = f"{location}\\Google\\Chrome\\Application\\chrome.exe"
        break

if not path:
    print("Chrome not found")
    exit()

# launch chrome offscreen and tiny to avoid flash
subprocess.Popen(
    [
        path,
        "--window-position=-3940,2160",
        "--window-size=0,0",
    ],
    creationflags=subprocess.CREATE_NEW_CONSOLE,
).pid

# wait till window is opened
while True:
    if gw.getWindowsWithTitle("Chrome"):
        win = gw.getWindowsWithTitle("Chrome")[0]
        # maximize window
        win.moveTo(0, 0)
        win.size = (3800, 2120)
        exit()
