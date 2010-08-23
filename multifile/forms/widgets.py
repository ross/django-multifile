from django import forms

class MultiFileInput(forms.widgets.Input):
    """A multiple-file FileInput widget."""

    input_type = 'file'

    needs_multipart_form = True

    class Media:
        js = ('js/jquery.js', 'js/jquery.multifile.js', )

    def render(self, name, value, attrs=None):
        """Render as usual, but with added class."""
        if attrs is None:
            attrs = {}

        if attrs.has_key('class'):
            attrs['class'] += ' multi'
        else:
            attrs['class'] = 'multi'

        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        """Return a list of the uploaded files."""

        return files.getlist(name)
