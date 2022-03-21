#!/usr/bin/env bash

if [ "$1" == "" ];
then
  echo Please provide name of the golang swagger sdk zip file
  exit 1
fi
cp go/go.mod .
git rm -rf go
mkdir go
cd go
unzip $1
mv ../go.mod .
go get -d ./...
go build ./...
cd ..
git add go

