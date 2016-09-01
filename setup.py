from setuptools import setup

setup(name='lamptimer',
      version='0.1',
      author='Tanpreet Grewal',
      author_email='tanpreet@tanpreet.com',
      url='https://github.com/tanline/lamptimer',
      license='MIT',
      install_requires=[
          'Astral',
      ],
      packages=[
          'lamptimer',
      ],
      entry_points={
          'console_scripts': [
              'lamptimer=lamptimer.__main__:main',
          ]
      },
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False
)
