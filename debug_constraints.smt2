; benchmark generated from python API
(set-info :status unknown)
(declare-fun depf_0_0_0 () Int)
(declare-fun depf_0_0_1 () Int)
(declare-fun depf_0_1_0 () Int)
(declare-fun depf_0_1_1 () Int)
(declare-fun x_0_1 () Bool)
(declare-fun x_0_0 () Bool)
(declare-fun depv_1_0_0 () Int)
(declare-fun depv_1_0_1 () Int)
(declare-fun depf_1_0_0 () Int)
(declare-fun depf_1_0_1 () Int)
(declare-fun depv_1_1_0 () Int)
(declare-fun depv_1_1_1 () Int)
(declare-fun depf_1_1_0 () Int)
(declare-fun depf_1_1_1 () Int)
(declare-fun x_1_1 () Bool)
(declare-fun x_1_0 () Bool)
(declare-fun depv_2_0_0 () Int)
(declare-fun depv_2_0_1 () Int)
(declare-fun depf_2_0_0 () Int)
(declare-fun depf_2_0_1 () Int)
(declare-fun depv_2_1_0 () Int)
(declare-fun depv_2_1_1 () Int)
(declare-fun depf_2_1_0 () Int)
(declare-fun depf_2_1_1 () Int)
(declare-fun x_2_1 () Bool)
(declare-fun x_2_0 () Bool)
(declare-fun var_0_0_0 () Int)
(declare-fun var_0_1_0 () Int)
(declare-fun var_1_0_0 () Int)
(declare-fun var_1_1_0 () Int)
(declare-fun var_2_0_0 () Int)
(declare-fun var_2_1_0 () Int)
(declare-fun depmv_0_0 () Int)
(declare-fun depmv_0_1 () Int)
(declare-fun depmf_0_0 () Int)
(declare-fun depmf_0_1 () Int)
(declare-fun depmv_1_0 () Int)
(declare-fun depmv_1_1 () Int)
(declare-fun depmf_1_0 () Int)
(declare-fun depmf_1_1 () Int)
(declare-fun cuenta_0_0 () Bool)
(declare-fun cuenta_0_1 () Bool)
(declare-fun cuenta_1_0 () Bool)
(declare-fun cuenta_1_1 () Bool)
(declare-fun cuenta_2_0 () Bool)
(declare-fun cuenta_2_1 () Bool)
(assert
 (>= depf_0_0_0 0))
(assert
 (<= depf_0_0_0 2))
(assert
 (>= depf_0_0_1 0))
(assert
 (<= depf_0_0_1 2))
(assert
 (let ((?x38 (* depf_0_0_1 1)))
 (let ((?x33 (* depf_0_0_0 2)))
 (let ((?x39 (+ ?x33 ?x38)))
 (<= ?x39 2)))))
(assert
 (or (> (+ depf_0_0_0 depf_0_0_1) 1) false))
(assert
 (>= depf_0_1_0 0))
(assert
 (<= depf_0_1_0 2))
(assert
 (>= depf_0_1_1 0))
(assert
 (<= depf_0_1_1 2))
(assert
 (let ((?x56 (* depf_0_1_1 1)))
 (let ((?x52 (* depf_0_1_0 2)))
 (let ((?x57 (+ ?x52 ?x56)))
 (<= ?x57 2)))))
(assert
 (or (> (+ depf_0_1_0 depf_0_1_1) 1) false))
(assert
 (let ((?x70 (ite (and (distinct depf_0_0_1 depf_0_1_1) true) 1 0)))
 (let ((?x68 (ite (and (distinct depf_0_0_0 depf_0_1_0) true) 1 0)))
 (let (($x71 (and x_0_0 x_0_1)))
 (=> $x71 (> (+ ?x68 ?x70) 0))))))
