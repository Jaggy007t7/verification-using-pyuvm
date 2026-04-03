import cocotb
import random
from cocotb.triggers import Timer
@cocotb.test()

async def clock(dut):
    clk=0
    arr = []
    for i in range(20):
        if(clk==0):
            clk=1
        else:
            clk=0

        # Input ports;
        dut.clk.value = clk

        #Delay;
        await Timer(5,units ="ps")

        # Output ports;
        out = dut.y.value
        arr.append(out)
    
    print("Clock signal with 5ps delay:")
    print(arr)
