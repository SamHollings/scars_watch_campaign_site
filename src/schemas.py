from datetime import date
from typing import List, Optional

from pydantic import BaseModel

# This file contains pydantic models for the model described in data/data model.md


class Chunk(BaseModel):
    chunk_id: str
    content: str


class Metadata(BaseModel):
    chunk_id: str
    parent_document: str
    title: str
    category: str
    source: str


class Embedding(BaseModel):
    chunk_id: str
    content_embedding: str
    model: str


class Document(BaseModel):
    doc_id: str
    content: str
    title: str
    category: str
    source: str


class Submission(BaseModel):
    submission_id: str
    content: str
    title: str
    category: str
    source: str


class Category(BaseModel):
    category_id: str
    category_type: str
    category_desc: str


class Character(BaseModel):
    character_id: str
    faction_id: Optional[str] = None
    background_information: str
    picture: str
    source: str


class Faction(BaseModel):
    faction_id: str
    parent_faction_id: Optional[str] = None
    background_information: str
    picture: str
    source: str
    effective_from_date: date
    effective_to_date: Optional[date] = None


class Location(BaseModel):
    location_id: str
    faction_id: Optional[str] = None
    parent_location_id: Optional[str] = None
    background_information: str
    picture: str
    source: str
    effective_from_date: date
    effective_to_date: Optional[date] = None


class GameObject(BaseModel):  # Renamed from Object to avoid keyword conflict
    object_id: str
    character_id: Optional[str] = None
    location_id: Optional[str] = None
    background_information: str
    picture: str
    source: str
    effective_from_date: date
    effective_to_date: Optional[date] = None


class Event(BaseModel):
    event_id: str
    faction_ids: List[str]
    location_id: str
    character_ids: List[str]
    object_ids: List[str]
    background_information: str
    picture: str
    source: str
    event_date: date
    in_game_date: date

