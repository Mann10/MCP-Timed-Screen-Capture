from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
import pyautogui
import io
import time

mcp=FastMCP("Screenshottool")

@mcp.tool()
def capture_screenshot():
    
    """
    Capture the current screen and return the image. Use this tool whenever the user request's screenshot.
    """
    time.sleep(3)
    buffer=io.BytesIO()
    screenshot=pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer,format='JPEG',quality=60,optimize=True)
    return Image(data=buffer.getvalue(),format='JPEG')

