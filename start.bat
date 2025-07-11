@echo off
title 启动人员信息管理系统
echo 启动中，请稍候...
python -m uvicorn app.main:app --reload
pause
