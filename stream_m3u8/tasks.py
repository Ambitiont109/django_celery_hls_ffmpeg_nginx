from __future__ import absolute_import, unicode_literals

import os
import subprocess
import time

from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail, BadHeaderError
from celery_project.settings import DEFAULT_FROM_EMAIL


logger = get_task_logger(__name__)


@shared_task(bind=True)
def stream_task(self, url_list: []):
    for url in url_list:
        self.update_state(state="PROGRESS", meta={'current_url': url})
        if url == "":
            continue
        # shell_command = f'''ffmpeg -re -i {url} -c copy -f flv rtmp://127.0.0.1/live/stream'''
        shell_command = f'''streamlink -O --http-header "User-Agent='Mozilla/5.0 \
        (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'" "hlsvariant://{url}" \
        best | ffmpeg -re -i - -acodec aac -strict -2 -ab 48000 -ar 48000 -vcodec copy -f flv "rtmp://127.0.0.1:443/live/stream"\
        '''
        logger.info(f"start stream from rtmp://127.0.0.1/live/stream with the content of {url}")
        logger.info(shell_command)
        proc = subprocess.Popen(shell_command ,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,preexec_fn=os.setsid)
        logger.info(f"Proc Id:{proc.pid}")
        while proc.poll() is None:
            logger.info(f"streaming .....")
            time.sleep(2)
        logger.info("Wait next Url")
        time.sleep(60)


@shared_task(bind=True)
def test_task(self, url_list:[]):
    cnt = 1
    while cnt < 30:
        cnt = cnt + 1
        logger.info(f"streaming .....")
        time.sleep(2)
