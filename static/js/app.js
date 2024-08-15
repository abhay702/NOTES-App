document.getElementById('addbtn').addEventListener('click', function() {
    var noteText = document.getElementById('addtxt').value;
    if (noteText.trim() === '') {
        alert('Please enter a note before adding.');
        return;
    }

    fetch('/notes/', {  // Ensure this URL is correct as per your FastAPI routing
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ note_content: noteText })  // Adjust 'note_content' based on your backend model
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        alert('Note added successfully!');
        document.getElementById('addtxt').value = ''; // Clear the input box after successful post
        // Optionally, you might want to update the UI here to show the new note without reloading the page
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error adding note: ' + error.message);
    });
});

function deleteNote(noteId) {
    fetch(`/notes/${noteId}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            alert('Note deleted successfully');
            // Remove the note element from the DOM
            document.getElementById(`note-${noteId}`).remove();
        } else {
            throw new Error('Failed to delete the note');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error deleting note: ' + error.message);
    });
}

function updateNote(noteId) {
    // Log to check if the function is triggered
    console.log("Update function called for note ID:", noteId);

    // Get the updated content from the textarea
    const updatedContent = document.getElementById(`edit-note-${noteId}`).value;

    // Check if the updated content is empty and alert the user if it is
    if (!updatedContent.trim()) {
        alert("Please enter some content before updating.");
        return; // Exit the function if no content
    }

    // Sending a PUT request to the server with the updated content
    fetch(`/notes/${noteId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ note_content: updatedContent })
    })
    .then(response => {
        if (!response.ok) { // If the server responds with a bad status
            throw new Error(`HTTP status ${response.status}`);
        }
        return response.json(); // Parsing the JSON body of the response
    })
    .then(data => {
        if (data.status === "success") {
            console.log('Success:', data.message);
            alert('Note updated successfully');

            // Optionally, you can update the DOM to reflect the new note content without reloading the page
            // For example, you might display the updated content statically instead of in a textarea
            const displayElement = document.getElementById(`display-note-${noteId}`);
            if (displayElement) {
                displayElement.innerText = updatedContent;
            }
        } else {
            throw new Error(data.message); // Throw an error if the API reports failure
        }
    })
    .catch(error => {
        console.error('Error updating note:', error);
        alert('Error updating note: ' + error.message);
    });
}
