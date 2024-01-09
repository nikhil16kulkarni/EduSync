# EduSync - Course Recommender

EduSync is a course recommendation web application that utilizes machine learning techniques, including tf-idf and linear kernel, to provide personalized course recommendations based on user input. The application is designed to be user-friendly, with a simple web interface allowing users to input a course name and receive relevant recommendations.

## Features

- **User-Friendly Interface:** A straightforward and intuitive web interface for users to input a course name and receive personalized recommendations.
- **Course Recommendations:** Utilizes machine learning algorithms to analyze course titles and suggest similar courses.
- **Data Extraction Module:** Allows continuous extraction of course data from Udemy to keep recommendations up-to-date.
- **Flask Backend:** The backend is implemented using Flask, providing a serverless architecture for handling HTTP requests and responses.

## Prerequisites

Before you begin, ensure you have the following requirements:

- Python 3.x installed
- Python packages listed in `requirements.txt` installed (`pip install -r requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nikhil16kulkarni/EduSync.git

2. Change into the project directory:

   ```bash
   cd EduSync

3. Install the required packages:

   ```bash
   pip install -r requirements.txt

## Usage

1. Start the Flask server:
   ```bash
   python app.py
   
2. Open your web browser and go to
   ```bash
   http://127.0.0.1:5000/

4. Enter a course name in the provided input box and click the "Get Recommendations" button.

5. View the recommended courses displayed on the page.


## Machine Learning Module
The core recommendation functionality is powered by a machine learning module. The module includes the following components:

1. **Data Loading and Preprocessing:** The load_and_preprocess_data function reads course data from a CSV file, performs necessary preprocessing, and creates a combined features column for analysis.
2. **Similarity Matrix Calculation:** The calculate_similarity_matrix function uses tf-idf vectorization and linear kernel to calculate the similarity matrix.
3. **Recommendation Generation:** The get_recommendations function takes a course title as input, calculates its similarity to other courses, and returns a list of recommended courses.


## Flask Backend
The backend of EduSync is implemented using Flask, a lightweight web framework for Python. The backend handles user requests, interacts with the machine learning module, and serves the recommendations to the user.


## Additional Functionalities
**API Integration:** EduSync can automatically fetch courses from Udemy APIs. If a course is not found in the local dataset, it queries the Udemy API for relevant courses.
