from sqlalchemy import Column, Integer, string
from sqlalchemy.orm import declarative_base
import uuid
    
Base = declarative_base()
    
class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_title = Column(String(100), nullable=False)

    def __repr__ (self):
        return f"<Subject(id={self.subject_id}, title='{self. subject_title}')>"

def test_add_subject(db_session):
    """Тест добавления нового предмета"""
    unique_id = str(uuid.uuid4())[:8]
    test_title = f"Математика_{unique_id}"

    new_subject = Subject(subject_title=test_title)

    db_session.add(new_subject)
    db_session. commit()

    assert new_subject.subject_id is not None
    
    saved_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=new_subject.subject_id)
        .first()
    )    
    assert saved_subject is not None
    assert saved_subject.subject_title == test_title
    
    db_session. delete(saved_subject)
    db_session. commit()
    
    deleted_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=new_subject.subject_id)
        .first()
    )
    assert deleted_subject is None

def test_update_subject(db_session):
    """Тест изменения существующего предмета"""
    unique_id = str(uuid.uuid4())[:8]
    original_title = f"Физика_{unique_id}"
    updated_title = f"Физика (углубленный курс)_{unique_id}"

    subject = Subject(subject_title=original_title)
    db_session.add(subject)
    db_session.commit ()

    subject_id = subject.subject_id

    created_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )
    assert created_subject is not None
    assert created_subject.subject_title == original_title
    
    created_subject.subject_title = updated_title
    db_session.commit()

    updated_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )
    assert updated_subject is not None
    assert updated_subject.subject_title == updated_title

    db_session.delete(updated_subject)
    db_session.commit()
    
    deleted_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )
    assert deleted_subject is None

def test_delete_subject(db_session):
    """Тест удаления предмета"""
    unique_id = str(uuid.uuid4())[:8]
    test_title = f"Химия_{unique_id}"
    
    subject = Subject(subject_title=test_title)
    db_session.add(subject)
    db_session.commit()
    
    subject_id = subject.subject_id
    
    created_subject = (
    db_session.query(Subject)
    .filter_by(subject_id=subject_id)
    .first()
    )

    subject_id = subject.subject_id
    
    created_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )
    assert created_subject is not None
    assert created_subject.subject_title == test_title
    
    db_session.delete(created_subject)
    db_session.commit()

    deleted_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )
    assert deleted_subject is None
    