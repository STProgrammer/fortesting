# InsightMint

This project is a lightweight Django prototype for **InsightMint**, an AI-powered report builder for personal brands and coaches. It includes:

- Marketing landing page
- Simple onboarding flow
- Report creation with tone and persona options
- Basic WYSIWYG editor using Quill
- Example social app (from original repository) under `/social/`

Due to environment limitations, required packages like Django may not be installed automatically. Install dependencies with `pip install django` and run migrations:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Access the landing page at `http://localhost:8000/`.
