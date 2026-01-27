1. Get the latest copy of Odoo from Nightly Build.
2. Run the application. Example:  
```
odoo_18.0.latest.exe 
```
3. Select the language "English", then click OK.
4. Click "Next" to continue.
5. Click "I Agree"
6. If you  have existing PostgreSQL installed in your system, stop this installation (proceed to Existing PSQL below). 
   If not, continue this step:
	1. Select the type of Install "Odoo Server and PostreSql". Make sure the Odoo Server and PostgreSQL Database are checked.
	2. Click "Next".
	3. Configure PostgreSQL connection. 
```
Hostname: localhost
Port: 5432
Username: openpg
Password: openpgpwd
```
	Note: You can change the username and password of psql connection. Make sure these credentials have the same with value in odoo.conf.
	4. Click "Next".
	5. Browse destination folder, click "Browse". 
	6. Make a new folder inside your chosen folder, Ex. Documents > "Your_Folder".
	7. Click Install.
	8. Installation is now complete. Click "Next".
	9. Uncheck Start Odoo, then click Finish.


Change Odoo service

1. Go to Services, press Win + R then enter services.msc
2. Find Odoo 14.x.x, then right-click and select Properties
3. Click Stop and then change to "Manual"
4. Click OK
5. Find Postgres_For_Odoo in Services then restart

1. Download VS Code Source: https://code.visualstudio.com/download.
2. Configure VS Code
   
   Install the VS Code and open the application.
3. Go to Extensions, install Python (IntelliSense Pylance).
4. Press Ctrl + Shift + P, search "Python: Select Interpreter" and click Python 3.10.x. If the option not available, press F1 and select "Developer: Reload Window"
5. Go to File tab > Open Folder.
6. Select your folder (Install Odoo Step 6.6) > server then click Open.
7. Modify odoo.conf (comment out the logfile)
	1. add the path of custom_addons in the addons_path
	2. set admin_passwd = 1
	3. comment out the logfile
	4. click Save
8. Go to Run tab > click "Add Configuration"
9. Modify launch.json
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Odoo 18 Debug",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/odoo-bin",
            "console": "integratedTerminal",
            "python": "C:\\Users\\Administrator\\Documents\\odoo18\\python\\python.exe",
            "args": [
                "--config=${workspaceFolder}/odoo.conf",
                "--dev=all"
            ],
            "justMyCode": false
        }
    ]
}
```
10. Go to Run tab, click Run without Debugging



Existing PSQL

Option 1
1. If you have existing PostgreSQL, you need to uninstall it in Control Panel
2. Remove directory after uninstall inside C:\Program Files\PostgreSQL
3. Go to Registry Editor, press Win + R then enter "regedit" (make sure you have the Administrator role)
4. Go to search bar, enter HKLM 
5. Select SOFTWARE then find the PostgreSQL, right-click then delete
6. Open CMD then type sc delete "PostresSQL_For_Odoo" and enter
7. Restart PC
8. Proceed to Install Odoo Step 2

Option 2
1. press windows + R
2. type regedit & enter
3. select HK-Key_current_user
4. Select software
5. choose postgresql folder and delete
After above step done, you can re-install odoo application