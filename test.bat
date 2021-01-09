@echo off

python -m robot ^
--outputdir  .robot_results ^
test.robot
echo.

echo  ERROR: %ERRORLEVEL%
