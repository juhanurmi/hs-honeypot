"""Follow HS directory events."""

import time
from datetime import datetime

from stem.control import Controller, EventType


def print_hsdesc(event):
    """Print HS_DESC event's variables."""
    print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print 'Action: %i, address: %i, directory: %i, directory_fingerprint: %i, directory_nickname: %i, descriptor_id: %i' % (event.action, event.address, event.directory, event.directory_fingerprint, event.directory_nickname, event.descriptor_id)

if __name__ == '__main__':
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate() # provide the password here if you set one
        print 'Tor is running version %s' % controller.get_version()
        controller.add_event_listener(print_hsdesc, EventType.HS_DESC)
        time.sleep(60*60*24*30)
