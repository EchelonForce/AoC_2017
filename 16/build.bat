python 16p2_gen_c_code.py input.txt

pushd "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\"
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x86_amd64

popd
cl 16p2.c

pause
