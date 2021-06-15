from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'pathlib',
    'pandas'
]

setup(
    name='SpotifyAlbumRater',
    version='1.0',
    description='Application for rating spotify songs',
    author='James Sommerville ,Ethan Coulter',
    author_email='Jsommerville99@gmail.com coltsyy@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)