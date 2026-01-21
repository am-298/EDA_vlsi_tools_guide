import cocotb 
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()

async def test_adder (dut):
    for i in range (4):
        for j in range (4):
            dut.a.value = i
            dut.b.value = j
            await Timer(1,units="ns")
            expected = a + b
            assert dut.out.value == expected , f"a={a} , b={b}, out={dut.out.value}, expected={expected}"
            cocotb.log.info("All the 2 bit combination passed")


