#!/usr/bin/env bash

if [ ! -f "~/.pypirc" ]
then

    cat <<EOF > ~/.pypirc
[server-login]
username: ${PYPI_USERNAME}
password: ${PYPI_PASSWORD}

EOF
fi

