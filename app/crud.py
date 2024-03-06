from sqlalchemy.orm import Session
from . import models

def create_device(db: Session, name: str):
    db_device = models.Device(name=name)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device
