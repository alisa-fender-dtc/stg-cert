import threading
from queue import Queue
from spider.spider import Spider
from spider.domain import *
from spider.general import *
from common.slingqa_utils import utils



PROJECT_NAME = 'sling'
HOMEPAGE = 'https://www.sling.com'
DOMAIN_NAME = get_sub_domain_name(HOMEPAGE)

ut = utils()
LOG_DIR = '../logs/' + PROJECT_NAME + '_' + ut.get_timestamp() + '/'

QUEUE_FILE = LOG_DIR + 'queue.txt'

NUMBER_OF_THREADS = 8

t_queue = Queue()
Spider(LOG_DIR, HOMEPAGE, DOMAIN_NAME)

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = t_queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        t_queue.task_done()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        t_queue.put(link)
    t_queue.join()
    crawl()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("{} links in queue.".format(len(queued_links)))
        create_jobs()


create_workers()
crawl()