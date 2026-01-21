from cocotb.triggers import RisingEdge, Timer
from clock import start_clock
from reset import reset_dut

@cocotb.test()
async def test_and_gate(dut):

    # Start clock
    cocotb.start_soon(start_clock(dut))

    # Apply reset
    await reset_dut(dut)

    # Small delay to move away from clock edge
    await Timer(1, unit="ns")

    # ---- Test 1: 0 & 0 ----
    dut.a.value = 0
    dut.b.value = 0
    await RisingEdge(dut.clk)   # capture happens here
    await Timer(1, unit="ns")   # allow output to settle
    assert dut.y.value == 0, "AND failed for 0 & 0"

    # ---- Test 2: 1 & 0 ----
    dut.a.value = 1
    dut.b.value = 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert dut.y.value == 0, "AND failed for 1 & 0"

    # ---- Test 3: 1 & 1 ----
    dut.a.value = 1
    dut.b.value = 1
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert dut.y.value == 1, "AND failed for 1 & 1"

                                         