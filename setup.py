from setuptools import setup

__version__ = '0.6.25'

# Read long description from README.rst file
def load_readme():
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='Docassemble-Flask-User',
    version=__version__,
    url='http://github.com/jhpyle/Flask-User',
    license='BSD License',
    author='Ling Thio, Jonathan Pyle',
    author_email='jhpyle@gmail.com',
    description='Customizable User Authentication and Management, and more.',
    long_description=load_readme(),
    keywords='Flask User Registration Email Username Confirmation Password Reset',

    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: German',
        'Natural Language :: Spanish',
        'Natural Language :: Finnish',
        'Natural Language :: French',
        'Natural Language :: Italian',
        'Natural Language :: Persian',
        'Natural Language :: Russian',
        'Natural Language :: Swedish',
        'Natural Language :: Turkish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages=['docassemble_flask_user'],
    include_package_data=True,    # Tells setup to use MANIFEST.in
    zip_safe=False,    # Do not zip as it will make debugging harder

    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',   # Python 2.6, 2.7, 3.3+
    install_requires=[
        'bcrypt==3.2.0',
        'Flask==1.1.2',
        'Flask-Login==0.5.0',
        'Flask-Mail==0.9.1',
        'Flask-SQLAlchemy==2.4.4',
        'Flask-WTF==0.14.3',
        'passlib==1.7.4',
        'pycryptodome==3.10.1',
    ]
)
