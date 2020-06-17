from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from bidi.algorithm import get_display
from arabic_reshaper import reshape
from kivy.properties import NumericProperty, StringProperty


def to_ar(txt):
    return get_display(reshape(txt))


class ToAr:
    def __init__(self, ori):
        self.ori = ori

    def to_ar(self):
        return get_display(reshape(self.ori))


class Arbutton(Button):
    def __init__(self, **kwargs):
        super(Arbutton, self).__init__(**kwargs)
        self.text = to_ar(self.text)
        self.font_name = "tahomabd.ttf"


class Arlabel(Label):
    def __init__(self, **kwargs):
        super(Arlabel, self).__init__(**kwargs)
        self.text = get_display(reshape(self.text))
        self.font_name = "tahomabd.ttf"


class ArInput(TextInput):
    str = StringProperty()
    max_char = NumericProperty(1000)

    def __init__(self, **kwargs):
        super(ArInput, self).__init__(**kwargs)
        self.text = get_display(reshape(self.text))
        self.font_name = "tahomabd.ttf"
        self.hint_text = get_display(reshape(self.hint_text))
        self.halign = "right"

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.str) + len(substring) > self.max_char):
            return
        self.str = self.str + substring
        self.text = get_display(reshape(self.str))
        substring = ''
        super(ArInput, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(reshape(self.str))


