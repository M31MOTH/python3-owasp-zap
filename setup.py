#!/usr/bin/env python
"""
Standard build script.
"""

__docformat__ = 'restructuredtext'


try:
    from setuptools import setup, find_packages
except ImportError:
    print("You must have setuptools installed to use setup.py. Exiting...")
    raise SystemExit(1)


install_dependencies = (
    'requests'
)
test_requirements = (
    'mock',
    'pylama',
    'pytest',
    'requests_mock'
)
setup(
    name="python3-owasp-zap",
    version="0.0.9",
    description="OWASP ZAP 2.6 API client (python3)",
    long_description="OWASP Zed Attack Proxy 2.6 API python3 client",
    author="ZAP development team (ported to Python3 by Fabian Martinez Portantier)",
    author_email='',
    url="https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project",
    download_url="https://github.com/portantier/zap-api-python3",
    platforms=['any'],

    license="ASL2.0",

    package_dir={
        '': 'src',
    },
    packages=find_packages('src'),

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3'],
    install_requires=install_dependencies,
    tests_require=test_requirements,
    extras_require={'tests': test_requirements}
)
