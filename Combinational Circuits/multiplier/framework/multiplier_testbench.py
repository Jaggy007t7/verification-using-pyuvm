import cocotb
from cocotb.triggers import Timer
import random
import pandas
@cocotb.test()

async def multiplier(dut):
    #Defining lists for storing values of input and output;
    input_a = []
    input_b = []
    output_p = []

    cases1 = input("Enter the no. of test cases:")
    cases = int(cases1)
    for i in range(cases):
        num1  = random.randint(0,3)
        num2  = random.randint(0,3)

        #Port classification;
        dut.a.value = num1
        input_a.append(num1)
        dut.b.value = num2
        input_b.append(num2)

        # delay;
        await Timer(5,units="ps")

        # output;
        out = dut.p.value
        output_p.append(out)

        print("multiplication of:",num1,"*",num2,"=",out)
    
    # Creating csv file of input and output;
    df = pandas.DataFrame({"Input_a":input_a,"input_b":input_b,"output":output_p})
    df.to_csv("multiplier.csv",index=False)
