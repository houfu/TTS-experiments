from setuptools import setup

setup(
    name='TTS-experiments',
    version='',
    packages=['tts'],
    url='',
    license='MIT',
    author='houfu',
    author_email='houfu@outlook.sg',
    description='Trying out TTS',
    install_requires=['Click', 'TTS', 'google-cloud-texttospeech'],
    entry_points={
        'console_scripts': [
            'my_tts = tts.main:main',
        ],
    },
)
