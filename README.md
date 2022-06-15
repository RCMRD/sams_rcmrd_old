# SERVIR Application Management System (SAMS)

[![Django: 4.x](https://img.shields.io/badge/Django-4.x-blue)](https://www.djangoproject.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![SERVIR: Global](https://img.shields.io/badge/SERVIR-Global-green)](https://servirglobal.net)


```commandline
conda env create -f environment.yml
```

Add a file named data.json in the base directory.  This file will hold a json object containing
the siteID for your application.  The format will be:

```json
{
  "siteID": 3
}
```

Add the site domain to the system in the terminal by entering the shell
```shell
python manage.py shell
```
Run the following in the open shell substituting domain for the correct domain
```python
from django.contrib.sites.models import Site
site = Site()
site.domain = 'samdev.servirglobal.net'
site.name = 'samdev.servirglobal.net'
site.save()
```