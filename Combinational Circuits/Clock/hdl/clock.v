module clock(
    input clk,
    output wire y
);
assign y = clk;

initial begin 
    $dumpfile("clock.vcd");
    $dumpvars(0,clock);
end
endmodule
