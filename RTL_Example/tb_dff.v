module tb_diff();

    reg clk;
    reg D;
    reg reset;
    wire Q;


    initial begin
        clk = 0;
        forever #5 clk = ~clk; // 10ns clock period
    end

   
    DFF uut (
        .D(D),
        .clk(clk),
        .reset(reset),
        .Q(Q)
    );


    initial begin
        $monitor("Time %0t | reset=%b | D=%b | Q=%b", $time, reset, D, Q);
    end


    initial begin
        $dumpfile("tb_diff.vcd");   // Output VCD file
        $dumpvars(0, tb_diff); // Dump all signals in this module and instantiated modules
        reset = 1;
        D = 0;

        repeat(10) begin
               @(posedge clk) ;
                reset = $random%2;
                D = $random % 2;
        end

        #100 $finish;  // End simulation
    end

endmodule
