#!/usr/bin/env bash

if [ "$1" == "" ];
then
  echo Please provide name of the python swagger sdk zip file
  exit 1
fi
git rm -rf python
mkdir python
cd python
unzip $1
pip3 install .
cd ..
git add python

