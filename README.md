# Overview
TILUP Backend API 입니다.  
API URL : https://tilup-release-v1.herokuapp.com  
Swagger URL : https://tilup-release-v1.herokuapp.com/swagger

# Features - API Name 
- 회원 여부 체크 - email_check
- 회원가입 - register
- 로그인/로그아웃 - login/logout
- 이메일 찾기 - find_email
- 비밀번호 변경 - password_change
- 학습 사이트 조회 - sites
- 강의 조회 - courses
- 섹션 조회 - sections
- 학습 카드 등록/조회/수정/삭제 - mycourses
- TIL 등록/조회/수정/삭제 - tils
- 학습 카드로 등록된 사이트 목록 조회 - mysites

# Tech Stack
- Language : Python 3.8.10
- Web Framework : Django 3.2.3, Django rest framework 3.2.3
- Database : PostgreSQL
- Docs : Swagger 
- Response : JSend
- Hosting : Heroku

# 개발 환경 및 개발 기간
- OS : MacOS
- IDE : Visual Studio Code 1.55.1
- 개발 기간 : 2021-06-07 ~ 2021-08-07

# DB ERD
![DB_visualized](https://user-images.githubusercontent.com/80886445/128706854-82cc8b05-ff52-4cbb-abe3-5429fb534a77.png)


# 실행 
local : python manage.py runserver --settings=conf.settings.local