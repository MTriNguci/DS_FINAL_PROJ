# DS_FINAL_PROJ
Final project of Introdution to Data Science

## Table of Contents

 - [Information](#information)
 - [Introduction](#introduction)
 - [Project Plan](#project-plan)
 - [Structure](#structure)
 - [Environment](#environment)
 - [Usage](#usage)

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

[Google Docs - Plan Document](https://docs.google.com/document/d/1-DmU7-sRuqkwM8OxN_qgs3zILV9BRisZw_LR21Io6Xw)

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
