from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs]

CLASSIFIERS = [
    'Development Status :: 1 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
    name='exrates',
    description='Exchange Rates',
    version='1.0.0',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    python_requires='>=2.7',
    classifiers=CLASSIFIERS,
    entry_points={
        'console_scripts': [
            'exrates = exchange_rates.exchange_rate:ExchangeRate'
        ]
    },
    author="Harsha Madhwani",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
