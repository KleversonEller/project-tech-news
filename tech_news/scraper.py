# Requisito 1
import requests
import time
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text

        return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    new_list = selector.css(".cs-overlay-link::attr(href)").getall()
    return new_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page = selector.css(".next::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)

    title = selector.css(".entry-title::text").get().strip()
    url = selector.css("link[rel=canonical]::attr(href)").get()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css(".meta-category span.label::text").get()
    timestamp = selector.css(".meta-date::text").get()
    summary = selector.xpath("string(//p)").get().strip()
    writer = selector.css(".author a::text").get()
    comments = selector.css(".post-comments-simple h5::text").get() or 0

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://blog.betrybe.com"
    news = []
    page = 0

    while page < amount:
        html_content = fetch(url)
        link_news_by_page = scrape_novidades(html_content)

        for link in link_news_by_page:
            if page == amount:
                break
            new = scrape_noticia(fetch(link))
            news.append(new)
            page += 1

        url = scrape_next_page_link(html_content)

    create_news(news)
    return news
