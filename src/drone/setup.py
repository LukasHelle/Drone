from importlib.util import source_from_cache
from collections.abc import Sequence

from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'drone'
models: list[tuple[str, Sequence[str]]] = []

for root, dirs, files in os.walk('drone_models'):
    for file in files:
        source = os.path.join(root, file)
        place = os.path.join('share', package_name, root)

        models.append((place, [source]))
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/drone_launch.py']),
        ('share/' + package_name + '/world_models', ['world_models/world.sdf']),

    ] + models,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lukas',
    maintainer_email='lukashelle04@gmail.com',
    description='TODO: Package description',
    license='MIT License',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
