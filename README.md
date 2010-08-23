Django MultiFile
================

This is a Django app that provides simple support for multiple-file input
fields in Django forms. This makes it easier to keep all your validation and
handling code in the form class.

It probably doesn't deserve to be an app, but I don't have enough repositories
on [GitHub][1]!

Usage
-----

Using this is pretty simple: just import `multifile.forms.MultiFileField` and
use it in a form!

Of course, you'll need to make sure you've got the media (in particular,
[jQuery][2] and the [Multiple File Upload][3] plugin) installed in the correct
place. By default, they're included as `MEDIA_URL/js/jquery.js` and
`MEDIA_URL/js/jquery.multifile.js`. If you need this to be somewhere else,
you'd probably be better offer just modifying the code than 


[1]: http://github.com/thsutton/
[2]: http://www.jquery.com/
[3]: http://www.fyneworks.com/jquery/multiple-file-upload/