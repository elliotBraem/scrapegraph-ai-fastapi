from fastapi import FastAPI
# 路由
from routers import crawl

import sys
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# 防止相对路径导入出错
sys.path.append(os.path.join(os.path.dirname(__file__)))

app = FastAPI()

# 将其余单独模块进行整合
app.include_router(crawl.router)