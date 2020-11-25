from setuptools import setup, find_packages

install_requires = [
      "kafka-python==2.0.*",
      "loguru==0.5.3",
      "psycopg2-binary==2.8.6",
      "pytest==6.1.2",
      "requests==2.25.0"
]

setup(name='lib',
      version='0.0.1',
      packages=find_packages('src'),
      package_dir={"": "src"},
      python_requires=">=3.6",
      install_requires=install_requires
      )
