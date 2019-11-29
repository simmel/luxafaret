#!/usr/bin/env python
# vim: set fileencoding=utf8 sw=2 et
# Copyright 2017 Simon Lundström <simmel@soy.se>

# Permission to use, copy, modify, and distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright
# notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

import argparse
import sys

import hid
import webcolors


def main():
    parser = argparse.ArgumentParser(description="Change colour on the Luxafor flag")
    parser.add_argument("--red", dest="colour", action="store_const", const="red")
    parser.add_argument("--green", dest="colour", action="store_const", const="green")
    parser.add_argument("--orange", dest="colour", action="store_const", const="orange")
    parser.add_argument("--blue", dest="colour", action="store_const", const="blue")
    parser.add_argument("--off", dest="colour", action="store_const", const="black")
    parser.add_argument(
        "--colour", "--color", help="Name of web colour to set the flag to"
    )
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(255)

    device = hid.device()
    device.open(0x04D8, 0xF372)
    # For explaination, see https://pro.luxafor.com/faq/ , click API, download the
    # .zip and check the .xls in it.
    # Fade the change
    cmd = [2]
    # Only change the flag LEDs
    cmd += [0x41]

    cmd += webcolors.name_to_rgb(args.colour)

    # Set fade time
    cmd += [16]

    device.write(cmd)
    device.close()


if __name__ == "__main__":
    main()
