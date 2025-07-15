"""
什么值得买自动签到脚本
项目地址: https://github.com/SamProjects/smzdm_bot
0 9 * * * smzdm_ql.py
const $ = new Env("2值得买签到");
"""

import os
from pathlib import Path

ql_repo_dir = Path("/ql/data/repo/")
repo_name = "SamProjects_smzdm_bot"
repo_dir = Path(ql_repo_dir, repo_name)


def main():
    os.system(
        f"cd {str(repo_dir)}; pip3 install -qr app/requirements.txt; python3 app/main.py"
    )


if __name__ == "__main__":
    main()
