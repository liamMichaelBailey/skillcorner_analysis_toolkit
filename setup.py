from setuptools import setup

setup(
    name='skillcorner_analysis_toolkit',
    version='1.0.0',

    url='https://github.com/liamMichaelBailey/skillcorner_analysis_toolkit',
    author='Liam Michael Bailey',
    author_email='liam.bailey@skillcorner.com',

    packages=['skillcorner_analysis_toolkit'],

    package_data={'': ['Montserrat-VariableFont_wght.ttf']},
    include_package_data=True,
    install_requires=['adjustText==0.7.3',
                      'matplotlib==3.7.0',
                      'numpy==1.24.2',
                      'pandas==1.5.3',
                      'seaborn==0.11.2'],
)