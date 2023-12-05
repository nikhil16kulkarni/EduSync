# EduSync - Course Recommender

EduSync is a course recommendation web application that utilizes natural language processing (NLP) to provide users with personalized course recommendations based on their input.


## Features

- **User-Friendly Interface**: A simple and intuitive web interface for users to input a course name and receive recommendations.
- **Course Recommendations**: Utilizes machine learning to analyze course titles and suggest similar courses.
- **Data Extraction Module**: Allows continuous extraction of course data from Udemy to keep the recommendations up-to-date.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Python packages listed in `requirements.txt` installed (`pip install -r requirements.txt`)


## Installation

1. Clone the repository:

   ```git clone https://github.com/nikhil16kulkarni/EduSync.git```

2. Change into the project directory:

   ```cd EduSync```

3. Install the required packages:

   ```pip install -r requirements.txt```

## Usage

1. Start the Flask server:

   ```python app.py```

2. Open your web browser and go to http://127.0.0.1:5000/

3. Enter a course name in the provided input box and click the "Get Recommendations" button.

4. View the recommended courses displayed on the page.