(assert
 (let ((?x89 (ite (and (distinct depf_0_1_1 depf_0_0_1) true) 1 0)))
 (let ((?x87 (ite (and (distinct depf_0_1_0 depf_0_0_0) true) 1 0)))
 (let (($x90 (and x_0_1 x_0_0)))
 (=> $x90 (> (+ ?x87 ?x89) 0))))))
(assert
 (>= depv_1_0_0 0))
(assert
 (<= depv_1_0_0 2))
(assert
 (let (($x108 (> depv_1_0_0 0)))
 (=> $x108 x_0_0)))
(assert
 (>= depv_1_0_1 0))
(assert
 (<= depv_1_0_1 2))
(assert
 (let (($x116 (> depv_1_0_1 0)))
 (=> $x116 x_0_1)))
(assert
 (>= depf_1_0_0 0))
(assert
 (<= depf_1_0_0 2))
(assert
 (>= depf_1_0_1 0))
(assert
 (<= depf_1_0_1 2))
(assert
 (let ((?x128 (* depf_1_0_1 1)))
 (<= (+ (+ (+ depv_1_0_0 depv_1_0_1) (* depf_1_0_0 2)) ?x128) 2)))
(assert
 (or (> (+ depf_1_0_0 depf_1_0_1) 1) (> (+ depv_1_0_0 depv_1_0_1) 1)))
(assert
 (>= depv_1_1_0 0))
(assert
 (<= depv_1_1_0 2))
(assert
 (let (($x148 (> depv_1_1_0 0)))
 (=> $x148 x_0_0)))
(assert
 (>= depv_1_1_1 0))
(assert
 (<= depv_1_1_1 2))
(assert
 (let (($x156 (> depv_1_1_1 0)))
 (=> $x156 x_0_1)))
(assert
 (>= depf_1_1_0 0))
(assert
 (<= depf_1_1_0 2))
(assert
 (>= depf_1_1_1 0))
(assert
 (<= depf_1_1_1 2))
(assert
 (let ((?x168 (* depf_1_1_1 1)))
 (<= (+ (+ (+ depv_1_1_0 depv_1_1_1) (* depf_1_1_0 2)) ?x168) 2)))
(assert
 (or (> (+ depf_1_1_0 depf_1_1_1) 1) (> (+ depv_1_1_0 depv_1_1_1) 1)))
(assert
 (let ((?x192 (ite (and (distinct depf_1_0_1 depf_1_1_1) true) 1 0)))
 (let ((?x190 (ite (and (distinct depf_1_0_0 depf_1_1_0) true) 1 0)))
 (let ((?x188 (ite (and (distinct depv_1_0_1 depv_1_1_1) true) 1 0)))
 (let ((?x186 (ite (and (distinct depv_1_0_0 depv_1_1_0) true) 1 0)))
 (let (($x193 (and x_1_0 x_1_1)))
 (=> $x193 (> (+ (+ (+ ?x186 ?x188) ?x190) ?x192) 0))))))))
(assert
 (let ((?x223 (ite (and (distinct depf_1_1_1 depf_1_0_1) true) 1 0)))
 (let ((?x221 (ite (and (distinct depf_1_1_0 depf_1_0_0) true) 1 0)))
 (let ((?x219 (ite (and (distinct depv_1_1_1 depv_1_0_1) true) 1 0)))
 (let ((?x217 (ite (and (distinct depv_1_1_0 depv_1_0_0) true) 1 0)))
 (let (($x224 (and x_1_1 x_1_0)))
 (=> $x224 (> (+ (+ (+ ?x217 ?x219) ?x221) ?x223) 0))))))))
(assert
 (>= depv_2_0_0 0))
(assert
 (<= depv_2_0_0 2))
(assert
 (let (($x250 (> depv_2_0_0 0)))
 (=> $x250 x_1_0)))
(assert
 (>= depv_2_0_1 0))
(assert
 (<= depv_2_0_1 2))
(assert
 (let (($x258 (> depv_2_0_1 0)))
 (=> $x258 x_1_1)))
