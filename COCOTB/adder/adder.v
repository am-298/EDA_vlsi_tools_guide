module adder (
    input [1:0] a,
    input [1:0] b,
    output [2:0] out
);
assign out = a + b;

endmodule