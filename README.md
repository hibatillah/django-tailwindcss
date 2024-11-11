# Django using Tailwind CSS

Web development using [Django](https://www.djangoproject.com) `v5.1.3` and styling using [Tailwind CSS](https://tailwindcss.com) `v3.4.14` for Deep Learning audio classification. <br>
This project using [Python](https://www.python.org) `v3.12.7` and [Node.js](https://nodejs.org/) `v22.11.0`.

## Getting Started

1. Clone this project

```bash
git clone https://github.com/hibatillah/django-tailwindcss
cd django-tailwindcss
```

2. Make sure you have Python installed, check version by running

```bash
python --version
```

4. Create virtual environment (venv)

```bash
python -m venv venv
```

5. Activate virtual environment (venv)

```bash
# on windows
venv/Scripts/activate

# on mac
source venv/bin/activate
```

> [!IMPORTANT]
> Make sure to always `activate venv before run project`

6. Install Depedencies

```bash
pip install -r requirements.txt
npm install
```

7. Run project

```bash
invoke start
```

8. Project running on http://localhost8000

> [!NOTE]
> All command `run concurrently` using invoke scripts. <br>
> Modify command in [tasks.py](/tasks.py).
>
> All the required depedencies store in [`requirements.txt`](/requirements.txt) and [`pakcage.json`](/package.json).

> [!WARNING]
> Django hot reload is not working because it runs different commands at the same time.

### Run command separately

```bash
cd audio_classification
python manage.py runserver
```

```bash
npm run watch
```

## Add new depedencies

Install your depedencies while `venv is active`, then add depedencies to [requirements.txt](/requirements.txt)

```bash
pip freeze > requirements.txt
```

> Run this command everytime you add python depedencies into your project

## Convention

Read [Django documentation](https://docs.djangoproject.com).

- Modify logic in [views.py](/audio_classification/audio_classification/views.py)
- Set routing in [urls.py](/audio_classification/audio_classification/urls.py)
- Modify interface in [/templates](/audio_classification/templates)
- Static assets in [/static](/audio_classification/static)
- Styling directly using Tailwindcss or in [index.css](/audio_classification/static/css/index.css)
- Modify DOM in [index.js](/audio_classification/static/css/index.js)
