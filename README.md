# Django using Tailwind CSS

Web development using Django with Tailwind css, using for Deep Learning project purposes.

### Tech Stack

- [Django](https://www.djangoproject.com) `v5.1.3`
- [Tailwind CSS](https://tailwindcss.com) `v3.4.14`
- [Python](https://www.python.org) `v3.12.7`
- [Node.js](https://nodejs.org/) `v22.11.0`

## Getting Started

1. Use this repo as template or/and clone the project

```bash
git clone https://github.com/hibatillah/django-tailwindcss
cd django-tailwindcss
```

2. Make sure you have python installed, check version by running

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
> Django hot reload is not working because it runs different commands manager at the same time. <br>
> Haven't looked into it yet.

### Run command separately

```bash
cd deep_learning
python manage.py runserver
```

```bash
npm run watch
```

## Add new depedencies

Install your depedencies with `actived venv`, then add depedencies to [requirements.txt](/requirements.txt) with next command

```bash
pip freeze > requirements.txt
```

> Run this command everytime you add python depedencies into your project

## Convention

Read [Django documentation](https://docs.djangoproject.com)

- Modify logic in [views.py](/deep_learning/deep_learning/views.py)
- Set routing in [urls.py](/deep_learning/deep_learning/urls.py)
- Modify interface in [/templates](/deep_learning/templates)
- Static assets in [/static](/deep_learning/static)
- Styling directly using Tailwindcss or in [index.css](/deep_learning/static/css/index.css)
- Modify DOM in [index.js](/deep_learning/static/js/index.js)

> [!WARNING]
> Change `deep_learning` directory name will break the project structure. <br>
> If you want to change it, make sure to change all the reference in the project.