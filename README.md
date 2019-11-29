# Luxafåret - 👋 your Luxafor 🏳️‍🌈 like a 🐑

## Usage

```
$ luxafaret --help
usage: luxafaret [-h] [--red] [--green] [--orange] [--blue] [--off]
                 [--colour COLOUR]

Change colour on the Luxafor flag

optional arguments:
  -h, --help            show this help message and exit
  --red
  --green
  --orange
  --blue
  --off
  --colour COLOUR, --color COLOUR
                        Name of web colour to set the flag to
$ luxafaret --red
$ luxafaret --colour green
```

## Installation

### Via pipx
```
$ pix install luxafaret
```

### Via venv
```
$ python3 -m venv luxafaret
$ . luxafaret/bin/activate
$ pip3 install luxafaret
```

## Using without sudo on Linux
Since you're writing directly to a USB-device you need permissions for that, on
Linux you have to [fix that via udev](https://duckduckgo.com/?q=luxafor+udev).
