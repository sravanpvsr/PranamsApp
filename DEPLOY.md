# Deploying to PythonAnywhere

Site: https://pranams2.pythonanywhere.com · account `pranams2` · Python **3.10**
(Django 3.2 does not run on 3.13).

Paths below assume the code lives in `/home/pranams2/PranamsApp`. If the Web
tab's **Source code** shows a different folder, use that everywhere instead.

All commands run in a PythonAnywhere **Bash console**.

## 0. Back up the live database first

The live `db.sqlite3` on the server is the real data, and it may be newer than
the copy in GitHub.

```bash
mkdir -p ~/backups
cp ~/PranamsApp/db.sqlite3 ~/backups/db.sqlite3.$(date +%Y%m%d-%H%M%S)
ls -l ~/backups
```

## 1. Get the code

**If `~/PranamsApp` already exists:**

```bash
cd ~/PranamsApp
git status            # must show nothing modified except db.sqlite3 / media/
git pull origin master
```

If `git status` lists other modified files (e.g. `DjangoAPI/settings.py` edited
on the server), stop and sort those out before pulling.

**First-time setup only:**

```bash
cd ~
git clone https://github.com/sravanpvsr/PranamsApp.git
```

A fresh clone brings GitHub's copy of `db.sqlite3` and `media/`. If an older
deployment exists elsewhere, copy its `db.sqlite3` and `media/` over these.

## 2. Virtualenv (Python 3.10)

```bash
mkvirtualenv --python=/usr/bin/python3.10 pranams-venv
pip install -r ~/PranamsApp/requirements.txt
python --version      # Python 3.10.x
```

Next time, activate it with `workon pranams-venv`.

## 3. Create `.env`

```bash
cd ~/PranamsApp
cp .env.example .env
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
nano .env
```

Paste the generated key as `DJANGO_SECRET_KEY=...` and keep
`DJANGO_DEBUG=False`. `.env` is gitignored, so never commit it.

A new secret key logs everyone out once. That's expected.

## 4. Check, then record the baseline migration

```bash
cd ~/PranamsApp
python manage.py check --deploy
python manage.py migrate --plan
```

`--plan` must list **only** `PranamsApp.0001_initial` (followed by its
"Create model ..." lines). If anything else appears, stop and don't migrate.

```bash
python manage.py migrate --fake-initial
python manage.py showmigrations PranamsApp    # [X] 0001_initial
```

The output should say `Applying PranamsApp.0001_initial... FAKED`. The tables
already exist, so Django only records the migration and changes no data.

## 5. Web tab

| Setting | Value |
|---|---|
| Python version | 3.10 |
| Source code | `/home/pranams2/PranamsApp` |
| Working directory | `/home/pranams2/PranamsApp` |
| Virtualenv | `/home/pranams2/.virtualenvs/pranams-venv` |
| Force HTTPS | **Enabled** (needed: login cookies are HTTPS-only) |

**WSGI configuration file**: open
`/var/www/pranams2_pythonanywhere_com_wsgi.py` and replace everything in it
with the contents of `pythonanywhere_wsgi.py` from this repo.

**Static files** mappings:

| URL | Directory |
|---|---|
| `/static/` | `/home/pranams2/PranamsApp/static` |
| `/media/` | `/home/pranams2/PranamsApp/media` |

Admin, DRF and bootstrap assets are already committed in `static/`, so you
don't need to run `collectstatic`.

## 6. Reload and verify

Click the green **Reload** button, then open:

- https://pranams2.pythonanywhere.com/ (the home page)
- https://pranams2.pythonanywhere.com/admin/login/ (the styled admin login)
- a resident photo under `/media/...`

## Logs

Web tab → **Log files**, or in a console:

```bash
tail -n 50 /var/log/pranams2.pythonanywhere.com.error.log    # tracebacks
tail -n 50 /var/log/pranams2.pythonanywhere.com.server.log   # print() output
tail -n 50 /var/log/pranams2.pythonanywhere.com.access.log
```

With `DEBUG=False`, errors show as a plain "Server Error (500)" page and the
traceback goes to the error log.

## Routine updates

```bash
cp ~/PranamsApp/db.sqlite3 ~/backups/db.sqlite3.$(date +%Y%m%d-%H%M%S)
cd ~/PranamsApp && git pull origin master
workon pranams-venv && pip install -r requirements.txt
python manage.py migrate --plan     # apply with `migrate` only if it lists what you expect
```

Then **Reload** on the Web tab.

## Local development

```bash
python3.10 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # set DJANGO_DEBUG=True and any DJANGO_SECRET_KEY
python manage.py runserver
```

`DJANGO_DEBUG=True` also turns off HTTPS-only cookies, so logging in over
plain http://127.0.0.1 works. To test from a phone on the same Wi-Fi, add
your laptop's IP to `DJANGO_ALLOWED_HOSTS` in `.env`.

When creating migrations, always name the app:
`python manage.py makemigrations PranamsApp`. Afterwards, check that nothing
was written into `venv/.../river/migrations/`. django-river otherwise
generates a migration inside the installed package, and the server won't
have it.
