Wagtail Asciinema
=================

Implements
`asciinema-player <https://github.com/asciinema/asciinema-player>`__
embedding block.

Requirements (tested)
---------------------

-  Python 3.5+
-  Wagtail 1.9+
-  Django 1.10

Installation
------------

Install the library with pip:

.. code:: bash

    $ pip install wagtail-asciinema

Add ``wagtail_asciinema`` to your INSTALLED\_APPS setting like this:

.. code:: python

    INSTALLED_APPS = [
        ...
        'wagtail_asciinema',
    ]

Download ``asciinema-player`` sources from it's `release
page <https://github.com/asciinema/asciinema-player/releases>`__ and
then place it in your STATIC directory.

Add ``AsciinemaBlock`` to your StreamField:

.. code:: python

    from wagtail_asciinema.blocks import AsciinemaBlock
    asciinema = AsciinemaBlock(classname='full')

You can add a method to determine if you need to include asciinema code
into your static/js blocks:

.. code:: python

    from wagtail.wagtailcore.models import Page
    class ArticlePage(Page):
        @property
        def has_asciinema(self):
            for stream_child in self.content:
                if stream_child.block.name == 'asciinema':
                    return True
            return False

And then add asciinema on your page on demand:

.. code:: djangotemplate

    {% block extra_css %}
      {% if self.has_asciinema %}
        <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}frontend/asciinema/v2.4.1/asciinema-player.css">
      {% endif %}
    {% endblock %}
    {% block extra_js %}
      {% if self.has_asciinema %}
        <script src="{{ STATIC_URL }}frontend/asciinema/v2.4.1/asciinema-player.js"></script>
      {% endif %}
    {% endblock %}
