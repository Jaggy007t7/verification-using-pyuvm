import cocotb
from cocotb.triggers import Timer
@cocotb.test()
async def test(dut): # Argument is compulosry;
    print("output for input :,a,b,c,is (cout,sum):,cout,sum")

    for a in range(2):
        for b in range(2):
            for c in range(2):

                # assigning the ports;
                dut.x.value=a
                dut.y.value=b
                dut.z.value=c

                # Time constraints; means settle time
                await Timer(2,unit="ns")

                # Outputs;
                cout = dut.carry.value
                sum = dut.sum.value

                # Monitor outputs;
                print("output for input :",a,b,c,"is (cout,sum):",cout,sum)


   
    

