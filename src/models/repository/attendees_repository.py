from typing import Dict
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events

class AttendeesRepository:

  def insert_attendee(self, attende_info: Dict) -> Dict:
    with db_connection_handler as database:
      try:
        attendee = (
          Attendees(
            id=attende_info.get('uuid'),
            name=attende_info.get('name'),
            email=attende_info.get('email'),
            event_id=attende_info.get('event_id'),
          )
        )
        database.session.add(attendee)
        database.session.commit()

        return attende_info
      
      except IntegrityError:
        raise Exception('Participante ja cadastrado!')

      except Exception as exception:
        database.session.rollback()
        raise exception

  def get_attende_badge_by_id(self, attendee_id: str) -> Attendees:
    with db_connection_handler as database:
      try:
        attendee = (
          database.session
            .query(Attendees)
            .join(Events, Events.id == Attendees.event_id)
            .filter(Attendees.id==attendee_id)
            .with_entities(
              Attendees.name,
              Attendees.email,
              Events.title
            )
            .one()
        )
        return attendee
      except NoResultFound:
        return None
