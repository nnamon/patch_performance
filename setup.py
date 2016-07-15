from distutils.core import setup

setup(
      name='patch_performance',
      version='0.01',
      packages=['patch_performance'],
      install_requires=[i.strip() for i in open('requirements.txt').readlines() if 'git' not in i],
      description='A Component that computes scores of all patched binaries and updates DB with corresponding scores.',
      url='https://git.seclab.cs.ucsb.edu/cgc/patch_performance',
)
