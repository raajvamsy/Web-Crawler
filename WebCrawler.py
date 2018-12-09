from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Crawler:

    def __init__(self, depth=1, address=None):  # Default value of depth is 1 and Address is None.
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe",
                                       chrome_options=self.options
                                       )
        self.links = {address: 0}
        self.Address = address
        self.depth = depth

    def crawler(self):
        ln = 0  # ln is the value of the Depth
        while ln != self.depth:
            count = 0
            for i in self.links:  # This checks weather all the links in dictionary are visited or not.
                if self.links[i] == 0:
                    count += 1
            if count == 0:
                break
            alllink = list(self.links)  # All Links.
            for i in alllink:
                if self.links[i] != 1:
                    self.links[i] = 1  # Visited.
                    links = self.getlinks(str(i))
                    if links is not None:
                        dic = {}    # Temporary Dictionary to store the urls obtained.
                        for j in range(len(links)):
                            if links[j] not in alllink:  # and self.Address in links[j]: optional condition to get
                                # only site urls.
                                dic[links[j]] = 0
                        self.links.update(dic)  # Adds the Temp Dictionary to self.link by removing repetitions.
            ln += 1
        return list(self.links)

    def getlinks(self, address):  # This functions gets all the href links from a tag in site.
        links = []
        try:
            self.driver.get(address)
            for i in self.driver.find_elements_by_tag_name('a'):
                links.append(i.get_attribute('href'))
            return links
        except:
            return None


if __name__ == "__main__":
    crawl = Crawler(address="http://127.0.0.1:5500/home.html")
    print(crawl.crawler())
