module and_ff (
    input clk,
    input reset,
    input a,
    input b,
    output reg y
);
always @(posedge clk or posedge reset) begin
    if (reset)
        y <= 0;
    else
        y <= a & b;
end
endmodule
