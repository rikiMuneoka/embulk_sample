# embulk_sample

## What is this

sample for embulk.
if you want to detail, plz read Makefile.

## How to use

### 1. prepare credential files

At first, you make the dotfile for mysql connect infomation.

```.env
MSYQL_HOST_NAME=[your mysql host name.(if you using local, write localhost)]
MSYQL_USER=[your mysql user name]
MSYQL_PASSWORD=[your msyql user password]
```

Next, you have to put google cloud project credential json file to under directory.

`credentials/`

### 2. export .env

```bash
$ export (cat .env)
```

### 3. setup

```bash
$ make setup
```

### 4. preview

```bash
$ make preview
```

### 5. preview

```bash
$ make run
```
