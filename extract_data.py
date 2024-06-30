import requests
from bs4 import BeautifulSoup

def fetch_course_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        courses = []

        for course in soup.find_all('div', class_='course-card'):
            title = course.find('h3').text.strip()
            description = course.find('p', class_='description').text.strip()
            courses.append({'title': title, 'description': description})

        return courses
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")