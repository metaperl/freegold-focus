freegold-focus
==============

source code for my [Karatbars Affiliate Pages](http://TerrenceBrannon.com)

## Adding a new affiliate page

Create a folder for it (e.g. `lookout`)

Put the static files in img, js, css, etc.

Add the folder to the `subdirs` value in config.py

Make sure the HTML has an `affiliate_url` value even if it's empty:
    <a meld:id="affiliate_url"></a>

All pages have to have it - it goes directly to the Karatbars sign-up form.

Add a routing for the folder in `myapp.py` in the `Root` class.

Edit tools/new-user-welcome.rst and add a link to the new page.
