import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import re
from pyudemy import Udemy

udemy = Udemy("tnIIoAvRcZiGqOU83iakp1gflqdqTjxQX2zM4ODg", "GNxUEVdLERvcPew3xou5uWSASpDQzFFFZvZQToK6fFgFld7TQsfOJzB3qcgGYuQBf9ajY8HC6GDZH8MGM0xkpEGK3s4tbnIVdCD4fqFdIRZFayfLSh61mBBF35nDC8uj")


def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    columns_to_drop = ['predictive_score', 'relevancy_score', 'price']
    df = df.drop(columns=columns_to_drop)
    df.dropna(inplace=True)
    df = pd.get_dummies(df, columns=['locale_title'], drop_first=True)
    df['cleaned_title'] = df['title'].str.lower().str.replace('[^a-zA-Z0-9]', ' ', regex=True)
    df['combined_features'] = df['cleaned_title'] + ' ' + df['visible_instructors'].fillna('') + ' ' + df['published_title'].fillna('') + ' ' + df['headline'].fillna('')
    return df

def calculate_similarity_matrix(df):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

def get_recommendations(course_title, df, cosine_sim):
    cleaned_title = re.sub(r'[^a-zA-Z0-9]', ' ', course_title.lower())

    # Check if the cleaned title exists in the DataFrame
    if cleaned_title not in df['cleaned_title'].values:
        ls = []
        print(f"Course '{course_title}' not found in the DataFrame.")
        print(course_title)
        tmp_courses = udemy.courses(search=course_title)
        cnt = 0
        for i in tmp_courses['results']:
            ls.append(i['title'])
            if(cnt == 5):
                break
            cnt+=1
        print(ls)
        return ls

    idx = df[df['cleaned_title'] == cleaned_title].index[0]

    # Get the pairwise similarity scores with other courses
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the courses based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 similar courses (excluding the input course itself)
    sim_scores = sim_scores[1:6]

    # Get the course indices
    course_indices = [score[0] for score in sim_scores]

    # Return the top 5 recommended courses
    recommended_courses = df['title'].iloc[course_indices].tolist()
    return recommended_courses

# # Example usage:
# file_path = 'D:/IUB/Sem3/ECC/Project/udemy_courses.csv'
# df = load_and_preprocess_data(file_path)
# cosine_sim = calculate_similarity_matrix(df)

# # Test the get_recommendations function
# course_title = 'Docker on Windows 10 and Server 2016'
# recommendations = get_recommendations(course_title, df, cosine_sim)
# print(f"\nRecommendations for '{course_title}':")
# print(recommendations)
