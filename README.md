# API to support some exercises in Elm

This is a simple API created for educational purposes while teaching [Elm](http://elm-lang.org) skills in my [Brazilian Portuguese live coding series](http://cuducos.me/2016/10/24/vamos-aprender-elm.html).

## Install

It was written having [Python](https://python.org) 3.5+ in mind.

Install the dependencies:

```console
$ python -m pip install -r requirements.txt
```

Set `FLASK_APP` environment variable and if you want to run it in debug also set `FLASK_DEBUG` environment variable:

```console
$ export FLASK_APP=api.py
$ export FLASK_DEBUG=1
```

Finally, run the Flask app:

```console
$ flask run
```

## Usage

By default the API starts with three comments and uses a SQLite in memory database (no persistence after server is down or restarted)

### `GET /api/comments`

List all blog comments.

```
HTTP/1.0 200 OK
Content-Type: application/json
```

```json
{
    "comments": [
        {
            "author": "John Doe",
            "content": "Ahoy, cap'n",
            "date": "2016-11-01T19:38:49.883231",
            "id": 1
        },
        {
            "author": "Joane Doe",
            "content": "What be happenin', matey?",
            "date": "2016-11-01T19:38:49.883980",
            "id": 2
        },
        {
            "author": "Buccaneer",
            "content": "What say ye, ya scurvy dog",
            "date": "2016-11-01T19:38:49.884164",
            "id": 3
        }
    ]
}
```

### `POST /api/comments/`

Receives two values: a comment `author` and a comment `content`. Creates a new comment and return it.

```
HTTP/1.0 201 CREATED
Content-Type: application/json
```

```json
{
    "author": "Cuducos",
    "content": "Hey!",
    "date": "2016-11-01T19:41:07.898834",
    "id": 4
}
```

### `GET /api/comment/<comment_id>`

Get the details of the comment with ID `<comment_id>`.

```
HTTP/1.0 200 OK
Content-Type: application/json
```

```json
{
    "author": "John Doe",
    "content": "Ahoy, cap'n",
    "date": "2016-11-01T19:38:49.883231",
    "id": 1
}
```

### `DELETE /api/<comment_id>`

Deletes the comment with ID `<comment_id>`.

```
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
```