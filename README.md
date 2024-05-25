# AlHakawatieh Backend

This is the backend project for the AlHakawatieh application, built using Flask.

## Prerequisites

Before you can run the server, you'll need to make sure you have the following installed:

1. **Python**: You can download the latest version of Python from the [official website](https://www.python.org/downloads/). Make sure to select the option to add Python to your system's PATH during the installation process.

2. **pip**: pip is the package installer for Python, and it should be installed automatically when you install Python. If you're having trouble with pip, you can follow the [official instructions](https://pip.pypa.io/en/stable/installation/) to install it.

## Running the Server

### Using the `run.bat` file

1. Clone the repository:

   ```
   git clone https://github.com/321abdulfatah/alhakawatieh-backend.git
   ```

2. Navigate to the project directory:

   ```
   cd alhakawatieh-backend
   ```

3. Run the `run.bat` file:

   ```
   run.bat
   ```

   This will install the required Python packages and start the Flask server. Make sure that the `python` and `pip` commands are available in your system's PATH.

   The server will be available at `http://localhost:5004`.

### Without the `run.bat` file

1. Clone the repository:

   ```
   git clone https://github.com/your-username/alhakawatieh-backend.git
   ```

2. Navigate to the project directory:

   ```
   cd alhakawatieh-backend
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

4. Start the Flask server:

   ```
   python app.py
   ```

   This will start the Flask server and make it available on `http://localhost:5004`.

## Endpoints

The backend server provides the following endpoints:

1. **Root Endpoint**: `GET /`
   - This endpoint returns a simple welcome message.

2. **Receive Story Endpoint**: `POST /receive_story`
   - This endpoint receives the story data, including the category and the base64-encoded image.
   - The server processes the image, counts the number of circles, and returns a response based on the category and the number of circles.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a new pull request, and we'll review your changes.
