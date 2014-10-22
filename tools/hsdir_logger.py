"""Follow HS directory events."""

from datetime import datetime

from stem.control import Controller, EventType


def print_hsdesc(event):
    """Print HS_DESC event's variables."""
    time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    action_str = 'Action: %s, address: %s, directory: %s, directory_fingerprint: %s, directory_nickname: %s, descriptor_id: %s' % (str(event.action), str(event.address), str(event.directory), str(event.directory_fingerprint), str(event.directory_nickname), str(event.descriptor_id))
    print time_str + " : " + action_str

if __name__ == '__main__':
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate() # provide the password here if you set one
        print 'Tor is running version %s' % controller.get_version()
        controller.add_event_listener(print_hsdesc, EventType.HS_DESC)
        raw_input()  # wait for user to press enter
