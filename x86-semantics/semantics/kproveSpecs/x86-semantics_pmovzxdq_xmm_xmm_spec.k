module X86-SEMANTICS-SPEC
  imports X86-SEMANTICS

  rule
    <k>
saveRegister(%ymm1, "SPAD1") ~>
splitXmmToR32( %xmm2, %xmm8, %xmm9, %xmm10, %xmm11, 128 ) ~>
combineNTo2N(%xmm8,  %xmm9, %ymm3, 128, 256, 128) ~>
execinstr ( vmovlhps %xmm3, %xmm3, %xmm6 , .Typedoperands ) ~>
execinstr ( movddup %xmm9, %xmm1 , .Typedoperands ) ~>
execinstr ( movss %xmm6, %xmm1 , .Typedoperands ) ~>
restoreRegister("SPAD1", 128, 128, 0, 0,
          0, 128, %ymm1) ~>
execinstr ( nop .Typedoperands ) ~> inforegisters ~> fetch
 => exit_0
    </k>
    <entrypoint> zeroMIntW64 </entrypoint>
    <nextLoc> zeroMIntW64  </nextLoc>
    <memstate>
      <cmem> .Map </cmem>
      <dmem> .Map </dmem>
    </memstate>

    <regstate>
"RIP" |->    (mi(64, 0) => _)
"SPAD1" |->    (mi(256, 0) => _)
"YMM1" |-> (mi(256, ?I1:Int):MInt => _)
"YMM10" |-> (mi(256, 0):MInt => _)
"YMM11" |-> (mi(256, 0):MInt => _)
"YMM2" |-> (mi(256, ?I2:Int):MInt => _)
"YMM3" |-> (mi(256, 0):MInt => _)
"YMM6" |-> (mi(256, 0):MInt => _)
"YMM8" |-> (mi(256, 0):MInt => _)
"YMM9" |-> (mi(256, 0):MInt => _)

    </regstate>
    <regstatequeue> .List => _ </regstatequeue>
endmodule
/*
opcode:pmovzxdq_xmm_xmm
instr:pmovzxdq %xmm2, %xmm1
maybe read:{ %xmm2 }
must read:{ %xmm2 }
maybe write:{ %xmm1 }
must write:{ %xmm1 }
maybe undef:{ }
must undef:{ }
required flags:{ sse4_1 }

circuit:callq .move_128_032_xmm2_xmm8_xmm9_xmm10_xmm11  #  1     0     5      OPC=callq_label
circuit:callq .move_128_256_xmm8_xmm9_ymm3              #  2     0x5   5      OPC=callq_label
circuit:vmovlhps %xmm3, %xmm3, %xmm6                    #  3     0xa   4      OPC=vmovlhps_xmm_xmm_xmm
circuit:movddup %xmm9, %xmm1                            #  4     0xe   5      OPC=movddup_xmm_xmm
circuit:movss %xmm6, %xmm1                              #  5     0x13  4      OPC=movss_xmm_xmm
*/