(assert
 (>= depf_2_0_0 0))
(assert
 (<= depf_2_0_0 2))
(assert
 (>= depf_2_0_1 0))
(assert
 (<= depf_2_0_1 2))
(assert
 (let ((?x270 (* depf_2_0_1 1)))
 (<= (+ (+ (+ depv_2_0_0 depv_2_0_1) (* depf_2_0_0 2)) ?x270) 2)))
(assert
 (or (> (+ depf_2_0_0 depf_2_0_1) 1) (> (+ depv_2_0_0 depv_2_0_1) 1)))
(assert
 (>= depv_2_1_0 0))
(assert
 (<= depv_2_1_0 2))
(assert
 (let (($x290 (> depv_2_1_0 0)))
 (=> $x290 x_1_0)))
(assert
 (>= depv_2_1_1 0))
(assert
 (<= depv_2_1_1 2))
(assert
 (let (($x298 (> depv_2_1_1 0)))
 (=> $x298 x_1_1)))
(assert
 (>= depf_2_1_0 0))
(assert
 (<= depf_2_1_0 2))
(assert
 (>= depf_2_1_1 0))
(assert
 (<= depf_2_1_1 2))
(assert
 (let ((?x310 (* depf_2_1_1 1)))
 (<= (+ (+ (+ depv_2_1_0 depv_2_1_1) (* depf_2_1_0 2)) ?x310) 2)))
(assert
 (or (> (+ depf_2_1_0 depf_2_1_1) 1) (> (+ depv_2_1_0 depv_2_1_1) 1)))
(assert
 (let ((?x334 (ite (and (distinct depf_2_0_1 depf_2_1_1) true) 1 0)))
 (let ((?x332 (ite (and (distinct depf_2_0_0 depf_2_1_0) true) 1 0)))
 (let ((?x330 (ite (and (distinct depv_2_0_1 depv_2_1_1) true) 1 0)))
 (let ((?x328 (ite (and (distinct depv_2_0_0 depv_2_1_0) true) 1 0)))
 (let (($x335 (and x_2_0 x_2_1)))
 (=> $x335 (> (+ (+ (+ ?x328 ?x330) ?x332) ?x334) 0))))))))
(assert
 (let ((?x365 (ite (and (distinct depf_2_1_1 depf_2_0_1) true) 1 0)))
 (let ((?x363 (ite (and (distinct depf_2_1_0 depf_2_0_0) true) 1 0)))
 (let ((?x361 (ite (and (distinct depv_2_1_1 depv_2_0_1) true) 1 0)))
 (let ((?x359 (ite (and (distinct depv_2_1_0 depv_2_0_0) true) 1 0)))
 (let (($x366 (and x_2_1 x_2_0)))
 (=> $x366 (> (+ (+ (+ ?x359 ?x361) ?x363) ?x365) 0))))))))
(assert
 (let ((?x38 (* depf_0_0_1 1)))
 (let ((?x33 (* depf_0_0_0 2)))
 (let ((?x39 (+ ?x33 ?x38)))
 (= var_0_0_0 ?x39)))))
(assert
 (let ((?x56 (* depf_0_1_1 1)))
 (let ((?x52 (* depf_0_1_0 2)))
 (let ((?x57 (+ ?x52 ?x56)))
 (= var_0_1_0 ?x57)))))
(assert
 (let ((?x128 (* depf_1_0_1 1)))
 (let ((?x124 (* depf_1_0_0 2)))
 (let ((?x408 (+ (+ (+ (* depv_1_0_0 var_0_0_0) (* depv_1_0_1 var_0_1_0)) ?x124) ?x128)))
 (= var_1_0_0 ?x408)))))
