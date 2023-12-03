To view, go to [evangriffiths.github.io](https://evangriffiths.github.io/)

## Building

This website uses jinja2 templating. To build the final html, run `make` from the root directory.

```bash
python3 -m venv .venv
pip install -r requirements.txt
make
open build/index.html
```

## Things I've learned along the way

- Web pages are HTML files rendered in a browser.
- HTML is made up of building blocks that can be rendered by the browser, e.g. `<body>...</body>`.
- These building blocks will have some default formatting when rendered (font, size, position, etc.)
- CSS is used to customise this formatting.
- You're quite limited in what you can do in just HTML. e.g. you can't factorize out common parts of a web page, to be used across multiple pages of a website (e.g. a site-wide header and footer).
- One way of doing this is with PHP. In PHP you can write HTML, but also with extra features like templates.
- A web server can interpret PHP files to produce HTML, but your browser can't (and nor can github pages, because it only supports static sites).
- You can either view .php files in you browser by installing php locally and:
  - Starting a local php server, `php -S localhost:port -t your_folder/`
  - Compiling the php into html: `php file.php > file.html`
- An alternative is to use a templating framework like `jinja2`. This has a python API that can be used to compile the html from a templated version that contains jinja directives.

## TODO

Sections on:

- paintings
- videos(?)
- bikeboxparking
- lily with things on her head
- uni thesis
