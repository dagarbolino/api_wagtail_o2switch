from django.db import models
from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from wagtail.api import APIField

from wagtail.fields import StreamField
from cheeseapi.utils.blocks import StoryBlock, InternalLinkBlock
from cheeseapi.utils.models import BasePage


class HomePage(BasePage):
    template = "pages/home_page.html"
    introduction = models.TextField(blank=True)
    hero_cta = StreamField(
        [("link", InternalLinkBlock())],
        blank=True,
        min_num=0,
        max_num=1,
    )
    body = StreamField(StoryBlock())
    featured_section_title = models.TextField(blank=True)

    search_fields = BasePage.search_fields + [index.SearchField("introduction")]

    api_fields = [
            APIField("introduction"),
            APIField("hero_cta"),
            APIField("body"),
            APIField("featured_section_title"),
            APIField("page_related_pages"),
        ]

    content_panels = BasePage.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("hero_cta"),
        FieldPanel("body"),
        MultiFieldPanel(
            [
                FieldPanel("featured_section_title", heading="Title"),
                InlinePanel(
                    "page_related_pages",
                    label="Pages",
                    max_num=12,
                ),
            ],
            heading="Featured section",
        ),
    ]