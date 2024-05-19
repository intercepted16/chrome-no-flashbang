# launch chrome offscreen and tiny to avoid flash
import subprocess
import pygetwindow as gw  # Import pygetwindow

subprocess.Popen(
    [
        "C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--window-position=-3940,2160",
        "--window-size=0,0",
    ],
    creationflags=subprocess.CREATE_NEW_CONSOLE,
).pid

win = None

while True:
    if gw.getWindowsWithTitle("Chrome"):
        win = gw.getWindowsWithTitle("Chrome")[0]
        win.moveTo(0, 0)
        win.size = (3800, 2120)
        exit()
