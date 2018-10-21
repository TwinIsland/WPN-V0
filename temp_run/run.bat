@echo off 
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin 
:: Rattlemander VPN Allocate is under this line

brook client -l 127.0.0.1:8080 -i 127.0.0.1 -s fra1.brookfree.pw:7000 -p DOUBIm43JTQCGPy --http