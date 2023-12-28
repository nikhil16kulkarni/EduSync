from pyudemy import Udemy
import csv

udemy = Udemy("tnIIoAvRcZiGqOU83iakp1gflqdqTjxQX2zM4ODg", "GNxUEVdLERvcPew3xou5uWSASpDQzFFFZvZQToK6fFgFld7TQsfOJzB3qcgGYuQBf9ajY8HC6GDZH8MGM0xkpEGK3s4tbnIVdCD4fqFdIRZFayfLSh61mBBF35nDC8uj")

def write_courses_to_csv(courses, csv_filename):
    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'url', 'is_paid', 'price', 'visible_instructors',
                      'is_practice_test_course', 'published_title', 'locale_title',
                      'predictive_score', 'relevancy_score', 'headline']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        for course in courses['results']:
            instructor_name = ''
            if course['visible_instructors']:
                instructor_name = course['visible_instructors'][0]['title']

            locale_title = ''
            if 'locale' in course and 'title' in course['locale']:
                locale_title = course['locale']['title']

            writer.writerow({
                'id': course['id'],
                'title': course['title'],
                'url': course['url'],
                'is_paid': course['is_paid'],
                'price': course.get('price', ''),
                'visible_instructors': instructor_name,
                'is_practice_test_course': course['is_practice_test_course'],
                'published_title': course['published_title'],
                'locale_title': locale_title,
                'predictive_score': course.get('predictive_score', ''),
                'relevancy_score': course.get('relevancy_score', ''),
                'headline': course.get('headline', '')
            })

if __name__ == "__main__":
    csv_filename = 'udemy_courses.csv'

    for page_number in range(1, 5):  
        courses = udemy.courses(page=page_number, page_size=100)
        write_courses_to_csv(courses, csv_filename)

    print(f"CSV file '{csv_filename}' has been created successfully.")
