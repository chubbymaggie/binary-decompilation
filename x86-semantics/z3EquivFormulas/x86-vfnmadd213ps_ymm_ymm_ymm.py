from z3 import *
import proverUtils
# Declarations
CF = BitVec('CF', 1)
PF = BitVec('PF', 1)
AF = BitVec('AF', 1)
ZF = BitVec('ZF', 1)
SF = BitVec('SF', 1)
OF = BitVec('OF', 1)

RAX = BitVec('RAX', 64)
RCX = BitVec('RCX', 64)
ZERO1 = BitVecVal(0, 1)
ONE1 = BitVecVal(1, 1)

cf = (CF == ONE1)
pf = (PF == ONE1)
af = (AF == ONE1)
zf = (ZF == ONE1)
sf = (SF == ONE1)
of = (OF == ONE1)

undef = BitVecVal(0, 1)
cvt_int32_to_single = Function('cvt_int32_to_single', IntSort(), Float32())

# Uninterpreted binary function declaration
add_double = Function('add_double', BitVecSort(64), BitVecSort(64), BitVecSort(64))
add_single = Function('add_single', BitVecSort(32), BitVecSort(32), BitVecSort(32))

sub_double = Function('sub_double', BitVecSort(64), BitVecSort(64), BitVecSort(64))
sub_single = Function('sub_single', BitVecSort(32), BitVecSort(32), BitVecSort(32))

mul_double = Function('mul_double', BitVecSort(64), BitVecSort(64), BitVecSort(64))
mul_single = Function('mul_single', BitVecSort(32), BitVecSort(32), BitVecSort(32))

div_double = Function('div_double', BitVecSort(64), BitVecSort(64), BitVecSort(64))
div_single = Function('div_single', BitVecSort(32), BitVecSort(32), BitVecSort(32))

maxcmp_double = Function('maxcmp_double', BitVecSort(64), BitVecSort(64), BitVecSort(64))
maxcmp_single = Function('maxcmp_single', BitVecSort(32), BitVecSort(32), BitVecSort(32))

mincmp_double = Function('mincmp_double', BitVecSort(64), BitVecSort(64), BitVecSort(64))
mincmp_single = Function('mincmp_single', BitVecSort(32), BitVecSort(32), BitVecSort(32))

# Uninterpreted binary function declaration
approx_reciprocal_double = Function('approx_reciprocal_double', BitVecSort(64), BitVecSort(64))
approx_reciprocal_single = Function('approx_reciprocal_single', BitVecSort(32), BitVecSort(32))

sqrt_double = Function('sqrt_double', BitVecSort(64), BitVecSort(64))
sqrt_single = Function('sqrt_single', BitVecSort(32), BitVecSort(32))

approx_reciprocal_sqrt_double = Function('approx_reciprocal_sqrt_double_double', BitVecSort(64), BitVecSort(64))
approx_reciprocal_sqrt_single = Function('approx_reciprocal_sqrt_double_single', BitVecSort(32), BitVecSort(32))

cvt_single_to_double  = Function('cvt_single_to_double', BitVecSort(32), BitVecSort(64))
cvt_single_to_int32   = Function('cvt_single_to_int32', BitVecSort(32), BitVecSort(32))
cvt_single_to_int64   = Function('cvt_single_to_int64', BitVecSort(32), BitVecSort(64))
cvt_int32_to_single   = Function('cvt_int32_to_single', BitVecSort(32), BitVecSort(32))
cvt_int32_to_double   = Function('cvt_int32_to_double', BitVecSort(32), BitVecSort(64))

# Uninterpreted ternary function declaration
vfmadd132_double = Function('vfmadd132_double', BitVecSort(64), BitVecSort(64), BitVecSort(64), BitVecSort(64))
vfmadd132_single = Function('vfmadd132_single', BitVecSort(32), BitVecSort(32), BitVecSort(32), BitVecSort(32))

vfmsub132_double = Function('vfmsub132_double', BitVecSort(64), BitVecSort(64), BitVecSort(64), BitVecSort(64))
vfmsub132_single = Function('vfmsub132_single', BitVecSort(32), BitVecSort(32), BitVecSort(32), BitVecSort(32))

vfnmadd132_double = Function('vfnmadd132_double', BitVecSort(64), BitVecSort(64), BitVecSort(64), BitVecSort(64))
vfnmadd132_single = Function('vfnmadd132_single', BitVecSort(32), BitVecSort(32), BitVecSort(32), BitVecSort(32))

