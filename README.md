[![Build Status](https://travis-ci.com/eHealthAfrica/ckanext-biskit.svg?branch=master)](https://travis-ci.com/eHealthAfrica/ckanext-biskit)
[![Coverage Status](https://coveralls.io/repos//ckanext-biskit/badge.svg?branch=master)](https://coveralls.io/r//ckanext-biskit?branch=master)

# ckanext-biskit

This is the main repo for the BISKIT Data Portal. All of the CKAN customizations
are added in this extension.

## Getting Started

### Requirements

This extension works with CKAN 2.8.x.

### Installation

To install ckanext-biskit:

1. Activate your CKAN virtual environment, for example:

    ```sh
    . /usr/lib/ckan/default/bin/activate
    ```

1. Install the ckanext-biskit Python package into your virtual environment:

    ```sh
    pip install ckanext-biskit
    ```

1. Add `biskit` to the `ckan.plugins` setting in your CKAN config file (by default
   the config file is located at `/etc/ckan/default/production.ini`).

1. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

    ```sh
    sudo service apache2 reload
    ```

## Development

### Development Installation

To install ckanext-biskit for development, activate your CKAN virtualenv and do:

```sh
  git clone https://github.com/eHealthAfrica/ckanext-biskit.git
  cd ckanext-biskit
  python setup.py develop
  pip install -r dev-requirements.txt
```

All code MUST follow [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/). Most editors have
plugins or integrations and automatic checking for PEP8 compliance so make sure you use them.

### Running the Tests

To run the tests, do:

```sh
  nosetests --nologcapture --with-pylons=test.ini
```

To run the tests and produce a coverage report, first make sure you have coverage installed in your
virtualenv (``pip install coverage``) then run:

```sh
  nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.biskit --cover-inclusive --cover-erase --cover-tests
```
