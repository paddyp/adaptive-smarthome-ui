from sqlalchemy.orm import Session, joinedload
from utils.const import get_broadcast_data_dict
from . import models, schemas


async def get_smarthome_devices(db: Session, skip: int = 0, limit: int = 100) -> list: 
    query_list =  db.query(models.SmarthomeDevice).options(joinedload(models.SmarthomeDevice.channels)).offset(skip).limit(limit).all()
    out = []
    for item in query_list: 
        temp_smarthomedevice_schema = schemas.SmarthomeDevice(**item.__dict__)
        out.append(temp_smarthomedevice_schema.json())
    return get_broadcast_data_dict(out)

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item