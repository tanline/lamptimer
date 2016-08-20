from setuptools import setup

setup(name='lamptimer',
      version='0.1',
      author='Tanpreet Grewal',
      author_email='tanpreet@tanpreet.com',
      license='MIT',
      packages=['lamptimer'],
      install_requires=[
          'Astral',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False)
