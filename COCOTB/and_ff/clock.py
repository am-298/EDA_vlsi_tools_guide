from cocotb.clock import Clock

def start_clock(dut, period=10, unit="ns"):
    """
    Starts a clock on dut.clk
    """
    return Clock(dut.clk, period, unit=unit).start()
