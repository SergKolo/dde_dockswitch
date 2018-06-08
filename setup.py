from setuptools import setup

setup(
    name='dde_dockswitch',
    version='0.1',
    license='MIT',
    description='Indicator for Deepin dock for switching between multiple lists of docked apps',
    author='Sergiy Kolodyazhnyy',
    author_email='1047481448@qq.com',
    url='https://github.com/SergKolo/dde_dockswitch',
    packages=['dde_dockswitch'],
    install_requires=['dbus-python'],
    data_files=[
        ('/usr/share/pixmaps',['dde_dockswitch/dde_dockswitch_icon.png']),
        ('/usr/share/applications',['dde_dockswitch/dde_dockswitch.desktop'])
    ],
    classifiers=[
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.0',
        'Topic :: Utilities'
    ]
)
