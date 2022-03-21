#!/usr/bin/env bash

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

