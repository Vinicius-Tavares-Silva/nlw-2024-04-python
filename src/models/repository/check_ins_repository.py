from sqlalchemy.exc import IntegrityError
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from src.errors.error_types.http_conflict import HttpConflictError

class CheckInRepository:
  def insert_attendee(self, attende_id):
    with db_connection_handler as database:
      try:
        chek_in = (
          CheckIns(attendeeId=attende_id)
        )
        database.session.add(chek_in)
        database.session.commit()

        return attende_id

      except IntegrityError:
        raise HttpConflictError('Check In ja cadastrado!')

      except Exception as exception:
        database.session.rollback()
