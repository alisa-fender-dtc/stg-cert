from general import *
import requests
from bs4 import BeautifulSoup
from urllib import parse


class Spider:
    log_dir = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    redirects_file = ''
    fail_file = ''
    queue = set()
    crawled = set()

    def __init__(self, log_dir, base_url, domain_name):
        Spider.log_dir = log_dir
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.log_dir + 'queue.txt'
        Spider.crawled_file = Spider.log_dir + 'crawled.txt'
        Spider.redirects_file = Spider.log_dir + 'redirects.txt'
        Spider.fail_file = Spider.log_dir + 'failed.txt'
        # print("Queue File: {} Crawled File: {}".format(Spider.queue_file, Spider.crawled_file))

        self.boot()
        self.crawl_page('Initial spider', Spider.base_url)

    @staticmethod
    def boot():
        create_log_dir(Spider.log_dir)
        create_data_files(Spider.log_dir, Spider.base_url)
        create_files_from_list([Spider.redirects_file, Spider.fail_file])
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)


    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            # print("Thread: {} crawling {}".format(thread_name, page_url))
            # print("Queued: {} -- Crawled: {}".format(len(Spider.queue), len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def check_response(response, page_url):
        good = True
        if response.history:
            history_string = ''
            for r in response.history:
                history_string = history_string + str(r.status_code) + ': ' + r.url + ' | '
            result_string = page_url + " was redirected to " + response.url + " History: " + history_string
            print(result_string)
            good = False
            append_to_file(Spider.redirects_file, result_string)
            return good
        if response.status_code != 200:
            good = False
            append_to_file(Spider.fail_file, str(response.status_code) + ": " + page_url)
            print(("{} got status code {}".format(page_url, response.status_code)))
        return good


    @staticmethod
    def gather_links(page_url):
        # print("Gathering links with soup. {}".format( page_url))
        links = set()
        try:
            response = requests.get(page_url)
            Spider.check_response(response, page_url)
            plain_text = response.text
            # print(plain_text)
            soup = BeautifulSoup(plain_text, features="lxml")
            for link in soup.findAll('a'):
                href = link.get('href')

                if href == None:
                    # print("href is None")
                    continue

                # print("Joining {}".format(href))
                url =  parse.urljoin(Spider.base_url, href)
                links.add(url)
        except Exception as e:
            print("Error crawling {}. {}".format(page_url, e))
        return links

    # Opted to use requests and beautiful soup instead
    # @staticmethod
    # def gather_links(page_url):
    #     html_string = ''
    #     try:
    #         response = urlopen(page_url)
    #         if response.getheader('Content-Type') == 'text/html':
    #             html_bytes = response.read()
    #             html_string = html_bytes.decode("utf-8")
    #         finder = LinkFinder(Spider.base_url, page_url)
    #         finder.feed(html_string)
    #     except Exception as e:
    #         print("Error: {} Cannot crawl {}".format(e, page_url))
    #         return set()
    #     return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
