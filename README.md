

# Notes App

This is a simple Notes application built with FastAPI and MongoDB. The application allows users to add, delete, update, and view notes. The frontend is rendered using Jinja2 templates, and the backend handles API requests for managing notes.

## Project Structure

```
NOTESAPP/
│
├── app/
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   └── routers.py
│
├── env/
│
├── static/
│   └── js/
│       └── styles.css
│
├── templates/
│   └── index.html
│
└── requirements.txt
```

### Files Overview

- **app/config.py**: 
  - Contains the configuration for the application including database connection, logging setup, and template initialization.

- **app/main.py**: 
  - Defines the FastAPI application and includes routers and static file mounting.

- **app/models.py**: 
  - Defines the Pydantic models used for validating and serializing the data.

- **app/routers.py**: 
  - Contains the API routes for handling requests related to notes such as adding, deleting, updating, and fetching notes.

- **static/js/styles.css**: 
  - Contains the CSS styling for the frontend.

- **templates/index.html**: 
  - The Jinja2 template used for rendering the home page with the list of notes.

- **requirements.txt**: 
  - Lists the Python dependencies required to run the application.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- MongoDB
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abhay702/NOTES-App.git
   cd NOTES-App
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**:

   Ensure that MongoDB is running, and update the connection string in `config.py` if necessary.

### Running the Application

To start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000/`.

### Usage

- **Home Page**: The home page displays a list of all notes.
- **Add Note**: Use the API endpoint `/notes/` to add a new note.
- **Delete Note**: Use the API endpoint `/notes/{note_id}` to delete a note by its ID.
- **Update Note**: Use the API endpoint `/notes/{note_id}` to update an existing note by its ID.

### API Endpoints

- `GET /`: Fetch and display all notes.
- `POST /notes/`: Add a new note.
- `DELETE /notes/{note_id}`: Delete a note by ID.
- `PUT /notes/{note_id}`: Update a note by ID.
