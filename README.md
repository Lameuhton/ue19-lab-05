# ue19-lab-05 : Python API & Docker

A simple Python 3 application that queries a public API service using the `requests` library.

## Features

* Queries the API service: **[JokesAPI]**
* The program retrieves and displays: **[A random joke]**
* The application is containerized using Docker.

## Prerequisites

To run this project, you will need:

1.  **Python 3.x** and **pip** (if running the application without Docker).
2.  **Docker** (for the recommended method).

## 🚀 Installation & Launch

You have two options to execute this program:

### Option 1: With Docker (Recommended)

This is the "zero-fuss" method that ensures the environment is always pristine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)Lameuhton/ue19-lab-05.git
    cd ue19-lab-05
    ```

2.  **Build the Docker image:**
    ```bash
    docker build -t ue19-lab-05 .
    ```

3.  **Run the container:**
    The program will execute, display its result directly, and then stop.
    ```bash
    docker run --rm ue19-lab-05
    ```
    *(The `--rm` flag removes the container after execution to keep things clean.)*

### Option 2: Locally (Python Environment)

If Docker isn't your thing and you prefer to handle dependencies manually.

1.  **Clone the repository and navigate to the folder** (see step 1 above).

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the script:**
    ```bash
    python app.py
    ```

## 📦 Dependencies

Dependencies are listed in `requirements.txt`:

* `requests`: Used to perform HTTP requests to the API.