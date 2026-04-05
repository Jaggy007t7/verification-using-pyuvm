module counter (
    input wire clk,      // clock input
    input wire rst_n,    // active-low asynchronous reset
    input wire en,       // count enable
    output reg [3:0] cnt // count output
);
    
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            cnt <= 4'b0000;
        else if (en)
            cnt <= cnt + 1'b1;
    end


    initial begin 
        $dumpfile("counter.vcd");
        $dumpvars(0,counter);
    end

endmodule
