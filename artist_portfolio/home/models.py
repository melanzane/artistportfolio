# home/models.py

from django.db import models

from wagtail import blocks
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page


# ---------------------------------------------------------
# HOMEPAGE
# ---------------------------------------------------------

class HomePage(Page):

    body = RichTextField(blank=True)

    about_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Seite, die im Menü unter 'About' verlinkt wird.",
    )

    # Wird im Menü unter 'Gallery' verwendet
    gallery_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Seite, die im Menü unter 'Gallery' verlinkt wird.",
    )

    contact_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Seite, die im Menü unter 'Contact' verlinkt wird.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        PageChooserPanel("about_page", "home.AboutPage"),
        PageChooserPanel("gallery_page", "home.GalleryPage"),
        PageChooserPanel("contact_page", "home.ContactPage"),
        # media_page lassen wir bewusst im Panel weg, solange du sie nicht brauchst
    ]

    class Meta:
        verbose_name = "Home Page"


# ---------------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------------

class AboutPage(Page):

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    class Meta:
        verbose_name = "About Page"


# ---------------------------------------------------------
# GALLERY PAGE
# ---------------------------------------------------------

class GalleryPage(Page):

    gallery_images = StreamField(
        [
            ("image", ImageChooserBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("gallery_images"),
    ]

    class Meta:
        verbose_name = "Gallery Page"


# ---------------------------------------------------------
# CONTACT PAGE
# ---------------------------------------------------------

class ContactPage(Page):

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Contact Page"
