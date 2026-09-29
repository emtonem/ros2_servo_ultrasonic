from setuptools import setup

package_name = 'ros2_servo_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'pyserial'],
    zip_safe=True,
    maintainer='Student',
    maintainer_email='student@example.com',
    description='ROS 2 package for ultrasonic sensor and servo control',
    license='MIT',
    entry_points={
        'console_scripts': [
            'bridge_node = ros2_servo_control.bridge_node:main',
            'controller_node = ros2_servo_control.controller_node:main',
        ],
    },
)
