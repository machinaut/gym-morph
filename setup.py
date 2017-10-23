from glob import glob
from setuptools import find_packages, setup


setup(name='gym-morph',
      version='0.0.1',
      description='Gym mujoco environments with morphology-control',
      packages=find_packages(),
      author='Alex Ray',
      author_email='a@machinaut.com',
      install_requires=['numpy>=1.13.3',
                        'gym>=0.9.4',
                        'mujoco_py>=1.50.1.23'],
      include_package_data=True)