(assert
 (let ((?x168 (* depf_1_1_1 1)))
 (let ((?x164 (* depf_1_1_0 2)))
 (let ((?x415 (+ (+ (+ (* depv_1_1_0 var_0_0_0) (* depv_1_1_1 var_0_1_0)) ?x164) ?x168)))
 (= var_1_1_0 ?x415)))))
(assert
 (let ((?x270 (* depf_2_0_1 1)))
 (let ((?x266 (* depf_2_0_0 2)))
 (let ((?x424 (+ (+ (+ (* depv_2_0_0 var_1_0_0) (* depv_2_0_1 var_1_1_0)) ?x266) ?x270)))
 (= var_2_0_0 ?x424)))))
(assert
 (let ((?x310 (* depf_2_1_1 1)))
 (let ((?x306 (* depf_2_1_0 2)))
 (let ((?x433 (+ (+ (+ (* depv_2_1_0 var_1_0_0) (* depv_2_1_1 var_1_1_0)) ?x306) ?x310)))
 (= var_2_1_0 ?x433)))))
(assert
 (>= depmv_0_0 0))
(assert
 (<= depmv_0_0 2))
(assert
 (let (($x441 (> depmv_0_0 0)))
 (=> $x441 x_2_0)))
(assert
 (>= depmv_0_1 0))
(assert
 (<= depmv_0_1 2))
(assert
 (let (($x451 (> depmv_0_1 0)))
 (=> $x451 x_2_1)))
(assert
 (>= depmf_0_0 0))
(assert
 (<= depmf_0_0 2))
(assert
 (>= depmf_0_1 0))
(assert
 (<= depmf_0_1 2))
(assert
 (let ((?x463 (* depmf_0_1 1)))
 (let ((?x466 (+ (+ (+ depmv_0_0 depmv_0_1) (* depmf_0_0 2)) ?x463)))
 (<= ?x466 2))))
(assert
 (let ((?x463 (* depmf_0_1 1)))
 (let ((?x466 (+ (+ (+ depmv_0_0 depmv_0_1) (* depmf_0_0 2)) ?x463)))
 (>= ?x466 0))))
(assert
 (>= depmv_1_0 0))
(assert
 (<= depmv_1_0 2))
(assert
 (let (($x476 (> depmv_1_0 0)))
 (=> $x476 x_2_0)))
(assert
 (>= depmv_1_1 0))
(assert
 (<= depmv_1_1 2))
(assert
 (let (($x484 (> depmv_1_1 0)))
 (=> $x484 x_2_1)))
(assert
 (>= depmf_1_0 0))
(assert
 (<= depmf_1_0 2))
(assert
 (>= depmf_1_1 0))
(assert
 (<= depmf_1_1 2))
(assert
 (let ((?x496 (* depmf_1_1 1)))
 (let ((?x499 (+ (+ (+ depmv_1_0 depmv_1_1) (* depmf_1_0 2)) ?x496)))
 (<= ?x499 2))))
(assert
 (let ((?x496 (* depmf_1_1 1)))
 (let ((?x499 (+ (+ (+ depmv_1_0 depmv_1_1) (* depmf_1_0 2)) ?x496)))
 (>= ?x499 0))))
(assert
 (let ((?x463 (* depmf_0_1 1)))
 (let ((?x459 (* depmf_0_0 2)))
 (let ((?x510 (+ (+ (+ (* depmv_0_0 var_2_0_0) (* depmv_0_1 var_2_1_0)) ?x459) ?x463)))
 (= ?x510 12)))))
(assert
 (let ((?x496 (* depmf_1_1 1)))
 (let ((?x492 (* depmf_1_0 2)))
 (let ((?x521 (+ (+ (+ (* depmv_1_0 var_2_0_0) (* depmv_1_1 var_2_1_0)) ?x492) ?x496)))
 (= ?x521 12)))))
