# dataVisualizer

```bash
version alpha
```
DataVisualizer is a proof of concpet for Flask-based application for data visualization. This application is containerized using Docker and can be run in a local environment. This README will guide you through setting up and running the application in a Docker container.

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.9 (for testing outside of Docker if needed)
- `pip` (Python package manager)

## Environment Variables

Before running the application, ensure to create an `.env` file in the root directory that contains the required infos

`.env` file:
```bash
DB_PATH="sqlDB.db"
OPENAI_API_KEY="Your_openai_apikey"
OPENAI_ORGA_ID="Your organization ID"
OPENAI_PROJECT_ID="Your project ID"
```

### How to get openai api key ?

- [Create an openAI account](https://openai.com/api/)
- [Get my API_KEY](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)

to get your organization ID and Project ID go to your settings page once you're done creating your profile. 

## Running the Application

### Using Docker Compose

The easiest way to run the application is by using Docker Compose. This will build the Docker image and start the application in a container.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/data-visualizer.git
   cd data-visualizer
   ```

2. **Build and run the container**:
   ```bash
   docker-compose up -d
   ```

   This will:
   - Build the Docker image from the provided `Dockerfile`.
   - Start a container for the application.
   - The application will be available locally on port `8000`.

3. **Access the application**:
   Open your web browser and go to:
   ```
   http://localhost:8000
   ```

### Stopping the Application

To stop the running containers, use:
```bash
docker-compose down
```

This will stop and remove the running containers but leave the built image intact.

## Project Structure

```plaintext
/app
│   ├── dataVisualizer.py   # Main Flask application
│   ├── init_data.py        # Script to initialize database
│   ├── Dockerfile          # Dockerfile for building the container
│   ├── entrypoint.sh       # Entrypoint script for the container
│   ├── requirements.txt    # Python dependencies
│   ├── .env                # Environment variables
│   └── templates/          # HTML templates for the Flask app
│
└── docker-compose.yml      # Docker Compose configuration
```

## Dockerfile

The Dockerfile performs the following tasks:

- Sets up a Python environment with required dependencies.
- Copies the application code into the container.
- Installs the necessary Python packages.
- Runs the Flask application using Gunicorn in production mode.

## Running Without Docker (Optional)

If you wish to run the application outside of Docker, you can do so using Python and pip.

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scriptsctivate      # On Windows
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   ```bash
   export FLASK_ENV=production
   python dataVisualizer.py
   ```

4. **Access the application**:
   Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Troubleshooting

- **Connection Refused Error**: Ensure that Docker Compose is mapping the correct port (`8000:8000`). Check for any firewall settings that may block access to port 8000.
- **Permission Errors**: Make sure the `entrypoint.sh` script has the correct execution permissions. Run:
  ```bash
  chmod +x entrypoint.sh
  ```

## License

This project is licensed under the MIT License.
