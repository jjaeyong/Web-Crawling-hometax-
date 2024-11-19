import pandas as pd
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))


df = pd.read_csv("/Users/eomjaeyong/Desktop/창윤이 크롤링/tmp_data.csv")


df = df[:5] # 이건 없어도 됨 길어져서 테스트 하느라고 줄임.

# mf_txppWframe_bsno 번호 입력 칸 Id
# mf_txppWframe_trigger5 조회하기 입력버튼 id
# mf_txppWframe_grid2_cell_0_1 휴폐업 자료

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install())) 

url = "https://hometax.go.kr/websquare/websquare.html?w2xPath=/ui/pp/index_pp.xml&tmIdx=43&tm2lIdx=4306000000&tm3lIdx=4306080000"


driver.get(url)
time.sleep(3)

result_list = [] 
for reg_no in df['가맹점 번호'] : 
    driver.find_element(By.ID, 'mf_txppWframe_bsno').send_keys(reg_no) # 가맹점 번호 입력칸 
    driver.find_element(By.ID, 'mf_txppWframe_trigger5').click() # 확인 버튼
    time.sleep(2) 
    result = driver.find_element(By.ID, "mf_txppWframe_grid2_cell_0_1").text # 결과값 리턴
    print(result)
    rst = None
    if '폐업자' in result:
        rst = '폐업/' + result.split("폐업일자:")[1].split(")")[0] 
    elif '일반과세자' in result:
        rst = '일반'
    else: 
        rst = '미등록'
    result_list.append(rst)
    time.sleep(1)


result_list 

df["결과값"] = result_list 
df

driver.close()
