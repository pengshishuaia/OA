from time import sleep


class Page():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://10.111.128.36:9080/OAFZHJ"
        self.timeout = 10

    def _open(self, url):
        url_ = self.base_url + url
        print("this page is %s" % url_)
        self.driver.get(url_)
        sleep(3)
        assert self.driver.current_url == url_, 'Did neot land out %s ' % url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
