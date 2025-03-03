# django based web scraper/crawler project
<img src="./images_for_readme/web_page_on_final.png">
<br/>
<br/>

# Package list & Version
<table align="center">
<tr>
<td>
<img src="./images_for_readme/pip_list.png">
</td>
<td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
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
<br/>

# ���� ȭ��


## ������Ʈ ����
```shell
python manage.py runserver
```

<details>
<summary>cmd â �ֿ� ��ɾ��</summary>

- project ���� : `django-admin startproject config`
- app ���� : `django-admin startapp myapp`
- model ���� : `python manage.py makemigrations`
- db�� �ݿ� : `python manage.py migrate`
- superuser ���� : `python manage.py createsuperuser`
</details>
<br>
<br>


# superuser cmd �� administration ������
<p align="center">
<img src="./images_for_readme/make_superuser.png">
<img src="./images_for_readme/show_superuser_page.png">
</p>


# ���� ���� capture
<img src="./images_for_readme/project_default_setting.png">
<img src="./images_for_readme/web_page_on_dev.png">
<br/>
<br/>


# error handling
> &nbsp; (1) adress -> address ���� �� re-migrate
<img src="./images_for_readme/adress_to_address.png">

> &nbsp;(2) POST ��û�� ���ؼ� try-catch �߰� # ���������� url ��û � ���� ���
<img src="./images_for_readme/add_try_catch.png">
<br/>
<br/>



# ref
- <a target="_blank" href="https://www.udemy.com/course/django-course/">Django Masterclass : Build 9 Real World Django Projects</a>
- <a target="_blank" href="https://wikidocs.net/72377">���� �� ��� - ��� ������Ʈ �����ϱ�</a><br/><br/>
- <a target="_blank" href="https://docs.djangoproject.com/en/5.1/ref/databases/#sqlite-notes">Django docs # supports SQLite 3.31.0 and later</a>
- <a target="_blank" href="https://docs.djangoproject.com/en/5.1/topics/db/models/">Django docs # models</a>
- <a target="_blank" href="https://docs.djangoproject.com/en/5.1/topics/migrations/">Django docs # migrations</a><br/><br/>
- <a target="_blank" href="https://chagokx2.tistory.com/49">req POST -> {% csrf_token %}</a>
- <a target="_blank" href="https://docs.python.org/ko/3.13/library/exceptions.html">BaseExecption (python)</a>

