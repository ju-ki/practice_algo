import os
import requests
import json
import re
import html
import subprocess
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 過去にサブミットしたファイルのダウンロード
if __name__ == "__main__":
    userID = "jukiya"
    unix_second = 0
    api_path = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={userID}&from_second={str(unix_second)}"

    def getSubmissionData(userID):
        api_url = api_path
        response = requests.get(api_url)
        jsonData = response.json()
        return jsonData

    submissions = getSubmissionData(userID)

    def getNewestSubmits(submissions):
        sortedData = sorted(submissions, key=lambda x: x["id"])
        submits = {}
        for data in sortedData:
            if data["result"] != "AC":
                continue
            submits[data["problem_id"]] = data

        result = {}
        for sub in submits.values():
            if not sub["contest_id"] in result:
                result[sub["contest_id"]] = []
            result[sub["contest_id"]].append(sub)
        return result

    submissions = getNewestSubmits(submissions)

    root = "./"
    paths = []
    contest_names = []

    def fetchContestName(submissions):
        for idx, contestName in enumerate(submissions):
            contest_names.append(contestName)
            paths.append(root + contestName)
            os.makedirs(paths[idx], exist_ok=True)

    fetchContestName(submissions)


    def fetchContestCode(submissions):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        for idx, submits in enumerate(submissions.values()):
            for sub in submits:
                path = paths[idx]
                contest_name = contest_names[idx]
                problem_num = sub["problem_id"]
                if problem_num.isdigit():
                    problem_num = chr(int(problem_num) + ord('a') - 1)
                    path = root + sub["contest_id"] + "/" + problem_num

                if "Python" in sub["language"]:
                    path += "/" + problem_num + ".py"
                elif "C++" in sub["language"]:
                    continue
                if os.path.isfile(path):
                    continue
                sub_url = "https://atcoder.jp/contests/" + sub["contest_id"] + "/submissions/" + str(sub["id"])
                driver.get(sub_url)

                code = driver.find_element(By.ID, "submission-code")
                inner_html = code.get_attribute("innerHTML")
                list_items = re.findall(r'<li[^>]*>.*?</li>', inner_html)
                lines = []

                for li in list_items:
                    line1 = re.sub(r'<[^>]+>', '', li)
                    line2 = re.sub(r'&nbsp;', '', line1)
                    line3 = html.unescape(line2)
                    lines.append(line3 + "\n")
                code_text = ''.join(lines)

                with open(path, "w") as f:
                    f.write(code_text)
                sleep(4)
        driver.quit()

    fetchContestCode()
