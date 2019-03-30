# Linguee-To-Notification

A simple python script that sends a request for the currently selected text to [Linguee.com](https://www.linguee.com/), parses the HTML-response and displays its most relevant content in a D-Bus-notification. Only tested on Linux.

## Requirements
### Linux
* xsel

### Python
* requests
* BeautifulSoup
* notify2
