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

To generate sources run 
```dcomp/client/qt/generate.sh```

Execute the python program with
```python dcomp/client/qt/generated/dcomp-qt.py```

Results in

```
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.
```
