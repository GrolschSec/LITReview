# LitReview

LitReview is a web application that allows users to create and manage tickets for literature reviews and publish reviews on existing tickets. The application is built using Django, Bootstrap, and SQLite.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)

## Features

- User registration and authentication
- Create, modify, and delete tickets for literature reviews
- Publish reviews on existing tickets
- View feed of all tickets and reviews
- View a user's own tickets and reviews

## Installation

1. Clone the repository:
```
git clone https://github.com/GrolschSec/litreview.git
```

2. Create a virtual environment:
```
cd litreview
python3 -m venv env
```

3. Activate the virtual environment:

- On Windows:

  ```
  env\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source env/bin/activate
  ```

4. Install the required packages:
```
pip install -r requirements.txt
```

5. Apply migrations:
```
python manage.py migrate
```

## Usage

1. Start the development server:
```
python manage.py runserver
```

2. Open your web browser and visit `http://127.0.0.1:8000/`.

3. Register a new user account or log in with an existing account.

4. Create tickets for literature reviews, publish reviews on existing tickets, and manage your own tickets and reviews.

