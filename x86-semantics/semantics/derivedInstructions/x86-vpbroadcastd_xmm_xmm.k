// Autogenerated using stratification.
requires "x86-configuration.k"

module VPBROADCASTD-XMM-XMM
  imports X86-CONFIGURATION

  rule <k>
    execinstr (vpbroadcastd R1:Xmm, R2:Xmm,  .Operands) => .
  ...</k>
    <regstate>
RSMap:Map => updateMap(RSMap,
convToRegKeys(R2) |-> (concatenateMInt(mi(128, 0), concatenateMInt(concatenateMInt(extractMInt(getParentValue(R1, RSMap), 224, 256), extractMInt(getParentValue(R1, RSMap), 224, 256)), concatenateMInt(extractMInt(getParentValue(R1, RSMap), 224, 256), extractMInt(getParentValue(R1, RSMap), 224, 256)))) )


)

    </regstate>
endmodule

module VPBROADCASTD-XMM-XMM-SEMANTICS
  imports VPBROADCASTD-XMM-XMM
endmodule
/*
TargetInstr:
vpbroadcastd %xmm2, %xmm1
RWSet:
maybe read:{ %xmm2 }
must read:{ %xmm2 }
maybe write:{ %ymm1 }
must write:{ %ymm1 }
maybe undef:{ }
must undef:{ }
required flags:{ avx2 }

Circuit:
circuit:callq .move_128_064_xmm2_r12_r13  #  1     0    5      OPC=callq_label
circuit:callq .move_064_128_r12_r13_xmm3  #  2     0x5  5      OPC=callq_label
circuit:vbroadcastss %xmm3, %xmm1         #  3     0xa  5      OPC=vbroadcastss_xmm_xmm
BVF:
WARNING: No live out values provided, assuming { }
WARNING: No def in values provided; assuming { %mxcsr::rc[0] }
Target

vpbroadcastd %xmm2, %xmm1

  maybe read:      { %xmm2 }
  must read:       { %xmm2 }
  maybe write:     { %ymm1 }
  must write:      { %ymm1 }
  maybe undef:     { }
  must undef:      { }
  required flags:  { avx2 }

Circuits:

%ymm1  : 0x0₁₂₈ ∘ (%ymm2[31:0] ∘ %ymm2[31:0] ∘ %ymm2[31:0] ∘ %ymm2[31:0])

sigfpe  : sigfpe
sigbus  : sigbus
sigsegv : sigsegv

*/