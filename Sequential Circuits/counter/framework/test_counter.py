import cocotb
from cocotb.triggers import Timer
import random
import pandas as pd


def clock(clk):

    if(clk==0):
        clk = 1
    else:
        clk = 0
    return clk

def golden_model(enable,reset,out):
    if not reset:
        return 0
    elif enable:
        return (out + 1)   # 4-bit wrap
    else:
        return out
    

def comparison(out1,out2):
    if(out1==out2):
        print("pass")
    else:
        print("fail")

@cocotb.test()
async def counter(dut):

    #initial values:
    clk = 1
    out =0

    for i in range(20):
        clk = clock(clk)
        reset = random.randint(0,1)
        enable = random.randint(0,1)

        # reset = 1
        # enable = 1

        #input ports;
        dut.clk.value = clk
        dut.rst_n.value = reset
        dut.en.value = enable

        # golden_model(enable,reset,out)
        # print(out)

        #timing
        await Timer(5,unit="ps")
        
        out = golden_model(enable,reset,out)

        #output of design;
        rtl_out = dut.cnt.value

        comparison(out,rtl_out)



