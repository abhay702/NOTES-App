from pydantic import BaseModel

class NoteModel(BaseModel):
    note_content: str  # Ensure this matches with the usage in your routes for adding notes.

class UpdateNoteModel(BaseModel):
    note_content: str  # Field expected in the incoming data
    