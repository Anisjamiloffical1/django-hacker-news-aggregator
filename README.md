# 🚀 Django Hacker News Dashboard

A modern Django-powered news aggregation platform that scrapes the latest articles from Hacker News, stores them in a database, and displays them through a beautiful Bootstrap dashboard.

## Features

* Scrape latest Hacker News articles
* Store news in SQLite/PostgreSQL
* Prevent duplicate articles
* Search articles by title
* Django Admin Panel
* Responsive Bootstrap 5 UI
* Animated news cards
* Display:

  * Title
  * URL
  * Author
  * Points
  * Comments

## Tech Stack

* Python 3
* Django
* BeautifulSoup4
* Requests
* SQLite / PostgreSQL
* Bootstrap 5
* HTML5
* CSS3

## Project Screenshots

Add screenshots here after deployment.

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/django-hacker-news-dashboard.git
cd django-hacker-news-dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

## Scrape Latest News

Run:

```bash
python manage.py scrape_news
```

Example Output:

```text
Number of articles found: 30
News scraped successfully!
```

## Project Structure

```text
django-hacker-news-dashboard/
│
├── manage.py
├── db.sqlite3
│
├── config/
│
├── hacker_news/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   │
│   └── management/
│       └── commands/
│           └── scrape_news.py
│
├── templates/
│   └── hacker_news/
│       └── news_list.html
│
└── static/
```

## Database Fields

| Field      | Type          |
| ---------- | ------------- |
| title      | CharField     |
| url        | URLField      |
| points     | IntegerField  |
| author     | CharField     |
| comments   | IntegerField  |
| created_at | DateTimeField |

## Future Improvements

* User Authentication
* Bookmark Articles
* Pagination
* REST API
* Scheduled Scraping with Celery
* Docker Support
* PostgreSQL Production Setup
* Dark Mode
* Category Filtering
* Trending Articles Analytics

## Learning Outcomes

This project demonstrates:

* Django Development
* Web Scraping
* Database Design
* Django Management Commands
* Bootstrap Frontend Development
* Search Functionality
* Git & GitHub Workflow

## License

This project is open-source and available for educational and portfolio purposes.
