from setuptools import setup

setup(name='spotonit_sec',
      version='0.1',
      description='spotonit software enginnering challenge',
      url='https://docs.google.com/document/d/1sMMRtG_tIKnp4NsVpnUZFFK7scaMazfGP3n-adMFXvo/edit',
      author='james chang',
      author_email='jamesc@berkeley.edi',
      license='MIT',
      packages=['spotonit_sec'],
      install_requires=[
          'beautifulsoup4',
          'requests',
      ],
      zip_safe=False)