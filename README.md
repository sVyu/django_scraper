## 📑 django based web scraper/crawler project
<table>
  <tr>
    <td>
      <img src="./images_for_readme/web_page_on_dev.png" height="350px"/>
    </td>
    <td>
      <img src="./images_for_readme/web_page_on_final.png" height="375px"/>
    </td>
  </tr>
</table>
<br/>


## ✍ Package list & Version
<table>
  <tr>
    <td>
      <img src="./images_for_readme/pip_list.png"/>
    </td>
    <td>
      <p align="center">
        <h3 align="center">DJango # 4.2</h3>
        <h3 align="center">requests # 2.32.3</h3>
        <h3 align="center">beautifulsoup4 # 4.13.3</h3>
      <p>
    </td>
  </tr>
</table>
<br/>

## 🚀 프로젝트 실행
```shell
python manage.py runserver
```

<details>
<br/>
<summary>그 외 cmd 주요 명령어들</summary>
<table>
  <tr>
    <td>project 생성</td>
    <td>django-admin startproject config .</td>
  </tr>
  <tr>
    <td>app 생성</td>
    <td>django-admin startapp myapp</td>
  </tr>
  <tr>
    <td>model 수정</td>
    <td>python manage.py makemigrations</td>
  </tr>
  <tr>
    <td>db 반영</td>
    <td>python manage.py migrate</td>
  </tr>
  <tr>
    <td>superuser 생성</td>
    <td>python manage.py createsuperuser</td>
  </tr>
</table>
</details>
<br>

## 👨‍💻 superuser cmd 및 administration 페이지
<table>
  <tr>
    <td>
      <img src="./images_for_readme/make_superuser.png"/>
    </td>
    <td>
      <img src="./images_for_readme/show_superuser_page.png" width="600px"/>
    </td>
  </tr>
</table>
<details>
  <summary>Password</summary>
  　└ superuser
</details>
<br/>

## 🛠 error handling
> [!important]
> adress -> address 오타 수정 및 re-migration  
> <img src="./images_for_readme/adress_to_address.png" width="600px" />

> [!caution]
> POST 요청에 대해서 try-catch 추가 # 비정상적인 url 요청 등에 대한 대비
> <img src="./images_for_readme/add_try_catch.png" width="600px" />
<br/>

## 📚 ref
- <a target="_blank" href="https://www.udemy.com/course/django-course/">Django Masterclass : Build 9 Real World Django Projects</a>
- <a target="_blank" href="https://wikidocs.net/72377">점프 투 장고 - 장고 프로젝트 생성하기</a><br/><br/>
- <a target="_blank" href="https://docs.djangoproject.com/en/5.1/ref/databases/#sqlite-notes">Django docs # supports SQLite 3.31.0 and later</a>
- <a target="_blank" href="https://docs.djangoproject.com/en/5.1/topics/db/models/">Django docs # models</a>
- <a target="_blank" href="https://docs.djangoproject.com/en/5.1/topics/migrations/">Django docs # migrations</a><br/><br/>
- <a target="_blank" href="https://chagokx2.tistory.com/49">req POST -> {% csrf_token %}</a>
- <a target="_blank" href="https://docs.python.org/ko/3.13/library/exceptions.html">BaseExecption (python)</a>

