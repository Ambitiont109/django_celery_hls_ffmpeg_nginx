# Basic Django Celery Example for HLS (Http Live Streaming) with ffmpeg

You could git clone this repository to get it working but I recommend following these manual steps so you understand what's required to get a basic Celery example up and running.

- Before you start, you'll need a Redis server. If you don't have one the easiest way is through Docker with the following command:

```bash
docker run --name my-redis-server -d -p 127.0.0.1:6379:6379 redis
```
- Also you have to install ffmpeg for streaming
```bash
sudo apt update
sudo apt install ffmpeg
```

- Create a virtual environment using the method of your choice, I like to use the following command:

```bash
python3.8 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip wheel setuptools > /dev/null
```

- Create the requirements.txt file to install the packages required:

```
django
redis
celery
```

- Activate your virtual environment and install the requirements in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

- Now you need to launch the Django test server:

```bash
python manage.py runserver
```

- Then in a second terminal window, navigate to your project directory, activate the virtual environment again, and then launch the Celery process - it should print out some debug information and then a `ready` message to indicate it has connected to Redis successfully and is waiting for tasks:

```bash
python -m celery -A celery_project worker -l info -P solo
```

- Browse to http://127.0.0.1 and you should see a form. Try inputing a url of the video , it can be local file url or stream link  
- After start streaming, you should see the streamed url. 

Hopefully that worked for you and gives you something to build upon.

- Input below urls for test
  1. https://skyfire.vimeocdn.com/1644500168-0x51bef7dacbefd83d0d90cb89a337cea22e5db7e8/a1d2a1ff-b876-48c2-9136-ef75b64e78ef/sep/video/004b12d5/playlist.m3u8
  2. https://11vod-adaptive.akamaized.net/exp=1644500209~acl=/45c3c211-588e-4711-ab2a-c691e69008ea/*~hmac=934ea53ea5dc24acc11c6e5787a5100bd356021ef14669d7c55d92a8163670a2/45c3c211-588e-4711-ab2a-c691e69008ea/sep/video/5b0bf124/playlist.m3u8
  3. https://197vod-adaptive.akamaized.net/exp=1644500115~acl=/d59b5cf6-c9a4-41e6-b4a9-12ac91516dc4/*~hmac=0913c3d00009b1f61a3ab5d444ae8d3d855fc57c14b89828beb7b9d631bd504c/d59b5cf6-c9a4-41e6-b4a9-12ac91516dc4/sep/video/1fcbbedd/playlist.m3u8
