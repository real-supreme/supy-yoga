# Supy-Yoga (FlexMoney)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/real-supreme/supy-fwas) [![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/309963727913091073)

# Problem Statement

Assume that you are the CTO for the outsourcing firm which has been chosen to build an
admission form for the Yoga Classes which happen every month.
Requirements for the admission form are:

* Only people within the age limit of 18-65 can enroll for the monthly classes and they will
		be paying the fees on a month on month basis. I.e. an individual will have to pay the fees
		every month and he can pay it any time of the month.

* They can enroll any day but they will have to pay for the entire month. The monthly fee is
		500/- Rs INR.

* There are a total of 4 batches a day namely 6-7AM, 7-8AM, 8-9AM and 5-6PM. The
		participants can choose any batch in a month and can move to any other batch next
		month. I.e. participants can shift from one batch to another in different months but in
		same month they need to be in same batch

![Untitled design](https://user-images.githubusercontent.com/70822569/207696607-7b9da683-04c0-4a73-b1e1-7090133c5886.png)

This is a Web application built using Django Framework with the capability, and possibly even scalable to a larger crowd with some tweaks and changes!

# Table of Contents

1. [Problem Statement](#problem-statement) 📦
2. [Implementation](#implementation) 🧾
	* [Usage](#how-to-run-it) ➕
	* [Requirements](#requirements) ⚙
3. [ER Diagram](#er-diagram--database) 📚
4. [Assumptions](#assumptions) ❗
5 [Scalability Idea](#What-could-be-different) 💡
6. [License](#license) &copy;

<p style="text-align: right;">
	<a href="#supy-yoga-flexmoney">Top</a>
</p>

## Implementation

Supy-Yoga uses both Synchronous and Asynchronous methods, with reliable efficiency and security features. Django itself, provides a Robust and Safe-to-use Secure Connectivity. See [Examples](#examples) after [Installation](#installation)

### How to run it

Either download the file zip or use the command line to download the repository
```
git clone https://github.com/real-supreme/supy-fwas.git

python -m pip install -r requirements.txt

cd %FOLDER%

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
``` 

### Requirements

- Python 3.7+ [(Preferably 3.9.x)](https://www.python.org/downloads/release/python-390/)
	- django
	- django-crispy-forms
- whitenose
  
 <p style="text-align: right;">
	<a href="#table-of-contents">Top</a>
</p>

## ER Diagram & Database

![flexmoney_ER](https://user-images.githubusercontent.com/70822569/207992263-e9e19dc2-252b-4e6f-a13b-1892976db0e6.png)

Database used could be: `postgresql` which allows 120 simultaneous connections at once. Asynchronous Databases cold also be used.
<p style="text-align: right;">
	<a href="#table-of-contents">Top</a>
</p>

## Assumptions

- There user must login to be able to enroll to a Yoga Batch
- Regstration to the website is free
- Enrollment fees is processed successfully without needing to actually implement a payment gateway
<p style="text-align: right;">
	<a href="#table-of-contents">Top</a>
</p>

## What could be different?

- Could add caching systems
- Could add asynchronous capabilities
- Using Connection pooling for faster database transanctions

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 

Copyright (c) 2022-present real-supreme

Live Server: https://supy.pythonanywhere.com/
<p style="text-align: right;">
	<a href="#table-of-contents">Top</a>
</p>
