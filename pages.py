from page_base import PageBase
from search_page import SearchPage
from playlist import PlayList
from typing import Dict
from kivy.uix.layout import Layout

def validate_dependenties(*args):
    def decorator(func):
        def wraperr(*args):
            if not all(args):
                raise AttributeError

        return wraperr

    return decorator

class Pages:
    pages : Dict[str, PageBase] = {
        "SearchPage" : SearchPage(),
        "PlayList" : PlayList()
    }

    last_page : PageBase = None
    main_layout : Layout = None

    @classmethod
    def init(cls, main_layout : Layout, pages : Dict = dict()):
        if len(pages) != 0:
            cls.pages = pages

        cls.main_layout = main_layout

    @classmethod
    def load_page(cls, page_name : str):
        if cls.last_page:
            cls.last_page.clear_page()

        if page_type := cls.pages.get(page_name):
            cls.last_page = page_type
            cls.main_layout.add_widget(cls.last_page.build(), 10)

        