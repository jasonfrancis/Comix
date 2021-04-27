"""labels.py - gtk.Label convenience classes."""

from gi.repository import Gtk as gtk
from gi.repository import Pango as pango


class FormattedLabel(gtk.Label):
    
    """FormattedLabel keeps a label always formatted with some pango weight,
    style and scale, even when new text is set using set_text().
    """
    
    def __init__(self, text='', weight=pango.Weight.NORMAL,
      style=pango.Style.NORMAL, scale=1.0):
        gtk.Label.__init__(self, text)
        self._weight = weight
        self._style = style
        self._scale = scale
        self._format()

    def set_text(self, text):
        gtk.Label.set_text(self, text)
        self._format()

    def _format(self):
        text_len = len(self.get_text())
        attrlist = pango.AttrList()
        attrlist.insert(pango.AttrWeight(self._weight, 0, text_len))
        attrlist.insert(pango.AttrStyle(self._style, 0, text_len))
        attrlist.insert(pango.AttrScale(self._scale, 0, text_len))
        self.set_attributes(attrlist)


class BoldLabel(FormattedLabel):
    
    """A FormattedLabel that is always bold and otherwise normal."""
    
    def __init__(self, text=''):
        FormattedLabel.__init__(self, text, weight=pango.Weight.BOLD)


class ItalicLabel(FormattedLabel):
    
    """A FormattedLabel that is always italic and otherwise normal."""
    
    def __init__(self, text=''):
        FormattedLabel.__init__(self, text, style=pango.Style.ITALIC)