(assert
 (let (($x148 (> depv_1_1_0 0)))
 (let ((?x540 (+ (+ (ite (> depv_1_1_0 1) 1 0) depv_1_1_1) depf_1_1_0)))
 (let ((?x544 (ite (and (> (+ ?x540 depf_1_1_1) 0) $x148 x_1_1) 1 0)))
 (let (($x108 (> depv_1_0_0 0)))
 (let ((?x532 (+ (+ (ite (> depv_1_0_0 1) 1 0) depv_1_0_1) depf_1_0_0)))
 (let ((?x536 (ite (and (> (+ ?x532 depf_1_0_1) 0) $x108 x_1_0) 1 0)))
 (=> cuenta_0_0 (and x_0_0 (> (+ ?x536 ?x544) 0))))))))))
(assert
 (let (($x156 (> depv_1_1_1 0)))
 (let ((?x584 (+ (+ depv_1_1_0 (ite (> depv_1_1_1 1) 1 0)) depf_1_1_0)))
 (let ((?x588 (ite (and (> (+ ?x584 depf_1_1_1) 0) $x156 x_1_1) 1 0)))
 (let (($x116 (> depv_1_0_1 0)))
 (let ((?x576 (+ (+ depv_1_0_0 (ite (> depv_1_0_1 1) 1 0)) depf_1_0_0)))
 (let ((?x580 (ite (and (> (+ ?x576 depf_1_0_1) 0) $x116 x_1_0) 1 0)))
 (=> cuenta_0_1 (and x_0_1 (> (+ ?x580 ?x588) 0))))))))))
(assert
 (let (($x290 (> depv_2_1_0 0)))
 (let ((?x628 (+ (+ (ite (> depv_2_1_0 1) 1 0) depv_2_1_1) depf_2_1_0)))
 (let ((?x632 (ite (and (> (+ ?x628 depf_2_1_1) 0) $x290 x_2_1) 1 0)))
 (let (($x250 (> depv_2_0_0 0)))
 (let ((?x620 (+ (+ (ite (> depv_2_0_0 1) 1 0) depv_2_0_1) depf_2_0_0)))
 (let ((?x624 (ite (and (> (+ ?x620 depf_2_0_1) 0) $x250 x_2_0) 1 0)))
 (=> cuenta_1_0 (and x_1_0 (> (+ ?x624 ?x632) 0))))))))))
(assert
 (let (($x298 (> depv_2_1_1 0)))
 (let ((?x672 (+ (+ depv_2_1_0 (ite (> depv_2_1_1 1) 1 0)) depf_2_1_0)))
 (let ((?x676 (ite (and (> (+ ?x672 depf_2_1_1) 0) $x298 x_2_1) 1 0)))
 (let (($x258 (> depv_2_0_1 0)))
 (let ((?x664 (+ (+ depv_2_0_0 (ite (> depv_2_0_1 1) 1 0)) depf_2_0_0)))
 (let ((?x668 (ite (and (> (+ ?x664 depf_2_0_1) 0) $x258 x_2_0) 1 0)))
 (=> cuenta_1_1 (and x_1_1 (> (+ ?x668 ?x676) 0))))))))))
(assert
 (=> cuenta_2_0 (and x_2_0 (> depmv_0_0 0))))
(assert
 (=> cuenta_2_0 (and x_2_0 (> depmv_1_0 0))))
(assert
 (=> cuenta_2_1 (and x_2_1 (> depmv_0_1 0))))
(assert
 (=> cuenta_2_1 (and x_2_1 (> depmv_1_1 0))))
(assert
 (let ((?x715 (ite cuenta_2_1 1 0)))
(let ((?x704 (ite cuenta_2_0 1 0)))
(let ((?x660 (ite cuenta_1_1 1 0)))
(let ((?x616 (ite cuenta_1_0 1 0)))
(let ((?x726 (+ (+ (ite cuenta_0_0 1 0) (ite cuenta_0_1 1 0)) ?x616)))
(<= (+ (+ (+ ?x726 ?x660) ?x704) ?x715) 3)))))))
(check-sat)
