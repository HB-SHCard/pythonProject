PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS

cmake \
  -DCMAKE_SYSTEM_PROCESSOR=arm64 \
  -DCMAKE_OSX_ARCHITECTURES=arm64 \
  -DWITH_OPENJPEG=OFF \
  -DWITH_IPP=OFF \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D OPENCV_EXTRA_MODULES_PATH=/Users/hb.shcard/Downloads/opencv_contrib-4.5.2/modules \
  -D PYTHON3_EXECUTABLE=/Applications/Xcode.app/Contents/Developer/usr/bin/python3 \
  -D PYTHON3_INCLUDE_DIR=/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/include/python3.8 \
  -D PYTHON3_LIBRARY=/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/libpython3.8.dylib \
  -D BUILD_opencv_python2=OFF \
  -D BUILD_opencv_python3=ON \
  -D INSTALL_PYTHON_EXAMPLES=ON \
  -D INSTALL_C_EXAMPLES=OFF \
  -D OPENCV_ENABLE_NONFREE=ON \
  -D BUILD_EXAMPLES=ON ..


  -D PYTHON_NUMPY_INCLUDE_DIR=/Users/hb.shcard/PycharmProjects/pythonProject/venv/lib/python3.8/site-packages/numpy/core/include
/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/include/python3.8
  -D PYTHON_LIBRARIES=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/libpython3.8.dylib \
  -D PYTHON3_INCLUDE_DIRS=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/include/python3.8 \
