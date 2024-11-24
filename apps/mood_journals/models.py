from apps.base_entities.models import BaseEntity

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class MoodEntry(BaseEntity):
    __tablename__ = 'mood_entries'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)

    user = relationship('User', back_populates='mood_entries')
    emotion_tags = relationship('EmotionTag', secondary=mood_entry_emotion_tag, back_populates='mood_entries')


class EmotionTag(BaseEntity):
    __tablename__ = 'emotion_tags'
    value = Column(String, nullable=False)


class textRecord(BaseEntity):
    __tablename__ = 'text_records'
    text = Column(Text, nullable=False)
    mood_id = Column(Integer, ForeignKey('mood_entries.id'), nullable=False)

    user = relationship('User', back_populates='text_records')


class VoiceRecord(BaseEntity):
    __tablename__ = 'voice_records'
    file_path = Column(String, nullable=False)
    mood_id = Column(Integer, ForeignKey('mood_entries.id'), nullable=False)

    user = relationship('User', back_populates='voice_records')


User.mood_entries = relationship('MoodEntry', order_by=MoodEntry.id, back_populates='user')
# Association table for many-to-many relationship between MoodEntry and EmotionTag
mood_entry_emotion_tag = Table(
    'mood_entry_emotion_tag', Base.metadata,
    Column('mood_entry_id', Integer, ForeignKey('mood_entries.id'), primary_key=True),
    Column('emotion_tag_id', Integer, ForeignKey('emotion_tags.id'), primary_key=True)
)
