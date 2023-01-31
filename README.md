# join-meet

API to join a meeting.

### Install requirements

(After creating a virtual environment)

```
pip install -r requirements.txt
```

### Create a .env file

(In the root directory)

```
EMAIL=your_email
PASSWORD=your_password
CHROME_DRIVER_PATH=your_chrome_driver_path
```

The chrome driver path can be found [here](https://chromedriver.chromium.org/downloads) depending on your chrome
version.

### Run the server

```
python manage.py runserver
```

### API for joining a google meet

(Go to the browser at this url)

```
http://localhost:8000/sweez/api/join_meet/google-meet/
```
