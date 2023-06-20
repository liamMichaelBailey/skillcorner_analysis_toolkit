from setuptools import setup, find_packages

setup(
    name='skillcorner_analysis_toolkit',
    version='1.0.0',

    url='https://github.com/liamMichaelBailey/skillcorner_analysis_toolkit',
    author='Liam Michael Bailey',
    author_email='liam.bailey@skillcorner.com',

    packages=find_packages(include=['skillcorner_analysis_toolkit', 'skillcorner_analysis_toolkit.*']),

    package_data={'skillcorner_analysis_toolkit': ['resources/Roboto/Roboto-Black.ttf',
                                                   'resources/Roboto/Roboto-BlackItalic.ttf',
                                                   'resources/Roboto/Roboto-Bold.ttf',
                                                   'resources/Roboto/Roboto-BoldItalic.ttf',
                                                   'resources/Roboto/Roboto-Italic.ttf',
                                                   'resources/Roboto/Roboto-Light.ttf',
                                                   'resources/Roboto/Roboto-LightItalic.ttf',
                                                   'resources/Roboto/Roboto-Medium.ttf',
                                                   'resources/Roboto/Roboto-MediumItalic.ttf',
                                                   'resources/Roboto/Roboto-Regular.ttf',
                                                   'resources/Roboto/Roboto-Thin.ttf',
                                                   'resources/Roboto/Roboto-ThinItalic.ttf']},

include_package_data=True,
    install_requires=['adjustText==0.7.3',
                      'matplotlib==3.7.0',
                      'numpy==1.24.2',
                      'pandas==1.5.3',
                      'seaborn==0.11.2'],
)
