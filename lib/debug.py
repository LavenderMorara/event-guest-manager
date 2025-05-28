
from lib import Session

if __name__ == '__main__':
    session = Session()
    from lib.models.guests import Guest
    from lib.models.events import Event
    from lib.models.rsvp import RSVP

    import ipdb; ipdb.set_trace()