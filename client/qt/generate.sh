#! /bin/bash

mkdir -p ./generated

pyuic5 -x qtdesigner/dcomp/mainwindow.ui -o generated/dcomp-qt.py
