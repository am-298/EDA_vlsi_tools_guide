from cocotb.triggers import Timer, RisingEdge

async def reset_dut(dut, duration=20):
    dut.reset.value = 1
    await Timer(duration, unit="ns")
    dut.reset.value = 0
    await RisingEdge(dut.clk)
