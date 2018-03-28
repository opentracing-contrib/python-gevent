from setuptools import setup

version = open('VERSION').read()
setup(
    name='gevent_opentracing',
    version=version,
    url='https://github.com/opentracing-contrib/python-gevent/',
    download_url='https://github.com/opentracing-contrib/python-gevent/tarball/'+version,
    license='Apache License 2.0',
    author='Carlos Alberto Cortez',
    author_email='calberto.cortez@gmail.com',
    description='OpenTracing support for Gevent applications',
    long_description=open('README.rst').read(),
    packages=['gevent_opentracing'],
    platforms='any',
    install_requires=[
        'gevent',
        'opentracing>=1.1,<1.2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
