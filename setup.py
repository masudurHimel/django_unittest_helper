from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='django_unittest_helper',  # How you named your package folder (MyLib)
    packages=['django_unittest_helper'],  # Chose the same as "name"
    version='0.3',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Helper package for django unittest',  # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Md. Masudur Rahman',  # Type in your name
    author_email='masudurhimel@gmail.com',  # Type in your E-Mail
    url='https://github.com/masudurHimel/django_unittest_helper',  # Provide either the link to your github or to your website
    download_url='https://github.com/masudurHimel/django_unittest_helper/archive/refs/tags/v_03.tar.gz',  # I explain this later on
    keywords=['django', 'unittest'],  # Keywords that define your package best
    install_requires=['Pillow'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
    ],
)

# python setup.py sdist bdist_wheel
# twine upload dist/*