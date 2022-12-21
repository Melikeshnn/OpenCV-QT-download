#Istediğin opencv sürümünü buraya gir.
OPENCV_VERSION='4.5.5'


#Ubuntu için genel güncelleştirmeleri al
sudo apt-get -y update

#C++ derleyicisini indir
sudo apt install build-essential


#gerekli küthüpaneleri indir
sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev \
                        libopenexr-dev libgdal-dev
                        

sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev \
                        libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm \
                        libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev

                       
sudo apt-get install -y python-dev  python-tk  pylint  python-numpy  \
                        python3-dev python3-tk pylint3 python3-numpy flake8 python3-pyqt5 python3-opencv
       
                        
#Python için qt arayüzü
pip3 install pyqt5

sudo apt install qtcreator



#opencv yükler
wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip
unzip ${OPENCV_VERSION}.zip && rm ${OPENCV_VERSION}.zip
mv opencv-${OPENCV_VERSION} OpenCV


#opencv contriblerini yükler
wget https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip
unzip ${OPENCV_VERSION}.zip && rm ${OPENCV_VERSION}.zip
mv opencv_contrib-${OPENCV_VERSION} opencv_contrib
mv opencv_contrib OpenCV


cd OpenCV && mkdir build && cd build


cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON \
      -DWITH_XINE=ON -DENABLE_PRECOMPILED_HEADERS=OFF \
      -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules ..


make -j8
sudo make install
sudo ldconfig
