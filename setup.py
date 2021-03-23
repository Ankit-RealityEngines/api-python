from setuptools import setup
setup(name='abacusai',
      version='0.15.0',
      description='Abacus.AI Python Client Library',
      url='https://github.com/abacusai/api-python',
      author='Abacus.AI',
      author_email='dev@abacus.ai',
      license='MIT',
      packages=['abacusai'],
      install_requires=['packaging', 'requests'],
      zip_safe=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ])
