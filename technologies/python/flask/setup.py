# -*- coding: utf-8 -*-

import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="flaskr",
    version="1.0.0",
    url="https://www.dynatrace.com/news/blog/monitoring-flask-applications",
    license="BSD",
    maintainer="Pallets team (see http://flask.pocoo.org/docs/tutorial/), Dynatrace",
    maintainer_email="contact@palletsprojects.com",
    description="The basic blog app built in the Flask tutorial instrumented by Dynatrace OneAgent SDK.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask","oneagent-sdk~=1.2","requests"],
    extras_require={"test": ["pytest", "coverage"]},
)
