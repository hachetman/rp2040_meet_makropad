import keypad
import board
import usb_hid
import displayio
from adafruit_simple_text_display import SimpleTextDisplay
from adafruit_hid.keyboard import Keyboard, find_device
from adafruit_hid.keycode import Keycode
import neopixel

# See https://cdn-shop.adafruit.com/product-files/5228/5223-ds.pdf#page=13
_DISPLAY_SLEEP_COMMAND = 0xAE
_DISPLAY_WAKE_COMMAND = 0xAF
key_pins = (
    board.KEY1,
    board.KEY2,
    board.KEY3,
    board.KEY4,
    board.KEY5,
    board.KEY6,
    board.KEY7,
    board.KEY8,
    board.KEY9,
    board.KEY10,
    board.KEY11,
    board.KEY12,
)

keys = keypad.Keys(key_pins, value_when_pressed=False, pull=True)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 12)
pixels[0] = (10, 0, 0)
pixels[9] = (0, 10, 0)
display = board.DISPLAY
display.bus.send(_DISPLAY_WAKE_COMMAND, b"")
mini_display = SimpleTextDisplay(title="Temperature Data!", title_scale=2, display=board.DISPLAY)
mini_display.show()
class Telephony:
    """Send and recieve telephony HID  reports."""

    # No more than _MAX_KEYPRESSES regular keys may be pressed at once.

    def __init__(self, devices: Sequence[usb_hid.Device]) -> None:
        """Create a Telephony object that will send adn receive telephony HID reports.

        Devices can be a sequence of devices that includes a keyboard device or a keyboard device
        itself. A device is any object that implements ``send_report()``, ``usage_page`` and
        ``usage``.
        """
        self._keyboard_device = find_device(devices, usage_page=0x0b, usage=0x05)
        # Reuse this bytearray to send keyboard reports.
        self.report = bytearray(1)
        self.muted = False
        self.in_call = False

    def status(self):
        """Returns the last received report"""
        # get_last_received_report() returns None when nothing was received
        report = self._keyboard_device.get_last_received_report(0x20)
        if report is not None:
            print("did get a report 0x20")
            print(report)
        report = self._keyboard_device.get_last_received_report(0x21)
        if report is not None:
            print("did get a report 0x21")
            print(report)
        report = self._keyboard_device.get_last_received_report(0x22)
        if report is not None:
            print("did get a report 0x22")
            print(report)
        report = self._keyboard_device.get_last_received_report(0x23)
        if report is not None:
            print("did get a report 0x23")
            print(report)
            if report == b'\x01':
                self.muted = True
            else:
                self.muted = False
        report = self._keyboard_device.get_last_received_report(0x24)
        if report is not None:
            print("did get a report 0x24")
            print(report)
            if report == b'\x01':
                self.in_call = True
            else:
                self.in_call = False

        report = self._keyboard_device.get_last_received_report(0x25)
        if report is not None:
            print("did get a report 0x25")
            print(report)

    def mute(self):
        """ mutes the active call """
        self._keyboard_device.send_report(b'\x03', 0x20)

#kbd = BitmapKeyboard(usb_hid.devices)
telephony = Telephony(usb_hid.devices)
keymap = [
    Keycode.ONE, Keycode.TWO, Keycode.THREE,
    Keycode.Q, Keycode.W, Keycode.E,
    Keycode.A, Keycode.S, Keycode.D,
    Keycode.Z, Keycode.X, Keycode.C]

while True:
    ev = keys.events.get()
    telephony.status()
    if ev is not None:
        if ev.pressed:
            telephony.mute()
