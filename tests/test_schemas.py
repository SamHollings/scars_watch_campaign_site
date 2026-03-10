import pytest
import src.schemas as schemas
import datetime


def test_chunk():
    chunk = schemas.Chunk(chunk_id="test_id", content="test_content")
    assert chunk.chunk_id == "test_id"
    assert chunk.content == "test_content"

def test_metadata():
    metadata = schemas.Metadata(
        chunk_id="test_id",
        parent_document="test_doc",
        title="test_title",
        category="test_category",
        source="test_source"
    )
    assert metadata.chunk_id == "test_id"
    assert metadata.parent_document == "test_doc"
    assert metadata.title == "test_title"
    assert metadata.category == "test_category"
    assert metadata.source == "test_source"

def test_embedding():
    embedding = schemas.Embedding(
        chunk_id="test_id",
        content_embedding="test_embedding",
        model="test_model"
    )
    assert embedding.chunk_id == "test_id"
    assert embedding.content_embedding == "test_embedding"
    assert embedding.model == "test_model"

def test_document():
    document = schemas.Document(
        doc_id="test_doc_id",
        content="test_content",
        title="test_title",
        category="test_category",
        source="test_source"
    )
    assert document.doc_id == "test_doc_id"
    assert document.content == "test_content"
    assert document.title == "test_title"
    assert document.category == "test_category"
    assert document.source == "test_source"

def test_submission():
    submission = schemas.Submission(
        submission_id="test_submission_id",
        content="test_content",
        title="test_title",
        category="test_category",
        source="test_source"
    )
    assert submission.submission_id == "test_submission_id"
    assert submission.content == "test_content"
    assert submission.title == "test_title"
    assert submission.category == "test_category"
    assert submission.source == "test_source"

def test_category():
    category = schemas.Category(
        category_id="test_category_id",
        category_type="test_category_type",
        category_desc="test_category_desc"
    )
    assert category.category_id == "test_category_id"
    assert category.category_type == "test_category_type"
    assert category.category_desc == "test_category_desc"

def test_character():
    character = schemas.Character(
        character_id="test_character_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source"
    )
    assert character.character_id == "test_character_id"
    assert character.background_information == "test_background"
    assert character.picture == "test_picture"
    assert character.source == "test_source"

def test_faction():
    faction = schemas.Faction(
        faction_id="test_faction_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01"
    )
    assert faction.faction_id == "test_faction_id"
    assert faction.background_information == "test_background"
    assert faction.picture == "test_picture"
    assert faction.source == "test_source"
    assert faction.effective_from_date == datetime.date(2024, 1, 1)

def test_faction_with_parent():
    faction = schemas.Faction(
        faction_id="test_faction_id",
        parent_faction_id="parent_faction_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01"
    )
    assert faction.faction_id == "test_faction_id"
    assert faction.parent_faction_id == "parent_faction_id"
    assert faction.background_information == "test_background"
    assert faction.picture == "test_picture"
    assert faction.source == "test_source"
    assert faction.effective_from_date == datetime.date(2024, 1, 1)

def test_location():
    location = schemas.Location(
        location_id="test_location_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01"
    )
    assert location.location_id == "test_location_id"
    assert location.background_information == "test_background"
    assert location.picture == "test_picture"
    assert location.source == "test_source"
    assert location.effective_from_date == datetime.date(2024, 1, 1)

def test_location_with_parent():
    location = schemas.Location(
        location_id="test_location_id",
        parent_location_id="parent_location_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01"
    )
    assert location.location_id == "test_location_id"
    assert location.parent_location_id == "parent_location_id"
    assert location.background_information == "test_background"
    assert location.picture == "test_picture"
    assert location.source == "test_source"
    assert location.effective_from_date == datetime.date(2024, 1, 1)

def test_location_with_faction():
    location = schemas.Location(
        location_id="test_location_id",
        faction_id="test_faction_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01"
    )
    assert location.location_id == "test_location_id"
    assert location.faction_id == "test_faction_id"
    assert location.background_information == "test_background"
    assert location.picture == "test_picture"
    assert location.source == "test_source"
    assert location.effective_from_date == datetime.date(2024, 1, 1)

def test_location_with_faction_and_parent():
    location = schemas.Location(
        location_id="test_location_id",
        faction_id="test_faction_id",
        parent_location_id="parent_location_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01"
    )
    assert location.location_id == "test_location_id"
    assert location.faction_id == "test_faction_id"
    assert location.parent_location_id == "parent_location_id"
    assert location.background_information == "test_background"
    assert location.picture == "test_picture"
    assert location.source == "test_source"
    assert location.effective_from_date == datetime.date(2024, 1, 1)

def test_location_with_faction_and_parent_and_end_date():
    location = schemas.Location(
        location_id="test_location_id",
        faction_id="test_faction_id",
        parent_location_id="parent_location_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01",
        effective_to_date="2024-12-31"
    )
    assert location.location_id == "test_location_id"
    assert location.faction_id == "test_faction_id"
    assert location.parent_location_id == "parent_location_id"
    assert location.background_information == "test_background"
    assert location.picture == "test_picture"
    assert location.source == "test_source"
    assert location.effective_from_date == datetime.date(2024, 1, 1)
    assert location.effective_to_date == datetime.date(2024, 12, 31)

def test_location_with_faction_and_parent_and_end_date_none():
    location = schemas.Location(
        location_id="test_location_id",
        faction_id="test_faction_id",
        parent_location_id="parent_location_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01",
        effective_to_date=None
    )
    assert location.location_id == "test_location_id"
    assert location.faction_id == "test_faction_id"
    assert location.parent_location_id == "parent_location_id"
    assert location.background_information == "test_background"
    assert location.picture == "test_picture"
    assert location.source == "test_source"
    assert location.effective_from_date == datetime.date(2024, 1, 1)
    assert location.effective_to_date is None

def test_gameobject():
    game_object = schemas.GameObject(
        object_id="test_object_id",
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        effective_from_date="2024-01-01"
    )
    assert game_object.object_id == "test_object_id"
    assert game_object.background_information == "test_background"
    assert game_object.picture == "test_picture"
    assert game_object.source == "test_source"
    assert game_object.effective_from_date == datetime.date(2024, 1, 1)

def test_event():
    event = schemas.Event(
        event_id="test_event_id",
        faction_ids=["faction1", "faction2"],
        location_id="test_location_id",
        character_ids=["character1", "character2"],
        object_ids=["object1", "object2"],
        background_information="test_background",
        picture="test_picture",
        source="test_source",
        event_date="2024-01-01",
        in_game_date="2024-01-01"
    )
    assert event.event_id == "test_event_id"
    assert event.faction_ids == ["faction1", "faction2"]
    assert event.location_id == "test_location_id"
    assert event.character_ids == ["character1", "character2"]
    assert event.object_ids == ["object1", "object2"]
    assert event.background_information == "test_background"
    assert event.picture == "test_picture"
    assert event.source == "test_source"
    assert event.event_date == datetime.date(2024, 1, 1)
    assert event.in_game_date == datetime.date(2024, 1, 1)