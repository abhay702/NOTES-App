from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from .config import notes_collection, templates  # Ensure these are correctly defined in your config module
from .models import NoteModel,UpdateNoteModel
import logging
from fastapi import APIRouter, HTTPException, Body
from bson import ObjectId
from pymongo.errors import PyMongoError

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home_route(request: Request):
    try:
        notes_cursor = notes_collection.find({})
        notes = [note for note in notes_cursor]  # Convert cursor to list
        return templates.TemplateResponse("index.html", {"request": request, "notes": notes})
    except Exception as e:
        logging.error(f"Failed to fetch notes: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/notes/")
async def add_note(note: NoteModel):
    try:
        result = notes_collection.insert_one({"note": note.note_content})
        return {"status": "success", "id": str(result.inserted_id)}
    except Exception as e:
        logging.error(f"Failed to add note: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/notes/{note_id}")
async def delete_note(note_id: str):
    logging.info(f"Attempting to delete note with ID: {note_id}")
    try:
        result = notes_collection.delete_one({"_id": ObjectId(note_id)})
        if result.deleted_count == 1:
            logging.info("Deletion successful")
            return {"status": "success", "message": "Note deleted successfully"}
        else:
            logging.info("Note not found")
            return {"status": "failure", "message": "Note not found"}
    except Exception as e:
        logging.error(f"Error deleting note: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.put("/notes/{note_id}")
async def update_note(note_id: str, note_data: UpdateNoteModel = Body(...)):
    try:
        # Attempt to update the note in the database
        result = notes_collection.update_one(
            {"_id": ObjectId(note_id)},
            {"$set": {"note": note_data.note_content}}
        )
        if result.modified_count == 0:
            # No document was modified, likely the note wasn't found
            return {"status": "failure", "message": "Note not found or no update made"}
        return {"status": "success", "message": "Note updated successfully"}
    except PyMongoError as e:
        logging.error(f"Database error when updating note: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error when updating note: {e}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
