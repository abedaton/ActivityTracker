from typing import Optional
from ctypes import windll, create_unicode_buffer
import time

def getForegroundWindowTitle(sleep_time=0) -> Optional[str]:
    time.sleep(sleep_time)
    foregroundWindow = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(foregroundWindow)
    buffer = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(foregroundWindow, buffer, length + 1)

    if buffer.value:
        return buffer.value
    else:
        return None

if __name__ == "__main__":
    print(getForegroundWindowTitle())
    print(getForegroundWindowTitle(3))