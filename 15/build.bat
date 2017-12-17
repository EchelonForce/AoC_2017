pushd "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\"
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x86_amd64

popd
cl 15p1.c

pause
