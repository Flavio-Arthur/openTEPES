
import os
# from openTEPES.openTEPES import openTEPES_run
# import openTEPES.openTEPES as oT
import openTEPES.openTEPES as oT
# import openTEPES

CWD = os.getcwd()
TEST_PATH = CWD + '/openTEPES'
os.chdir(TEST_PATH)

CASE = "9n"
DIR='/Users/flavioalferreira/opt/anaconda3/lib/python3.9/site-packages/openTEPES'
SOLVER = "gurobi"
LOG='No'
RESULT='No'

oT.openTEPES_run(DIR, CASE, SOLVER)
