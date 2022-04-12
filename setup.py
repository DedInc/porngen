import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='porngen',
    version='1.0.0',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='Porn content search module.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/porngen',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/porngen/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=['porngen'],
    include_package_data = True,
    install_requires = ['requests', 'requests_html', 'lxml'],
    python_requires='>=3.6',
)