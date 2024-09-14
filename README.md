
# Flask Pastebin App

This is a simple Flask-based internal Pastebin web application that allows users
to register and get their own API key. Each user can add notes and retrieve
their notes using API endpoints. The application is secured with API key
authentication.

## Features

- User registration with automatic API key generation.
- Add notes that are specific to each user.
- Retrieve notes based on the user's API key.
- No web interface, interaction is through API calls only.
- Deployed using Docker for easy containerized deployment.
- In-memory storage for notes (non-persistent).

## Running the App

The app is containerized and can be run with Docker.

### Steps to Run the App:

1. **Build the Docker Image**:
   ```bash
   docker build -t flask-pastebin .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -d -p 5000:5000 flask-pastebin
   ```

3. The app will now be available at `http://localhost:5000`.

## API Endpoints

### 1. **Sign Up and Get API Key**

Register a new user to get a unique API key.

**Request**:

```bash
curl -X POST http://localhost:5000/signup \
-H "Content-Type: application/json" \
-d '{"username": "your-username"}'
```

**Response**:

```json
{
    "message": "User registered successfully",
    "api_key": "your-generated-api-key"
}
```

### 2. **Add a New Note**

Use your API key to add a new note.

**Request**:

```bash
curl -X POST http://localhost:5000/add_note \
-H "Authorization: Bearer your-generated-api-key" \
-H "Content-Type: application/json" \
-d '{"note": "This is a new note!"}'
```

**Response**:

```json
{
    "message": "Note added successfully"
}
```

### 3. **Get All Notes**

Use your API key to retrieve all notes associated with your account.

**Request**:

```bash
curl -X GET http://localhost:5000/notes \
-H "Authorization: Bearer your-generated-api-key"
```

**Response**:

```json
{
    "notes": [
        "This is a new note!"
    ]
}
```

## License

This project is open-source and free to use under the MIT License.
