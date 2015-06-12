#!/usr/bin/env bash

# Script to change the version scheme depending on the branch we are on.
# NOTICE: running this script with a branch in the form v?N.N.x will result in git assuming
# setup.cfg being unchanged, so that versioneer does not think that the source tree has changed.

# What the maintenance branches look like. Typically it is something like v2.x / 2.x / v2.1.x etc.
MAINT_BRANCH_REGEXP="^v?[0-9]+\.[0-9]*?\.?x$"


if [ -z "$CI" ]
then
   echo "Testing... this isn't on travis-ci!"
   TRAVIS_BRANCH=master
#   TRAVIS_BRANCH=v1.x
fi

if [ "$TRAVIS_BRANCH" == "master" ]; then
   echo "Version set up for master"
elif [[ "$TRAVIS_BRANCH" =~ $MAINT_BRANCH_REGEXP ]]; then
   echo "Setting up version for $TRAVIS_BRANCH"
   # Flick the versioneer style to a standard post form.
   sed -i -- 's|style = pep440-plus-one-dev|style = pep440-post|g' setup.cfg
   git update-index --assume-unchanged setup.cfg
else
   echo "Unknown branch: ${TRAVIS_BRANCH}"
fi

