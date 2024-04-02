from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

def test_insert_event():
  event = {
    'uuid': 'meu-uuid-e-nois2',
    'title': 'meu title',
    'slug': 'meu-slug2',
    'maximum_attendees': 20
  }
  event_repository = EventsRepository()
  response = event_repository.insert_event(event)
  print(response)

def test_get_event_by_id():
  event_id = 'meu-uuid-e-nois2'
  event_repository = EventsRepository()
  response = event_repository.get_event_by_id(event_id)
  print(response)
