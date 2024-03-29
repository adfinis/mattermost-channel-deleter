from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mattermost-channel-deleter",
    version="0.0.1",
    description="Delete Mattermost Channels",
    url="https://github.com/adfinis-sygroup/mattermost-channel-deleter",
    author="Adfinis SyGroup",
    license="AGPL-3.0",
    packages=["mattermost_channel_deleter"],
    install_requires=requirements,
    zip_safe=False,
    entry_points={
        "console_scripts": ["mattermost-channel-deleter=mattermost_channel_deleter.app:main"]
    },
    data_files=[
        ('/usr/lib/systemd/system',[
            'config/mattermost-channel-deleter.service',
            'config/mattermost-channel-deleter.timer'
        ])
    ]
)
