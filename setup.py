from setuptools import setup
import versioneer


setup(
    name = "continuous_delivery_with_travis_and_pypi",
    version=versioneer.get_version(),
    author = "Phil Elson",
    author_email = "pelson.pub@gmail.com",
    description = ("An demonstration of how to setup a package which "
                   "automatically uploads itself to pypi upon sucessful "
                   "test completion."),
    license = "BSD",
    keywords = "example documentation continuous delivery",
    url = "https://github.com/pelson/continuous_delivery_pure_python",
    packages=['continuous_delivery_with_travis_and_pypi'],
    install_requires=['numpy'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    cmdclass=versioneer.get_cmdclass(),
)

