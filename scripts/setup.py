import setuptools

REQUIRED_PACKAGES = [
    "apache-beam==2.23.0",
    "beam-nuggets",
    "psycopg2-binary"
]

setuptools.setup(
    name='league_of_legends_example',
    version='0.0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
)