vfnmsub132_double = Function('vfnmsub132_double', BitVecSort(64), BitVecSort(64), BitVecSort(64), BitVecSort(64))
vfnmsub132_single = Function('vfnmsub132_single', BitVecSort(32), BitVecSort(32), BitVecSort(32), BitVecSort(32))



print('[6;30;44m' + 'Opcode:vfnmadd213ps_ymm_ymm_ymm' + '[0m')

R1 = BitVec('R1', 256)
R2 = BitVec('R2', 256)
R3 = BitVec('R3', 256)

PK_R3 = (Concat( vfnmadd132_single ( Extract( R2.size() - 0 - 1, R2.size() - 32, R2  ) , Extract( R1.size() - 0 - 1, R1.size() - 32, R1  ) , Extract( R3.size() - 0 - 1, R3.size() - 32, R3  )  ) , Concat( vfnmadd132_single ( Extract( R2.size() - 32 - 1, R2.size() - 64, R2  ) , Extract( R1.size() - 32 - 1, R1.size() - 64, R1  ) , Extract( R3.size() - 32 - 1, R3.size() - 64, R3  )  ) , Concat( vfnmadd132_single ( Extract( R2.size() - 64 - 1, R2.size() - 96, R2  ) , Extract( R1.size() - 64 - 1, R1.size() - 96, R1  ) , Extract( R3.size() - 64 - 1, R3.size() - 96, R3  )  ) , Concat( vfnmadd132_single ( Extract( R2.size() - 96 - 1, R2.size() - 128, R2  ) , Extract( R1.size() - 96 - 1, R1.size() - 128, R1  ) , Extract( R3.size() - 96 - 1, R3.size() - 128, R3  )  ) , Concat( vfnmadd132_single ( Extract( R2.size() - 128 - 1, R2.size() - 160, R2  ) , Extract( R1.size() - 128 - 1, R1.size() - 160, R1  ) , Extract( R3.size() - 128 - 1, R3.size() - 160, R3  )  ) , Concat( vfnmadd132_single ( Extract( R2.size() - 160 - 1, R2.size() - 192, R2  ) , Extract( R1.size() - 160 - 1, R1.size() - 192, R1  ) , Extract( R3.size() - 160 - 1, R3.size() - 192, R3  )  ) , Concat( vfnmadd132_single ( Extract( R2.size() - 192 - 1, R2.size() - 224, R2  ) , Extract( R1.size() - 192 - 1, R1.size() - 224, R1  ) , Extract( R3.size() - 192 - 1, R3.size() - 224, R3  )  ) ,  vfnmadd132_single ( Extract( R2.size() - 224 - 1, R2.size() - 256, R2  ) , Extract( R1.size() - 224 - 1, R1.size() - 256, R1  ) , Extract( R3.size() - 224 - 1, R3.size() - 256, R3  )  ) ))))))) )
PS_R3 = (Concat((Concat(( vfnmadd132_single ( (Extract (255, 224, ((R2)))), (Extract (255, 224, ((R1)))), (Extract (255, 224, ((R3)))))), ( vfnmadd132_single ( (Extract (223, 192, ((R2)))), (Extract (223, 192, ((R1)))), (Extract (223, 192, ((R3)))))))), (Concat(( vfnmadd132_single ( (Extract (191, 160, ((R2)))), (Extract (191, 160, ((R1)))), (Extract (191, 160, ((R3)))))), (Concat(( vfnmadd132_single ( (Extract (159, 128, ((R2)))), (Extract (159, 128, ((R1)))), (Extract (159, 128, ((R3)))))), (Concat(( vfnmadd132_single ( (Extract (127, 96, ((R2)))), (Extract (127, 96, ((R1)))), (Extract (127, 96, ((R3)))))), (Concat(( vfnmadd132_single ( (Extract (95, 64, ((R2)))), (Extract (95, 64, ((R1)))), (Extract (95, 64, ((R3)))))), (Concat(( vfnmadd132_single ( (Extract (63, 32, ((R2)))), (Extract (63, 32, ((R1)))), (Extract (63, 32, ((R3)))))), ( vfnmadd132_single ( (Extract (31, 0, ((R2)))), (Extract (31, 0, ((R1)))), (Extract (31, 0, ((R3))))))))))))))))))
proverUtils.prove( PK_R3 == PS_R3 )
