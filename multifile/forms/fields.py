

from django.core import validators
from django.core.exceptions import ValidationError

from django.forms import Field

from widgets import MultiFileInput

class MultiFileField(Field):
    """A multiple-valued file input field."""
    
    widget = MultiFileInput
    default_error_messages = {
        'invalid': _(u"No file was submitted. Check the encoding type on the form."),
        'missing': _(u"No file was submitted."),
        'empty': _(u"The submitted file is empty."),
        'max_length': _(u'Ensure this filename has at most %(max)d characters (it has %(length)d).'),
    }

    def __init__(self, *args, **kwargs):
        self.max_length = kwargs.pop('max_length', None)
        super(FileField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        if data in validators.EMPTY_VALUES:
            return None

        # UploadedFile objects should have name and size attributes.
        try:
            file_name = data.name
            file_size = data.size
        except AttributeError:
            raise ValidationError(self.error_messages['invalid'])

        if self.max_length is not None and len(file_name) > self.max_length:
            error_values =  {'max': self.max_length, 'length': len(file_name)}
            raise ValidationError(self.error_messages['max_length'] % error_values)
        if not file_name:
            raise ValidationError(self.error_messages['invalid'])
        if not file_size:
            raise ValidationError(self.error_messages['empty'])

        return data

    def clean(self, data, initial=None):
        if not data and initial:
            return initial
        return super(MultiFileField, self).clean(data)
