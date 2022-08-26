#!/usr/bin/env bash
#g++ -std=c++11 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC -I /home/lirh/anaconda3/envs/tensorflow3/lib/python3.6/site-packages/tensorflow/include  -I /usr/local/cuda-8.0/include -lcudart -L /usr/local/cuda-8.0/lib64/ -O2 -D_GLIBCXX_USE_CXX11_ABI=0
#g++ -std=c++11 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC -I /home/lirh/anaconda3/envs/tensorflow3/lib/python2.7/site-packages/tensorflow/include  -I /usr/local/cuda-8.0/include -lcudart -L /usr/local/cuda-8.0/lib64/ -O2 -D_GLIBCXX_USE_CXX11_ABI=0

g++ -std=c++14 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC -I /home/klc/anaconda3/envs/test1/lib/python3.7/site-packages/tensorflow/include  -I /usr/local/cuda-11.7/include -I /home/klc/anaconda3/envs/test1/lib/python3.7/site-packages/tensorflow/include/external/nsync/public -lcudart -L /usr/local/cuda-11.7/lib64/ -L/home/klc/anaconda3/envs/test1/lib/python3.7/site-packages/tensorflow -l:libtensorflow_framework.so.2 -O2 -D_GLIBCXX_USE_CXX11_ABI=0

