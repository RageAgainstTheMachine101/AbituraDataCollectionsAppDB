from apps.base_entities.models import BaseEntity
from apps.users.models import User

from sqlalchemy import Column, Date, Integer, String, ForeignKey, Boolean, Table, Text
from sqlalchemy.orm import relationship

# Association table for many-to-many relationship between MoodEntry and EmotionTag
mood_entry_emotion_tag = Table(
    'mood_entry_emotion_tag', BaseEntity.metadata,
    Column('mood_entry_id', Integer, ForeignKey('mood_entries.id'), primary_key=True),
    Column('emotion_tag_id', Integer, ForeignKey('emotion_tags.id'), primary_key=True)
)

class MoodEntry(BaseEntity):
    __tablename__ = 'mood_entries'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)

    # Relationships
    user = relationship('User', back_populates='mood_entries')
    emotion_tags = relationship('EmotionTag', secondary=mood_entry_emotion_tag, back_populates='mood_entries')


class EmotionTag(BaseEntity):
    __tablename__ = 'emotion_tags'
    value = Column(String, nullable=False)

    # Relationships
    mood_entries = relationship('MoodEntry', secondary=mood_entry_emotion_tag, back_populates='emotion_tags')


class TextRecord(BaseEntity):
    __tablename__ = 'text_records'
    text = Column(Text, nullable=False)
    mood_id = Column(Integer, ForeignKey('mood_entries.id'), nullable=False)

    # Relationships
    mood_entry = relationship('MoodEntry', back_populates='text_records')


class VoiceRecord(BaseEntity):
    __tablename__ = 'voice_records'
    file_path = Column(String, nullable=False)
    mood_id = Column(Integer, ForeignKey('mood_entries.id'), nullable=False)

    # Relationships
    mood_entry = relationship('MoodEntry', back_populates='voice_records')


# Add relationships to User and MoodEntry
User.mood_entries = relationship('MoodEntry', order_by=MoodEntry.id, back_populates='user')
MoodEntry.text_records = relationship('TextRecord', order_by=TextRecord.id, back_populates='mood_entry')
MoodEntry.voice_records = relationship('VoiceRecord', order_by=VoiceRecord.id, back_populates='mood_entry')
