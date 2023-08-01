#!/bin/sh

mkdir build

find src/ -name "*.java" > listFile.tmp

javac -target 1.7 -source 1.7 -d build @listFile.tmp

jar cfm gendocker.jar manifest-docker.mf -C build/ com/

rm listFile.tmp
rm -r build
