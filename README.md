# DS_FINAL_PROJ
Final project of Introdution to Data Science

## Table of Contents

 - [Information](#information)
 - [Introduction](#introduction)
 - [Project Plan](#project-plan)
 - [Structure](#structure)
 - [Environment](#environment)
 - [Usage](#usage)
 - [References](#references)

## Information

| Student ID | Name                   | Class                                | 
|------------|------------------------|--------------------------------------|
| 21120496   | Chu Hải Linh           | Introduction to Data Science - 21_21 |
| 21120570   | Đặng Nguyễn Thanh Tín  | Introduction to Data Science - 21_21 |
| 21120574   | Nguyễn Minh Trí        | Introduction to Data Science - 21_21 |
| 21120580   | Trần Thị Kim Trinh     | Introduction to Data Science - 21_21 |

## Introduction

- This is the Final Project of class **Introduction to Data Science - 21_21** (2023).

- Our project focuses on analyzing raw data related to the buying and selling of used cars on the carvago website. We aim to gain a deeper understanding of various factors such as pricing, customer preferences, and the condition of the cars through this analysis. Our main objective is to explore and interpret the data to identify any patterns or trends that may exist. By doing so, we hope to enhance our understanding of the carvago marketplace and contribute valuable insights to the field of used car sales.

- Data for the project is taken from [website carvago](https://carvago.com), the data is completely free to access.

## Project Plan

[Microsoft Word - Plan Document](https://studenthcmusedu-my.sharepoint.com/:w:/g/personal/21120574_student_hcmus_edu_vn/EUnRDvsk3rBJvzrS_zXXS5oB7yOvpTpfc2-1wlGLOT5EUQ?e=ouEwAQ&fbclid=IwAR2sAQmuRQFbJJjkDSVjgrI6e0bBOiV1Mrl6m59BDUijFu3uX6zhUuldO3E)

## Structure

```
📦DS_FINAL_PROJ
├──📜1. Overview & CrawlData.ipynb
├──📜2. Preprocessing.ipynb
├──📜3. Eda.ipynb
├──📜4. Building_Model.ipynb
├──📦data
│   ├──📜cleaned_data.csv
│   ├──📜cleaned_data_edited.csv
│   ├──📜crawl_data.csv
│   ├──📜link1.txt
│   ├──📜link2.txt
│   └──📜testlinks.txt
├──📦deploy
│   ├──📜app.py
│   ├──📜model.pkl
│   ├──📜process.py
│   ├──📦_pycache_
│   │   └──📜process.cpython-310.pyc
│   ├──📦static
│   │   └──📜style.css
│   └──📦templates
│       └──📜form.html
└──📜README.md
```

## Environment

| Name            |     Version   |
|-----------------|---------------|
| python          |     3.10.8    |
| requests        |     2.28.1    |
| requests-cache  |     1.1.0     |
| beautifulsoup4  |     4.11.1    |
| matplotlib      |     3.7.1     |
| numpy           |     1.24.1    |
| pandas          |     1.5.3     |
| scikit-learn    |     1.2.2     |
| seaborn         |     0.13.0    |
| selenium        |     4.14.0    |
| openpyxl        |     3.1.2     |
| notebook        |     7.0.6     |
| plotly          |     5.18.0    |
| flask           |     3.0.0     |

## Usage

1. Clone repository to your device

```
  git clone https://github.com/MTriNguci/DS_FINAL_PROJ.git
```
2. Open Jupyter Notebook (Anaconda/Miniconda/...)

3. Open files .ipynb in the folder

- How to deploy our model:

1. Install the necessary libraries for the operating environment: sklearn, joblib, flask,...

2. Navigate to the "deploy" directory:
   - In the terminal, use the `cd` command to go to the "deploy" directory where your project files are located.

3. Run the "app.py" script:
   - In the terminal, execute the following command to run the "app.py" script:
     ```shell
     python app.py
     ```
## References
Online:
1. Link: [One Hot Encoding in Machine Learning](https://www.geeksforgeeks.org/ml-one-hot-encoding-of-datasets-in-python/)
2. Link: [Chia Training Set và Testing Set với Python](https://tek4.vn/khoa-hoc/machine-learning-co-ban/chia-training-set-va-testing-set-voi-python)
3. Link: [Cross-Validation](https://www.kaggle.com/code/alexisbcook/cross-validation?fbclid=IwAR1E3E5YGQa8yK6HEwi2gic8yD6xpv9GiC2Zq4qkbsdau81juvn5t5lyumY)
4. Link: [Deep AI Khanhblog](https://phamdinhkhanh.github.io/deepai-book/intro.html)
 
