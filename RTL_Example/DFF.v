// module : D Flip Flop with synchronous reset


`timescale 1ns/1ps

module DFF (input D,
input clk,
input reset,
output reg Q
);

always @(posedge clk)
    begin
        if (reset) 
            begin
                Q<=0;
            end
        else 
                Q<=D;
    end
endmodule
