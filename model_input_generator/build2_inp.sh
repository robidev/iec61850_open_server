#!/bin/sh

mkdir build

find src/ -name "*.java" > listFile.tmp

javac -target 1.7 -source 1.7 -d build @listFile.tmp

jar cfm genconfig_input.jar manifest-dynamic_inp.mf -C build/ com/

rm listFile.tmp
rm -r build
