OpenFaaS Python HTTP Templates
=============================================

The Python HTTP template gives you additional control of the HTTP response for your function and access to the HTTP request details.

## Status of the Template

This template is a work in progress and makes use of the incubator project [of-watchdog](https://github.com/openfaas-incubator/of-watchdog).

## Downloading the Template
```
$ faas template pull https://github.com/kturcios/python-http-template
$ faas new --lang python2.7-http
```

## Event and Context Data
The function handler is passed two arguments, *event* and *context*.

*event* contains the prominent data about the request, including:
- body
- headers
- method
- query
- path

*context* contains basic information about the function, including:
- hostname

## Response Bodies
By default, flask will automatically attempt to set the correct Content-Type header for you based on the type of response. For example, returning a dict object type will automatically attach the header `Content-Type: application/json` and returning a string type will automatically attach the `Content-Type: text/html, charset=utf-8` for you.


## Examples
### Custom Status Codes and Response Bodies
Successful response status code and JSON response body
```python
def handle(event, context):
    return {
        "response": {
            "key": "value"
        },
        "status_code": 200
    }
```
Successful response status code and string response body
```python
def handle(event, context):
    return {
        "response": "Object successfully created",
        "status_code": 201
    }
```
Failure response status code and JSON error message
```python
def handle(event, context):
    return {
        "response": {
            "error": "Bad request"
        },
        "status_code": 400
    }
```
### Custom Response Headers
Setting custom response headers
```python
def handle(event, context):
    return {
        "response": {
            "key": "value"
        },
        "status_code": 200,
        "headers": [
            ("Location", "https://www.example.com/")
        ]
    }
```
### Accessing Event Data
Accessing request body
```python
def handle(event, context):
    return {
        "response": "You said: " + str(event.body),
        "status_code": 200
    }
```
Accessing request method
```python
def handle(event, context):
    if event.method == 'GET':
        return {
            "response": "GET request",
            "status_code": 200
        }
    else:
        return {
            "response": "Method not allowed",
            "status_code": 405
        }
```
Accessing request query string arguments
```python
def handle(event, context):
    return {
        "response": {
            "name": event.query['name']
        },
        "status_code": 200
    }
```
Accessing request headers
```python
def handle(event, context):
    return {
        "response": {
            "content-type-received": event.headers['Content-Type']
        },
        "status_code": 200
    }
```