@echo off

:: �������Զ����ʼ��ϵͳ��Ŀ
del /f version\temp\update_sc
del /f temp_run\run.bat
del /f temp_run\ss\gui-config.json
taskkill -f -im brook.exe
taskkill -f -im ss.exe


:: Proxy setting ��ǿ�� By Wyatt
rem �����Զ��������
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections" /v DefaultConnectionSettings /t REG_BINARY /d 4600000000 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections" /v SavedLegacySettings /t REG_BINARY /d 4600000000 /f

rem ���ô���
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f

rem ɾ������IP��ַ
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /f


exit