# Requisito 6
import datetime
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        format_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        news = search_news({"timestamp": {"$regex": format_date}})
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    news = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    )
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]
