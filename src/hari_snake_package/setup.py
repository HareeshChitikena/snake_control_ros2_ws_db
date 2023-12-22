from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hari_snake_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*.rviz'))), 
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.*'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.world'))), 
        (os.path.join('share', package_name, 'description', 'urdf'), glob(os.path.join('description','urdf', '*.xacro'))),
        (os.path.join('share', package_name, 'description', 'urdf'), glob(os.path.join('description','urdf', '*.urdf.xacro'))),
        # (os.path.join('share', package_name, 'description', 'xacro'), glob(os.path.join('description','xacro', '*.xacro'))),
        # (os.path.join('share', package_name, 'description', 'meshes', 'a0912_blue'), glob(os.path.join('description','meshes','a0912_blue', '*.dae'))),
        # (os.path.join('share', package_name, 'description', 'meshes', 'm1013_white'), glob(os.path.join('description','meshes','m1013_white', '*.dae'))),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hari22',
    maintainer_email='hari.chitikena@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
