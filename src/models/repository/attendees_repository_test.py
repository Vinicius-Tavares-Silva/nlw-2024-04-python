from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

def test_insert_attendee():
  event_id = 'dc8d0757-f664-463b-8c3b-346bbd0308fa'

  attendees_info = {
    'uuid': 'meu-uuid-attendee3',
    'name': 'meu name',
    'email': 'email@email.com',
    'event_id': event_id
  }
  attendees_repository = AttendeesRepository()
  response = attendees_repository.insert_attendee(attendees_info)
  print(response)

def test_get_attende_badge_by_id():
  attendee_id = 'meu-uuid-attendee'
  attendees_repository= AttendeesRepository()
  attendee = attendees_repository.get_attende_badge_by_id(attendee_id)
  print(attendee)
