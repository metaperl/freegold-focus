freegold-focus
==============

source code for my [Karatbars Affiliate Pages](http://TerrenceBrannon.com)

## Deploying to Apache

    <Macro WSGISite $domain ${approot} $script>
    <VirtualHost *:80>
       ServerName $domain
       WSGIScriptAlias / ${approot}/$script
       #SetEnv configuration /path/to/config/file
       ErrorLog ${approot}/.error.log
       CustomLog ${approot}/.access.log combined
    </VirtualHost>
    </Macro>


Use WSGISite karatbars.iwantyoutoprosper.com /home/schemelab/domains/com/iwantyoutoprosper/karatbars myapp.wsgi


## Adding a new affiliate page

Create a folder for it (e.g. `lookout`)

Put the static files in img, js, css, etc.

Add the folder to the `subdirs` value in config.py

Make sure the HTML has an `affiliate_url` value even if it's empty:
    <a meld:id="affiliate_url"></a>

All pages have to have it - it goes directly to the Karatbars sign-up form.

Add a routing for the folder in `myapp.py` in the `Root` class.

Edit tools/new-user-welcome.rst and add a link to the new page.
Edit trainwith/index.html and add a link to the new page in the affiliate/internet-style marketing section.

## Send an email

# Testing

Tools page