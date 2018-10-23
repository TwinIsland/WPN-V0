@echo off

:: 在这里自定义初始化系统项目
del /f version\temp\update_sc
del /f temp_run\run.bat
del /f temp_run\ss\gui-config.json
taskkill -f -im brook.exe
taskkill -f -im ss.exe


:: Proxy setting 加强版 By Wyatt
rem 禁用自动检测设置
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections" /v DefaultConnectionSettings /t REG_BINARY /d 4600000000 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections" /v SavedLegacySettings /t REG_BINARY /d 4600000000 /f

rem 禁用代理
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f

rem 删除代理IP地址
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /f


exit