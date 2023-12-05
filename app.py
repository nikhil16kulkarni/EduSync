from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from ml_module import load_and_preprocess_data, calculate_similarity_matrix, get_recommendations

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load and preprocess data
file_path = 'D:/IUB/Sem3/ECC/Project/udemy_courses.csv'
df = load_and_preprocess_data(file_path)

# Calculate similarity matrix
cosine_sim = calculate_similarity_matrix(df)

# Serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Handle course recommendation logic
@app.route('/recommend', methods=['POST'])
def recommend_courses():
    data = request.json
    course_name = data.get('course_name', '')

    recommended_courses = get_recommendations(course_name, df, cosine_sim)

    print(f"Recommendations for '{course_name}': {recommended_courses}")  # Print recommendations to console

    return jsonify({'recommendations': recommended_courses})

if __name__ == '__main__':
    app.run(debug=True)
