# Continuous delivery example

An example of implementing continuous delivery with Travis-CI.



# How it works

The _build branch is the single place where the CI tools do the building. The branch has a submodule of the source which should be built, so triggering a new build is simply a matter of updating the submodule SHA. This could be done manually, or could be automated to be done when the tests are successful, as has been done in this repository.

