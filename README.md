# Narvan Assignment

This repo provides a web service to do the following:
* Calculating a ​Fibonacci number​ F(n) with the value of n provided by the user.
* The ​Ackermann function​ A(m,n) with values of m and n provided by the user.
* The ​Factorial​ of a non-negative integer n provided by the user.

## Getting Started
Firstly, ``` cd ``` to the project directory.

Make a virtual environment:

```bash
python3 -m venv env
```

Activate the virtual env you created:

```bash
source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Simply start the server by running this command on Terminal:

```bash
./manage.py runserver
```
and you can run the service under [localhost:8000](http://localhost:8000)

## API Endpoints

### `GET /fibonacci/api/`

_Response:_
```json
{
    "detail": "Enter a number"
}
```

### `POST /fibonacci/api/`

_Request(application/json):_
```json
{
    "n": 9
}
```
_Response:_

_200_

```json
{
    "n": 9,
    "result": 34,
    "runtime": "7e-06"
}
```

And if the input is not valid

_405_

```json
{
    "detail": "Input must be an integer."
}
```

### `GET /ackermann/api/`

_Response:_
```json
{
    "detail": "Enter desired numbers"
}
```

### `POST /ackermann/api/`

_Request(application/json):_
```json
{
    "m": 2,
    "n": 4
}
```
_Response:_

_200_

```json
{
    "m": 2,
    "n": 4,
    "result": 11,
    "runtime": "1.8e-05"
}
```

And if the input is not valid

_405_

```json
{
    "detail": "Inputs must be integers."
}
```
As Ackermann Function is a recursive function, the recursion may exceed the limitations in large numbers and a recursion error will happen

_500_

```json
{
    "error": "Sorry, this calculation is beyond limitations!"
}
```

### `GET /factorial/api/`

_Response:_
```json
{
    "detail": "Enter a number"
}
```

### `POST /factorial/api/`

_Request(application/json):_
```json
{
    "n": 6
}
```
_Response:_

_200_

```json
{
    "n": 6,
    "result": 720,
    "runtime": "1.1e-05"
}
```

And if the input is not valid

_405_

```json
{
    "detail": "Input must be an integer."
}
```