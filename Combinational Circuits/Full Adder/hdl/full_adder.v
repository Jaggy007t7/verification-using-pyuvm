module full_adder(
    input x,y,z,
    output sum,carry
);
assign{carry,sum} = x+y+z;

initial begin 
    $dumpfile("adder.vcd");
    $dumpvars(0,full_adder);
end 
endmodule 
