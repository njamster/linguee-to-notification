# Linguee-To-Notification

A simple python script that sends a request for the currently selected text to [Linguee.com](https://www.linguee.com/), parses the HTML-response and displays its most relevant content in a D-Bus-notification. Only tested on Linux.

## Usage

If you want to use the currently selected text as a query, simply run the python script as is:

`python main.py`

Alternatively you can pass along one command line argument to use as a query instead:

`python main.py "drink something"`

**I highly recommend binding those calls to hotkeys via your operating system or window manager!**

## Notes
* This script will most likely break once Linguee decides to change their API! Adapting it should be easy though.
* Queries consisting of more than three words are ignored by default, cf. `get_current_selection()`
* Translations are done between English and German by default, cf. `translate()`

## Requirements
### Linux
* xsel (only if you want to use the currently selected text as a query)

### Python
* requests
* BeautifulSoup
* notify2

## Terms and Conditions

If you use this script, make sure you comply with the [Linguee Terms and Conditions](http://www.linguee.com/page/termsAndConditions.php) and especially this clause:

> Both private and business usage of linguee.com services is free of charge. It is however strictly prohibited to forward on our services to third parties against payment
