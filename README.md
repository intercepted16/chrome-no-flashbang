# Usage
1. Download and move the packaged executable into any directory.

2. Edit the Google Chrome shortcut(s) to point to the packaged executable.

3. Done! Enjoy Chrome without the painful flashbang.

**PS:** this only works on Windows for now, support for other OS's coming soon


# Compilation
You can use pyinstaller for the compilation.
To mitigate the annoying terminal flash, pass the `--noconsole` parameter to pyinstaller, like so:

`pyinstaller --onefile --noconsole main.py -o chrome-no-flash.exe`
