from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore import blocks
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class AsciinemaBlock(blocks.StructBlock):
    FONT_SIZE = (
        ('small', _('small')),
        ('medium', _('medium')),
        ('big', _('big')),
    )
    THEME = (
        ('asciinema',) * 2,
        ('tango',) * 2,
        ('solarized-dark',) * 2,
        ('solarized-light',) * 2,
        ('monokai',) * 2,
    )

    title = blocks.CharBlock(required=False)
    poster = blocks.CharBlock(required=False, default='npt:0:0', help_text=_('npt:2:34 || data:text/plain,Poster text'))
    document = DocumentChooserBlock(required=True)
    font_size = blocks.ChoiceBlock(FONT_SIZE, default='small')
    theme = blocks.ChoiceBlock(THEME, default='monokai')
    speed = blocks.IntegerBlock(default=1, min_value=1)
    start_at = blocks.CharBlock(default='0', help_text=_('123, mm:ss, hh:mm:ss'))
    cols = blocks.IntegerBlock(default=0, min_value=0, max_value=1024)
    rows = blocks.IntegerBlock(default=5, min_value=0, max_value=1024)
    loop = blocks.BooleanBlock(default=False, required=False)
    preload = blocks.BooleanBlock(default=False, required=False)
    autoplay = blocks.BooleanBlock(default=False, required=False)

    class Meta:
        icon = 'media'
        template = 'wagtail_asciinema/blocks/asciinema_block.html'
