# pylint: disable=missing-docstring
import sys
import time
from .. import chip, line, line_request

try:
    if len(sys.argv) > 2:
        LED_CHIP = sys.argv[1]
        LED_LINE_OFFSET = int(sys.argv[2])
    else:
        raise Exception()
# pylint: disable=broad-except
except Exception:
    print(
        """Usage:
    python3 -m gpiod.test.blink <chip> <line offset>"""
    )
    sys.exit()

c = chip(LED_CHIP)

print("chip name: ", c.name)
print("chip label: ", c.label)
print("number of lines: ", c.num_lines)

print()

led = c.get_line(LED_LINE_OFFSET)

print("line offset: ", led.offset)
print("line name: ", led.name)
print("line consumer: ", led.consumer)
print(
    "line direction: ",
    "input" if led.direction == line.DIRECTION_INPUT else "output",
)
print(
    "line active state: ",
    "active low" if led.active_state == line.ACTIVE_LOW else "active high",
)
print("is line used: ", led.is_used)
print("is line open drain: ", led.is_open_drain)
print("is_open_source: ", led.is_open_source)
print("is line requested: ", led.is_requested)

print("\nrequest line\n")

config = line_request()
config.consumer = "Blink"
config.request_type = line_request.DIRECTION_OUTPUT

led.request(config)

print("line consumer: ", led.consumer)
print(
    "line direction: ",
    "input" if led.direction == line.DIRECTION_INPUT else "output",
)
print(
    "line active state: ",
    "active low" if led.active_state == line.ACTIVE_LOW else "active high",
)
print("is line used: ", led.is_used)
print("is line open drain: ", led.is_open_drain)
print("is_open_source: ", led.is_open_source)
print("is line requested: ", led.is_requested)

while True:
    led.set_value(0)
    time.sleep(0.1)
    led.set_value(1)
    time.sleep(0.1)
