import os,sys


BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
sys.path.insert(0,BASE_DIR)

CASE_PATH = os.path.join(BASE_DIR,"test_case\\")
ERROT_PNG_PATH = os.path.join(BASE_DIR,"error_png\\")
REPORT_FILE = os.path.join(BASE_DIR, "Report\\result_xbt.html")
