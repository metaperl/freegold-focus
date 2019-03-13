jquery-flyout
===========

This JQuery Flyout plugin provides Bootstrap Popover-like flyout without pulling all the Bootstrap things in. It is pretty simple, you can use it as either popover or tooltip depending on your scenarios.


Usage
---------

Put `jquery.flyout.js` in your js library, `jquery.flyout.css` in your CSS library and reference them properly in your files. Then you can use the entry API `$().flyout()` to setup your flyouts on trigger elements or issue commands on them.

> **Note**:
> 
> - This plugin only supports Chrome, Firefox and IE9+
> - JQuery version 1.4+ required

Check out the `index.html` to see common use cases.


API
-----

#### `$.fn.flyout(param)`

This is the entry API used to setup the flyout on trigger elements or issue commonds manually.

- `param`: Type `{object|null|string}`
When it is `object` or omitted, this API initializes flyout using provided `param` as options. See Options section for details.
When it is `string`, this API executes predefined commands:
    + show
    + hide
    + toggle
    + destroy

#### `$.fn.flyout.defaults`

Default options that can be overridden by users, see Options section for details.


Options
-----------

- **`animation`**: `{boolean}` indicates if it shows and hides flyouts with fading animation, default is `true`
- **`title`**: `{string|function|null}` title of this flyout, can be text or string returned by function. If the title is empty, the title area will not appear intentionally. `this` refers to the jquery object of element that setups this flyout.
- **`content`**: `{string|function|null}` contents of this flyout, can be html string or string returned by function. `this` refers to the jquery object of element that setups this flyout.
- **`html`**: `{boolean}` indicates if content is HTML string or simple text. When it is `true`, contents will be inserted by using `$.html()`, otherwise `$.text()`, default is `false`.
- **`placement`**: `{string}` where to place the flyout, could be `top`, `right`, `bottom` and `left`, default is `top`.
- **`dismissible`**: `{boolean}` indicates if the flyout is intended to be dismissed when the trigger is out of focus, default is `false`.
- **`trigger`**: `{string}` the way how the showing of flyout is triggered, could be `click` and `manual`. When set to `manual`, to show the flyout, you need to call `$().flyout('show')` explicitly.


License
----------

Copyright (c) 2016 Nobel Huang. Licensed under the MIT license.
