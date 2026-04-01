import cocotb
from cocotb.triggers import Timer 
import random
@cocotb.test()
async def alu(dut):

    # Taking inputs from end user;    This type of input is not allowed in python;
    A = input("Enter input a:")
    B = input("Enter input B:")

    # num1 = random.randint(0,100)
    # num2 = random.randint(0,100)

    num1 = int(A)
    num2 = int(B)

    # port declaration;
    dut.a.value = num1
    dut.b.value = num2

    for i in range(4):
        dut.sel.value = i

        #Delay;
        await Timer(2,units="ps")

        output = dut.result.value
        zero = dut.zero.value
        negative = dut.negative.value
        overflow = dut.overflow.value
        carry = dut.carry.value


        # Display outputs;
        print("Inputs are : a=",num1 ,"b=",num2)
        print("result=",output,"carry=",carry)
        print("flags are zero,negative,overflow",zero,negative,overflow)
        print("----------------------------------------------------")

    
