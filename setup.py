from setuptools import setup, find_packages


install_requires=[
        "annotated-types==0.7.0",
        "anyio==4.8.0",
        "blinker==1.9.0",
        "certifi==2025.1.31",
        "click==8.1.8",
        "eval_type_backport==0.2.2",
        "exceptiongroup==1.2.2",
        "Flask==3.1.0",
        "flask-mysql-connector==1.1.0",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.1",
        "idna==3.10",
        "itsdangerous==2.2.0",
        "Jinja2==3.1.6",
        "jsonpath-python==1.0.6",
        "MarkupSafe==3.0.2",
        "mistralai==1.5.1",
        "mypy-extensions==1.0.0",
        "mysql-connector-python==9.2.0",
        "numpy==2.2.3",
        "pandas==2.2.3",
        "pydantic==2.10.6",
        "pydantic_core==2.27.2",
        "python-dateutil==2.9.0.post0",
        "python-dotenv==1.0.1",
        "pytz==2025.1",
        "six==1.17.0",
        "sniffio==1.3.1",
        "typing-inspect==0.9.0",
        "typing_extensions==4.12.2",
        "tzdata==2025.1",
        "Werkzeug==3.1.3"
    ]

setup(
    name='summary-service',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    include_package_data=True,
)