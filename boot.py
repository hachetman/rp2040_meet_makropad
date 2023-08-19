import usb_hid

REPORT_ID = (0x20, 0x21, 0x22, 0x23, 0x24, 0x25)
REPORT_BYTES = (1,1,1,1,1,1)
bitmap_keyboard_descriptor = bytes((
        0x05, 0x0B,        # Usage Page (Telephony)
        0x09, 0x05,        # Usage (Headset)
        0xA1, 0x01,        # Collection (Application)
        0x85, 0x20,        #   Report ID (32)
        0x15, 0x00,        #   Logical Minimum (0)
        0x25, 0x01,        #   Logical Maximum (1)
        0x75, 0x01,        #   Report Size (1)
        0x95, 0x01,        #   Report Count (1)
        0x09, 0x20,        #   Usage (Hook Switch)
        0x81, 0x22,        #   Input (Data,Var,Abs,No Wrap,Linear,No Preferred State,No Null Position)
        0x09, 0x2F,        #   Usage (Phone Mute)
        0x81, 0x06,        #   Input (Data,Var,Rel,No Wrap,Linear,Preferred State,No Null Position)
        0x09, 0x21,        #   Usage (Flash)
        0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0x09, 0x24,        #   Usage (Redial)
        0x81, 0x06,        #   Input (Data,Var,Rel,No Wrap,Linear,Preferred State,No Null Position)
        0x09, 0x07,        #   Usage (Programmable Button)
        0x05, 0x09,        #   Usage Page (Button)
        0x09, 0x01,        #   Usage (0x01)
        0x81, 0x06,        #   Input (Data,Var,Rel,No Wrap,Linear,Preferred State,No Null Position)
        0x75, 0x03,        #   Report Size (3)
        0x81, 0x01,        #   Input (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)
        0x85, 0x21,        #   Report ID (33)
        0x05, 0x08,        #   Usage Page (LEDs)
        0x09, 0x18,        #   Usage (Ring)
        0x75, 0x01,        #   Report Size (1)
        0x91, 0x22,        #   Output (Data,Var,Abs,No Wrap,Linear,No Preferred State,No Null Position,Non-volatile)
        0x75, 0x07,        #   Report Size (7)
        0x91, 0x01,        #   Output (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
        0x85, 0x22,        #   Report ID (34)
        0x09, 0x1E,        #   Usage (Speaker)
        0x75, 0x01,        #   Report Size (1)
        0x91, 0x22,        #   Output (Data,Var,Abs,No Wrap,Linear,No Preferred State,No Null Position,Non-volatile)
        0x75, 0x07,        #   Report Size (7)
        0x91, 0x01,        #   Output (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
        0x85, 0x23,        #   Report ID (35)
        0x09, 0x09,        #   Usage (Mute)
        0x75, 0x01,        #   Report Size (1)
        0x91, 0x22,        #   Output (Data,Var,Abs,No Wrap,Linear,No Preferred State,No Null Position,Non-volatile)
        0x75, 0x07,        #   Report Size (7)
        0x91, 0x01,        #   Output (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
        0x85, 0x24,        #   Report ID (36)
        0x09, 0x17,        #   Usage (Off-Hook)
        0x75, 0x01,        #   Report Size (1)
        0x91, 0x22,        #   Output (Data,Var,Abs,No Wrap,Linear,No Preferred State,No Null Position,Non-volatile)
        0x75, 0x07,        #   Report Size (7)
        0x91, 0x01,        #   Output (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
        0x85, 0x25,        #   Report ID (37)
        0x09, 0x20,        #   Usage (Hold)
        0x75, 0x01,        #   Report Size (1)
        0x91, 0x22,        #   Output (Data,Var,Abs,No Wrap,Linear,No Preferred State,No Null Position,Non-volatile)
        0x75, 0x07,        #   Report Size (7)
        0x91, 0x01,        #   Output (Const,Array,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
        0xC0               # End Collection
))


bitmap_keyboard = usb_hid.Device(
  report_descriptor=bitmap_keyboard_descriptor,
    usage_page=0x0b,
    usage=0x05,
    report_ids=REPORT_ID,
    in_report_lengths=REPORT_BYTES,
    out_report_lengths=REPORT_BYTES,
)

usb_hid.enable(
    (
        bitmap_keyboard,
    )
)
print("enabled HID with custom keyboard device")
