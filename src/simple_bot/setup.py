from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'simple_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # ROS2 패키지 인덱스 등록
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # package.xml 등록
        ('share/' + package_name, ['package.xml']),

        # launch 파일 설치
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),

        # urdf 파일 설치
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='eddy0215@kakao.com',
    description='Simple differential drive robot with camera and ultrasonic sensor',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 나중에 Python 노드를 추가하면 여기에 등록
        ],
    },
)
