# Continuous delivery example

An example of implementing continuous delivery with Travis-CI.


Tests: [![Build Status](https://travis-ci.org/pelson/package_with_continuous_delivery.svg?branch=master)](https://travis-ci.org/pelson/package_with_continuous_delivery); Build: [![Build Status](https://travis-ci.org/pelson/package_with_continuous_delivery.svg?branch=_build)](https://travis-ci.org/pelson/package_with_continuous_delivery)



# How it works

The _build branch is the single place where the CI tools do the building. The branch has a submodule of the source which should be built, so triggering a new build is simply a matter of updating the submodule SHA. This could be done manually, or could be automated to be done when the tests are successful, as has been done in this repository.

The same process can be used for building executables on OS X, Linux, and Windows through TravisCI, CircleCI and AppVeyor respectively.


# Versioning

Nowhere in this repository is the version explicitly written. This means that there is no manual step to update the version - instead this is computed from the repository (or source for an sdist) using versioneer, along with an un-released extension to versioneer. See https://github.com/warner/python-versioneer/pull/90 for progress on the automatic versioning.

# Still to do

The _build branch still needs to build for all 3 OSes, but there is a repository which has implemented this for conda distributions in https://github.com/conda-forge/udunits-feedstock.
