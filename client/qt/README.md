# dcomp

Install qt

```
sudo python3.6 -m pip install pyqt5
```

Install qtdesigner with
```
sudo yum install -y qt-creator
```

If you get following error when building in qt-creator see next step
```
toolchain.prf(50): system(execute) requires one or two arguments.
```

Comment out last line - load(toolchain) in following if you get above error
```
sudo vi /usr/lib64/qt5/mkspecs/features/default_pre.prf
```