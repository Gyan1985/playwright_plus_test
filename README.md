# playwright_plus
The provided package code utilizes Playwright, a web automation library, to intercept JSON data from web pages. It includes utility functions like json_detect_error to identify errors within the JSON response and json_parse_result to format the JSON data into a standardized response structure. The main functions, such as intercept_json_playwright and intercept_json_playwright_multiple, use Playwright to intercept JSON responses, handle errors, and parse the data. These functions offer flexibility by allowing users to provide custom error detection and parsing logic. Additionally, there's a function request_json_playwright that simplifies the process by internally utilizing intercept_json_playwright. These functions facilitate seamless interaction with web APIs, providing a structured approach to handling JSON data retrieval and potential errors during the process.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Playwright plus ppt](playwright_plus.pdf)

## Prerequisites 
* python >= 3.10
* pip3

## Getting Started

Please follow the instructions for run the test case for the code

1. Create a virtual environment. If you don't have virtualenv installed, you can download it with the command:
    ```
    pip install virtualenv
    
    ```
2. Create a virtual environment with the following command:
    ```
    virtualenv <virtual environment name>
    ```

3. Take clone of the repository using the following command:

   ```
   git clone https://github.com/
   ```

4. Activate the virtual environment using the command:

    ```
    source <virtual environment name>/bin/activate
    ```


5. Install the app dependencies by running:
    ```
    pip install -r requirements.txt
   ```

6. Run the setup.py by following the command:

   ```
   python setup.py install
   ```

7. Install the playwright install by following the command:
   ```
   playwright install
   ```

8. Then go to the directory where test.py file is there

    ```
    cd playwright_plus
    ```
   
9. Run the python file test.py by following command

    ```
    python test.py
    ```
