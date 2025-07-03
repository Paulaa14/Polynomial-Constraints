; benchmark generated from python API
(set-info :status unknown)
(declare-fun depf_0_0_0 () Int)
(declare-fun depf_0_0_1 () Int)
(declare-fun depf_0_0_2 () Int)
(declare-fun depf_0_0_3 () Int)
(declare-fun depf_0_0_4 () Int)
(declare-fun depf_0_1_0 () Int)
(declare-fun depf_0_1_1 () Int)
(declare-fun depf_0_1_2 () Int)
(declare-fun depf_0_1_3 () Int)
(declare-fun depf_0_1_4 () Int)
(declare-fun x_0_1 () Bool)
(declare-fun x_0_0 () Bool)
(declare-fun depv_1_0_0 () Int)
(declare-fun depv_1_0_1 () Int)
(declare-fun depf_1_0_0 () Int)
(declare-fun depf_1_0_1 () Int)
(declare-fun depf_1_0_2 () Int)
(declare-fun depf_1_0_3 () Int)
(declare-fun depf_1_0_4 () Int)
(declare-fun depv_1_1_0 () Int)
(declare-fun depv_1_1_1 () Int)
(declare-fun depf_1_1_0 () Int)
(declare-fun depf_1_1_1 () Int)
(declare-fun depf_1_1_2 () Int)
(declare-fun depf_1_1_3 () Int)
(declare-fun depf_1_1_4 () Int)
(declare-fun x_1_1 () Bool)
(declare-fun x_1_0 () Bool)
(declare-fun depv_2_0_0 () Int)
(declare-fun depv_2_0_1 () Int)
(declare-fun depf_2_0_0 () Int)
(declare-fun depf_2_0_1 () Int)
(declare-fun depf_2_0_2 () Int)
(declare-fun depf_2_0_3 () Int)
(declare-fun depf_2_0_4 () Int)
(declare-fun depv_2_1_0 () Int)
(declare-fun depv_2_1_1 () Int)
(declare-fun depf_2_1_0 () Int)
(declare-fun depf_2_1_1 () Int)
(declare-fun depf_2_1_2 () Int)
(declare-fun depf_2_1_3 () Int)
(declare-fun depf_2_1_4 () Int)
(declare-fun x_2_1 () Bool)
(declare-fun x_2_0 () Bool)
(declare-fun var_0_0_0 () Int)
(declare-fun var_0_0_1 () Int)
(declare-fun var_0_1_0 () Int)
(declare-fun var_0_1_1 () Int)
(declare-fun var_1_0_0 () Int)
(declare-fun var_1_0_1 () Int)
(declare-fun var_1_1_0 () Int)
(declare-fun var_1_1_1 () Int)
(declare-fun var_2_0_0 () Int)
(declare-fun var_2_0_1 () Int)
(declare-fun var_2_1_0 () Int)
(declare-fun var_2_1_1 () Int)
(declare-fun depmv_0_0 () Int)
(declare-fun depmv_0_1 () Int)
(declare-fun depmf_0_0 () Int)
(declare-fun depmf_0_1 () Int)
(declare-fun depmf_0_2 () Int)
(declare-fun depmf_0_3 () Int)
(declare-fun depmf_0_4 () Int)
(declare-fun depmv_1_0 () Int)
(declare-fun depmv_1_1 () Int)
(declare-fun depmf_1_0 () Int)
(declare-fun depmf_1_1 () Int)
(declare-fun depmf_1_2 () Int)
(declare-fun depmf_1_3 () Int)
(declare-fun depmf_1_4 () Int)
(declare-fun depmv_2_0 () Int)
(declare-fun depmv_2_1 () Int)
(declare-fun depmf_2_0 () Int)
(declare-fun depmf_2_1 () Int)
(declare-fun depmf_2_2 () Int)
(declare-fun depmf_2_3 () Int)
(declare-fun depmf_2_4 () Int)
(declare-fun depmv_3_0 () Int)
(declare-fun depmv_3_1 () Int)
(declare-fun depmf_3_0 () Int)
(declare-fun depmf_3_1 () Int)
(declare-fun depmf_3_2 () Int)
(declare-fun depmf_3_3 () Int)
(declare-fun depmf_3_4 () Int)
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
 (>= depf_0_0_2 0))
(assert
 (<= depf_0_0_2 2))
(assert
 (>= depf_0_0_3 0))
(assert
 (<= depf_0_0_3 2))
(assert
 (>= depf_0_0_4 0))
(assert
 (<= depf_0_0_4 2))
(assert
 (let ((?x50 (* depf_0_0_4 1)))
 (let ((?x46 (* depf_0_0_3 2)))
 (let ((?x42 (* depf_0_0_2 1)))
 (let ((?x54 (+ (+ (+ (+ (* depf_0_0_0 2) (* depf_0_0_1 2)) ?x42) ?x46) ?x50)))
 (<= ?x54 2))))))
(assert
 (let ((?x64 (+ (+ (+ (+ depf_0_0_0 depf_0_0_1) depf_0_0_2) depf_0_0_3) depf_0_0_4)))
 (or (> ?x64 1) false)))
(assert
 (>= depf_0_1_0 0))
(assert
 (<= depf_0_1_0 2))
(assert
 (>= depf_0_1_1 0))
(assert
 (<= depf_0_1_1 2))
(assert
 (>= depf_0_1_2 0))
(assert
 (<= depf_0_1_2 2))
(assert
 (>= depf_0_1_3 0))
(assert
 (<= depf_0_1_3 2))
(assert
 (>= depf_0_1_4 0))
(assert
 (<= depf_0_1_4 2))
(assert
 (let ((?x89 (* depf_0_1_4 1)))
 (let ((?x85 (* depf_0_1_3 2)))
 (let ((?x81 (* depf_0_1_2 1)))
 (let ((?x93 (+ (+ (+ (+ (* depf_0_1_0 2) (* depf_0_1_1 2)) ?x81) ?x85) ?x89)))
 (<= ?x93 2))))))
(assert
 (let ((?x103 (+ (+ (+ (+ depf_0_1_0 depf_0_1_1) depf_0_1_2) depf_0_1_3) depf_0_1_4)))
 (or (> ?x103 1) false)))
(assert
 (let ((?x118 (ite (and (distinct depf_0_0_4 depf_0_1_4) true) 1 0)))
 (let ((?x116 (ite (and (distinct depf_0_0_3 depf_0_1_3) true) 1 0)))
 (let ((?x114 (ite (and (distinct depf_0_0_2 depf_0_1_2) true) 1 0)))
 (let ((?x112 (ite (and (distinct depf_0_0_1 depf_0_1_1) true) 1 0)))
 (let ((?x110 (ite (and (distinct depf_0_0_0 depf_0_1_0) true) 1 0)))
 (let (($x119 (and x_0_0 x_0_1)))
 (=> $x119 (> (+ (+ (+ (+ ?x110 ?x112) ?x114) ?x116) ?x118) 0)))))))))
(assert
 (let ((?x155 (ite (and (distinct depf_0_1_4 depf_0_0_4) true) 1 0)))
 (let ((?x153 (ite (and (distinct depf_0_1_3 depf_0_0_3) true) 1 0)))
 (let ((?x151 (ite (and (distinct depf_0_1_2 depf_0_0_2) true) 1 0)))
 (let ((?x149 (ite (and (distinct depf_0_1_1 depf_0_0_1) true) 1 0)))
 (let ((?x147 (ite (and (distinct depf_0_1_0 depf_0_0_0) true) 1 0)))
 (let (($x156 (and x_0_1 x_0_0)))
 (=> $x156 (> (+ (+ (+ (+ ?x147 ?x149) ?x151) ?x153) ?x155) 0)))))))))
(assert
 (>= depv_1_0_0 0))
(assert
 (<= depv_1_0_0 2))
(assert
 (let (($x186 (> depv_1_0_0 0)))
 (=> $x186 x_0_0)))
(assert
 (>= depv_1_0_1 0))
(assert
 (<= depv_1_0_1 2))
(assert
 (let (($x194 (> depv_1_0_1 0)))
 (=> $x194 x_0_1)))
(assert
 (>= depf_1_0_0 0))
(assert
 (<= depf_1_0_0 2))
(assert
 (>= depf_1_0_1 0))
(assert
 (<= depf_1_0_1 2))
(assert
 (>= depf_1_0_2 0))
(assert
 (<= depf_1_0_2 2))
(assert
 (>= depf_1_0_3 0))
(assert
 (<= depf_1_0_3 2))
(assert
 (>= depf_1_0_4 0))
(assert
 (<= depf_1_0_4 2))
(assert
 (let ((?x218 (* depf_1_0_4 1)))
 (let ((?x214 (* depf_1_0_3 2)))
 (let ((?x210 (* depf_1_0_2 1)))
 (let ((?x206 (* depf_1_0_1 2)))
 (let ((?x222 (+ (+ (+ (+ depv_1_0_0 depv_1_0_1) (* depf_1_0_0 2)) ?x206) ?x210)))
 (<= (+ (+ ?x222 ?x214) ?x218) 2)))))))
(assert
 (let ((?x234 (+ (+ (+ (+ depf_1_0_0 depf_1_0_1) depf_1_0_2) depf_1_0_3) depf_1_0_4)))
 (or (> ?x234 1) (> (+ depv_1_0_0 depv_1_0_1) 1))))
(assert
 (>= depv_1_1_0 0))
(assert
 (<= depv_1_1_0 2))
(assert
 (let (($x247 (> depv_1_1_0 0)))
 (=> $x247 x_0_0)))
(assert
 (>= depv_1_1_1 0))
(assert
 (<= depv_1_1_1 2))
(assert
 (let (($x255 (> depv_1_1_1 0)))
 (=> $x255 x_0_1)))
(assert
 (>= depf_1_1_0 0))
(assert
 (<= depf_1_1_0 2))
(assert
 (>= depf_1_1_1 0))
(assert
 (<= depf_1_1_1 2))
(assert
 (>= depf_1_1_2 0))
(assert
 (<= depf_1_1_2 2))
(assert
 (>= depf_1_1_3 0))
(assert
 (<= depf_1_1_3 2))
(assert
 (>= depf_1_1_4 0))
(assert
 (<= depf_1_1_4 2))
(assert
 (let ((?x279 (* depf_1_1_4 1)))
 (let ((?x275 (* depf_1_1_3 2)))
 (let ((?x271 (* depf_1_1_2 1)))
 (let ((?x267 (* depf_1_1_1 2)))
 (let ((?x283 (+ (+ (+ (+ depv_1_1_0 depv_1_1_1) (* depf_1_1_0 2)) ?x267) ?x271)))
 (<= (+ (+ ?x283 ?x275) ?x279) 2)))))))
(assert
 (let ((?x295 (+ (+ (+ (+ depf_1_1_0 depf_1_1_1) depf_1_1_2) depf_1_1_3) depf_1_1_4)))
 (or (> ?x295 1) (> (+ depv_1_1_0 depv_1_1_1) 1))))
(assert
 (let ((?x318 (ite (and (distinct depf_1_0_4 depf_1_1_4) true) 1 0)))
 (let ((?x316 (ite (and (distinct depf_1_0_3 depf_1_1_3) true) 1 0)))
 (let ((?x314 (ite (and (distinct depf_1_0_2 depf_1_1_2) true) 1 0)))
 (let ((?x312 (ite (and (distinct depf_1_0_1 depf_1_1_1) true) 1 0)))
 (let ((?x310 (ite (and (distinct depf_1_0_0 depf_1_1_0) true) 1 0)))
 (let ((?x308 (ite (and (distinct depv_1_0_1 depv_1_1_1) true) 1 0)))
 (let ((?x306 (ite (and (distinct depv_1_0_0 depv_1_1_0) true) 1 0)))
 (let (($x326 (> (+ (+ (+ (+ (+ (+ ?x306 ?x308) ?x310) ?x312) ?x314) ?x316) ?x318) 0)))
 (let (($x319 (and x_1_0 x_1_1)))
 (=> $x319 $x326)))))))))))
(assert
 (let ((?x367 (ite (and (distinct depf_1_1_4 depf_1_0_4) true) 1 0)))
 (let ((?x365 (ite (and (distinct depf_1_1_3 depf_1_0_3) true) 1 0)))
 (let ((?x363 (ite (and (distinct depf_1_1_2 depf_1_0_2) true) 1 0)))
 (let ((?x361 (ite (and (distinct depf_1_1_1 depf_1_0_1) true) 1 0)))
 (let ((?x359 (ite (and (distinct depf_1_1_0 depf_1_0_0) true) 1 0)))
 (let ((?x357 (ite (and (distinct depv_1_1_1 depv_1_0_1) true) 1 0)))
 (let ((?x355 (ite (and (distinct depv_1_1_0 depv_1_0_0) true) 1 0)))
 (let (($x375 (> (+ (+ (+ (+ (+ (+ ?x355 ?x357) ?x359) ?x361) ?x363) ?x365) ?x367) 0)))
 (let (($x368 (and x_1_1 x_1_0)))
 (=> $x368 $x375)))))))))))
(assert
 (>= depv_2_0_0 0))
(assert
 (<= depv_2_0_0 2))
(assert
 (let (($x406 (> depv_2_0_0 0)))
 (=> $x406 x_1_0)))
(assert
 (>= depv_2_0_1 0))
(assert
 (<= depv_2_0_1 2))
(assert
 (let (($x414 (> depv_2_0_1 0)))
 (=> $x414 x_1_1)))
(assert
 (>= depf_2_0_0 0))
(assert
 (<= depf_2_0_0 2))
(assert
 (>= depf_2_0_1 0))
(assert
 (<= depf_2_0_1 2))
(assert
 (>= depf_2_0_2 0))
(assert
 (<= depf_2_0_2 2))
(assert
 (>= depf_2_0_3 0))
(assert
 (<= depf_2_0_3 2))
(assert
 (>= depf_2_0_4 0))
(assert
 (<= depf_2_0_4 2))
(assert
 (let ((?x438 (* depf_2_0_4 1)))
 (let ((?x434 (* depf_2_0_3 2)))
 (let ((?x430 (* depf_2_0_2 1)))
 (let ((?x426 (* depf_2_0_1 2)))
 (let ((?x442 (+ (+ (+ (+ depv_2_0_0 depv_2_0_1) (* depf_2_0_0 2)) ?x426) ?x430)))
 (<= (+ (+ ?x442 ?x434) ?x438) 2)))))))
(assert
 (let ((?x454 (+ (+ (+ (+ depf_2_0_0 depf_2_0_1) depf_2_0_2) depf_2_0_3) depf_2_0_4)))
 (or (> ?x454 1) (> (+ depv_2_0_0 depv_2_0_1) 1))))
(assert
 (>= depv_2_1_0 0))
(assert
 (<= depv_2_1_0 2))
(assert
 (let (($x467 (> depv_2_1_0 0)))
 (=> $x467 x_1_0)))
(assert
 (>= depv_2_1_1 0))
(assert
 (<= depv_2_1_1 2))
(assert
 (let (($x475 (> depv_2_1_1 0)))
 (=> $x475 x_1_1)))
(assert
 (>= depf_2_1_0 0))
(assert
 (<= depf_2_1_0 2))
(assert
 (>= depf_2_1_1 0))
(assert
 (<= depf_2_1_1 2))
(assert
 (>= depf_2_1_2 0))
(assert
 (<= depf_2_1_2 2))
(assert
 (>= depf_2_1_3 0))
(assert
 (<= depf_2_1_3 2))
(assert
 (>= depf_2_1_4 0))
(assert
 (<= depf_2_1_4 2))
(assert
 (let ((?x499 (* depf_2_1_4 1)))
 (let ((?x495 (* depf_2_1_3 2)))
 (let ((?x491 (* depf_2_1_2 1)))
 (let ((?x487 (* depf_2_1_1 2)))
 (let ((?x503 (+ (+ (+ (+ depv_2_1_0 depv_2_1_1) (* depf_2_1_0 2)) ?x487) ?x491)))
 (<= (+ (+ ?x503 ?x495) ?x499) 2)))))))
(assert
 (let ((?x515 (+ (+ (+ (+ depf_2_1_0 depf_2_1_1) depf_2_1_2) depf_2_1_3) depf_2_1_4)))
 (or (> ?x515 1) (> (+ depv_2_1_0 depv_2_1_1) 1))))
(assert
 (let ((?x538 (ite (and (distinct depf_2_0_4 depf_2_1_4) true) 1 0)))
 (let ((?x536 (ite (and (distinct depf_2_0_3 depf_2_1_3) true) 1 0)))
 (let ((?x534 (ite (and (distinct depf_2_0_2 depf_2_1_2) true) 1 0)))
 (let ((?x532 (ite (and (distinct depf_2_0_1 depf_2_1_1) true) 1 0)))
 (let ((?x530 (ite (and (distinct depf_2_0_0 depf_2_1_0) true) 1 0)))
 (let ((?x528 (ite (and (distinct depv_2_0_1 depv_2_1_1) true) 1 0)))
 (let ((?x526 (ite (and (distinct depv_2_0_0 depv_2_1_0) true) 1 0)))
 (let (($x546 (> (+ (+ (+ (+ (+ (+ ?x526 ?x528) ?x530) ?x532) ?x534) ?x536) ?x538) 0)))
 (let (($x539 (and x_2_0 x_2_1)))
 (=> $x539 $x546)))))))))))
(assert
 (let ((?x587 (ite (and (distinct depf_2_1_4 depf_2_0_4) true) 1 0)))
 (let ((?x585 (ite (and (distinct depf_2_1_3 depf_2_0_3) true) 1 0)))
 (let ((?x583 (ite (and (distinct depf_2_1_2 depf_2_0_2) true) 1 0)))
 (let ((?x581 (ite (and (distinct depf_2_1_1 depf_2_0_1) true) 1 0)))
 (let ((?x579 (ite (and (distinct depf_2_1_0 depf_2_0_0) true) 1 0)))
 (let ((?x577 (ite (and (distinct depv_2_1_1 depv_2_0_1) true) 1 0)))
 (let ((?x575 (ite (and (distinct depv_2_1_0 depv_2_0_0) true) 1 0)))
 (let (($x595 (> (+ (+ (+ (+ (+ (+ ?x575 ?x577) ?x579) ?x581) ?x583) ?x585) ?x587) 0)))
 (let (($x588 (and x_2_1 x_2_0)))
 (=> $x588 $x595)))))))))))
(assert
 (let ((?x637 (* depf_0_0_4 0)))
 (let ((?x636 (* depf_0_0_3 0)))
 (let ((?x42 (* depf_0_0_2 1)))
 (let ((?x641 (+ (+ (+ (+ (* depf_0_0_0 2) (* depf_0_0_1 1)) ?x42) ?x636) ?x637)))
 (= var_0_0_0 ?x641))))))
(assert
 (let ((?x50 (* depf_0_0_4 1)))
 (let ((?x46 (* depf_0_0_3 2)))
 (let ((?x645 (* depf_0_0_2 0)))
 (let ((?x652 (+ (+ (+ (+ (* depf_0_0_0 0) (* depf_0_0_1 1)) ?x645) ?x46) ?x50)))
 (= var_0_0_1 ?x652))))))
(assert
 (let ((?x657 (* depf_0_1_4 0)))
 (let ((?x656 (* depf_0_1_3 0)))
 (let ((?x81 (* depf_0_1_2 1)))
 (let ((?x663 (+ (+ (+ (+ (* depf_0_1_0 2) (* depf_0_1_1 1)) ?x81) ?x656) ?x657)))
 (= var_0_1_0 ?x663))))))
(assert
 (let ((?x89 (* depf_0_1_4 1)))
 (let ((?x85 (* depf_0_1_3 2)))
 (let ((?x667 (* depf_0_1_2 0)))
 (let ((?x673 (+ (+ (+ (+ (* depf_0_1_0 0) (* depf_0_1_1 1)) ?x667) ?x85) ?x89)))
 (= var_0_1_1 ?x673))))))
(assert
 (let ((?x680 (* depf_1_0_4 0)))
 (let ((?x679 (* depf_1_0_3 0)))
 (let ((?x210 (* depf_1_0_2 1)))
 (let ((?x678 (* depf_1_0_1 1)))
 (let ((?x202 (* depf_1_0_0 2)))
 (let ((?x685 (+ (+ (+ (* depv_1_0_0 var_0_0_0) (* depv_1_0_1 var_0_1_0)) ?x202) ?x678)))
 (= var_1_0_0 (+ (+ (+ ?x685 ?x210) ?x679) ?x680)))))))))
(assert
 (let ((?x218 (* depf_1_0_4 1)))
 (let ((?x214 (* depf_1_0_3 2)))
 (let ((?x694 (* depf_1_0_2 0)))
 (let ((?x678 (* depf_1_0_1 1)))
 (let ((?x693 (* depf_1_0_0 0)))
 (let ((?x697 (+ (+ (+ (* depv_1_0_0 var_0_0_1) (* depv_1_0_1 var_0_1_1)) ?x693) ?x678)))
 (= var_1_0_1 (+ (+ (+ ?x697 ?x694) ?x214) ?x218)))))))))
(assert
 (let ((?x709 (* depf_1_1_4 0)))
 (let ((?x708 (* depf_1_1_3 0)))
 (let ((?x271 (* depf_1_1_2 1)))
 (let ((?x707 (* depf_1_1_1 1)))
 (let ((?x263 (* depf_1_1_0 2)))
 (let ((?x714 (+ (+ (+ (* depv_1_1_0 var_0_0_0) (* depv_1_1_1 var_0_1_0)) ?x263) ?x707)))
 (= var_1_1_0 (+ (+ (+ ?x714 ?x271) ?x708) ?x709)))))))))
(assert
 (let ((?x279 (* depf_1_1_4 1)))
 (let ((?x275 (* depf_1_1_3 2)))
 (let ((?x723 (* depf_1_1_2 0)))
 (let ((?x707 (* depf_1_1_1 1)))
 (let ((?x722 (* depf_1_1_0 0)))
 (let ((?x726 (+ (+ (+ (* depv_1_1_0 var_0_0_1) (* depv_1_1_1 var_0_1_1)) ?x722) ?x707)))
 (= var_1_1_1 (+ (+ (+ ?x726 ?x723) ?x275) ?x279)))))))))
(assert
 (let ((?x738 (* depf_2_0_4 0)))
 (let ((?x737 (* depf_2_0_3 0)))
 (let ((?x430 (* depf_2_0_2 1)))
 (let ((?x736 (* depf_2_0_1 1)))
 (let ((?x422 (* depf_2_0_0 2)))
 (let ((?x743 (+ (+ (+ (* depv_2_0_0 var_1_0_0) (* depv_2_0_1 var_1_1_0)) ?x422) ?x736)))
 (= var_2_0_0 (+ (+ (+ ?x743 ?x430) ?x737) ?x738)))))))))
(assert
 (let ((?x438 (* depf_2_0_4 1)))
 (let ((?x434 (* depf_2_0_3 2)))
 (let ((?x752 (* depf_2_0_2 0)))
 (let ((?x736 (* depf_2_0_1 1)))
 (let ((?x751 (* depf_2_0_0 0)))
 (let ((?x755 (+ (+ (+ (* depv_2_0_0 var_1_0_1) (* depv_2_0_1 var_1_1_1)) ?x751) ?x736)))
 (= var_2_0_1 (+ (+ (+ ?x755 ?x752) ?x434) ?x438)))))))))
(assert
 (let ((?x767 (* depf_2_1_4 0)))
 (let ((?x766 (* depf_2_1_3 0)))
 (let ((?x491 (* depf_2_1_2 1)))
 (let ((?x765 (* depf_2_1_1 1)))
 (let ((?x483 (* depf_2_1_0 2)))
 (let ((?x772 (+ (+ (+ (* depv_2_1_0 var_1_0_0) (* depv_2_1_1 var_1_1_0)) ?x483) ?x765)))
 (= var_2_1_0 (+ (+ (+ ?x772 ?x491) ?x766) ?x767)))))))))
(assert
 (let ((?x499 (* depf_2_1_4 1)))
 (let ((?x495 (* depf_2_1_3 2)))
 (let ((?x781 (* depf_2_1_2 0)))
 (let ((?x765 (* depf_2_1_1 1)))
 (let ((?x780 (* depf_2_1_0 0)))
 (let ((?x784 (+ (+ (+ (* depv_2_1_0 var_1_0_1) (* depv_2_1_1 var_1_1_1)) ?x780) ?x765)))
 (= var_2_1_1 (+ (+ (+ ?x784 ?x781) ?x495) ?x499)))))))))
(assert
 (>= depmv_0_0 0))
(assert
 (<= depmv_0_0 2))
(assert
 (let (($x795 (> depmv_0_0 0)))
 (=> $x795 x_2_0)))
(assert
 (>= depmv_0_1 0))
(assert
 (<= depmv_0_1 2))
(assert
 (let (($x807 (> depmv_0_1 0)))
 (=> $x807 x_2_1)))
(assert
 (>= depmf_0_0 0))
(assert
 (<= depmf_0_0 2))
(assert
 (>= depmf_0_1 0))
(assert
 (<= depmf_0_1 2))
(assert
 (>= depmf_0_2 0))
(assert
 (<= depmf_0_2 2))
(assert
 (>= depmf_0_3 0))
(assert
 (<= depmf_0_3 2))
(assert
 (>= depmf_0_4 0))
(assert
 (<= depmf_0_4 2))
(assert
 (let ((?x833 (* depmf_0_4 1)))
 (let ((?x829 (* depmf_0_3 2)))
 (let ((?x825 (* depmf_0_2 1)))
 (let ((?x821 (* depmf_0_1 2)))
 (let ((?x837 (+ (+ (+ (+ depmv_0_0 depmv_0_1) (* depmf_0_0 2)) ?x821) ?x825)))
 (let ((?x839 (+ (+ ?x837 ?x829) ?x833)))
 (<= ?x839 2))))))))
(assert
 (let ((?x833 (* depmf_0_4 1)))
 (let ((?x829 (* depmf_0_3 2)))
 (let ((?x825 (* depmf_0_2 1)))
 (let ((?x821 (* depmf_0_1 2)))
 (let ((?x837 (+ (+ (+ (+ depmv_0_0 depmv_0_1) (* depmf_0_0 2)) ?x821) ?x825)))
 (let ((?x839 (+ (+ ?x837 ?x829) ?x833)))
 (>= ?x839 0))))))))
(assert
 (>= depmv_1_0 0))
(assert
 (<= depmv_1_0 2))
(assert
 (let (($x813 (> depmv_1_0 0)))
 (=> $x813 x_2_0)))
(assert
 (>= depmv_1_1 0))
(assert
 (<= depmv_1_1 2))
(assert
 (let (($x857 (> depmv_1_1 0)))
 (=> $x857 x_2_1)))
(assert
 (>= depmf_1_0 0))
(assert
 (<= depmf_1_0 2))
(assert
 (>= depmf_1_1 0))
(assert
 (<= depmf_1_1 2))
(assert
 (>= depmf_1_2 0))
(assert
 (<= depmf_1_2 2))
(assert
 (>= depmf_1_3 0))
(assert
 (<= depmf_1_3 2))
(assert
 (>= depmf_1_4 0))
(assert
 (<= depmf_1_4 2))
(assert
 (let ((?x883 (* depmf_1_4 1)))
 (let ((?x879 (* depmf_1_3 2)))
 (let ((?x875 (* depmf_1_2 1)))
 (let ((?x871 (* depmf_1_1 2)))
 (let ((?x887 (+ (+ (+ (+ depmv_1_0 depmv_1_1) (* depmf_1_0 2)) ?x871) ?x875)))
 (let ((?x889 (+ (+ ?x887 ?x879) ?x883)))
 (<= ?x889 2))))))))
(assert
 (let ((?x883 (* depmf_1_4 1)))
 (let ((?x879 (* depmf_1_3 2)))
 (let ((?x875 (* depmf_1_2 1)))
 (let ((?x871 (* depmf_1_1 2)))
 (let ((?x887 (+ (+ (+ (+ depmv_1_0 depmv_1_1) (* depmf_1_0 2)) ?x871) ?x875)))
 (let ((?x889 (+ (+ ?x887 ?x879) ?x883)))
 (>= ?x889 0))))))))
(assert
 (>= depmv_2_0 0))
(assert
 (<= depmv_2_0 2))
(assert
 (let (($x863 (> depmv_2_0 0)))
 (=> $x863 x_2_0)))
(assert
 (>= depmv_2_1 0))
(assert
 (<= depmv_2_1 2))
(assert
 (let (($x907 (> depmv_2_1 0)))
 (=> $x907 x_2_1)))
(assert
 (>= depmf_2_0 0))
(assert
 (<= depmf_2_0 2))
(assert
 (>= depmf_2_1 0))
(assert
 (<= depmf_2_1 2))
(assert
 (>= depmf_2_2 0))
(assert
 (<= depmf_2_2 2))
(assert
 (>= depmf_2_3 0))
(assert
 (<= depmf_2_3 2))
(assert
 (>= depmf_2_4 0))
(assert
 (<= depmf_2_4 2))
(assert
 (let ((?x933 (* depmf_2_4 1)))
 (let ((?x929 (* depmf_2_3 2)))
 (let ((?x925 (* depmf_2_2 1)))
 (let ((?x921 (* depmf_2_1 2)))
 (let ((?x937 (+ (+ (+ (+ depmv_2_0 depmv_2_1) (* depmf_2_0 2)) ?x921) ?x925)))
 (let ((?x939 (+ (+ ?x937 ?x929) ?x933)))
 (<= ?x939 2))))))))
(assert
 (let ((?x933 (* depmf_2_4 1)))
 (let ((?x929 (* depmf_2_3 2)))
 (let ((?x925 (* depmf_2_2 1)))
 (let ((?x921 (* depmf_2_1 2)))
 (let ((?x937 (+ (+ (+ (+ depmv_2_0 depmv_2_1) (* depmf_2_0 2)) ?x921) ?x925)))
 (let ((?x939 (+ (+ ?x937 ?x929) ?x933)))
 (>= ?x939 0))))))))
(assert
 (>= depmv_3_0 0))
(assert
 (<= depmv_3_0 2))
(assert
 (let (($x913 (> depmv_3_0 0)))
 (=> $x913 x_2_0)))
(assert
 (>= depmv_3_1 0))
(assert
 (<= depmv_3_1 2))
(assert
 (let (($x957 (> depmv_3_1 0)))
 (=> $x957 x_2_1)))
(assert
 (>= depmf_3_0 0))
(assert
 (<= depmf_3_0 2))
(assert
 (>= depmf_3_1 0))
(assert
 (<= depmf_3_1 2))
(assert
 (>= depmf_3_2 0))
(assert
 (<= depmf_3_2 2))
(assert
 (>= depmf_3_3 0))
(assert
 (<= depmf_3_3 2))
(assert
 (>= depmf_3_4 0))
(assert
 (<= depmf_3_4 2))
(assert
 (let ((?x983 (* depmf_3_4 1)))
 (let ((?x979 (* depmf_3_3 2)))
 (let ((?x975 (* depmf_3_2 1)))
 (let ((?x971 (* depmf_3_1 2)))
 (let ((?x987 (+ (+ (+ (+ depmv_3_0 depmv_3_1) (* depmf_3_0 2)) ?x971) ?x975)))
 (let ((?x989 (+ (+ ?x987 ?x979) ?x983)))
 (<= ?x989 2))))))))
(assert
 (let ((?x983 (* depmf_3_4 1)))
 (let ((?x979 (* depmf_3_3 2)))
 (let ((?x975 (* depmf_3_2 1)))
 (let ((?x971 (* depmf_3_1 2)))
 (let ((?x987 (+ (+ (+ (+ depmv_3_0 depmv_3_1) (* depmf_3_0 2)) ?x971) ?x975)))
 (let ((?x989 (+ (+ ?x987 ?x979) ?x983)))
 (>= ?x989 0))))))))
(assert
 (let ((?x1002 (* depmf_0_4 0)))
 (let ((?x1001 (* depmf_0_3 0)))
 (let ((?x825 (* depmf_0_2 1)))
 (let ((?x1000 (* depmf_0_1 1)))
 (let ((?x817 (* depmf_0_0 2)))
 (let ((?x1005 (+ (+ (+ (* depmv_0_0 var_2_0_0) (* depmv_0_1 var_2_1_0)) ?x817) ?x1000)))
 (= (+ (+ (+ ?x1005 ?x825) ?x1001) ?x1002) 3))))))))
(assert
 (let ((?x833 (* depmf_0_4 1)))
 (let ((?x829 (* depmf_0_3 2)))
 (let ((?x1018 (* depmf_0_2 0)))
 (let ((?x1000 (* depmf_0_1 1)))
 (let ((?x1017 (* depmf_0_0 0)))
 (let ((?x1021 (+ (+ (+ (* depmv_0_0 var_2_0_1) (* depmv_0_1 var_2_1_1)) ?x1017) ?x1000)))
 (= (+ (+ (+ ?x1021 ?x1018) ?x829) ?x833) 0))))))))
(assert
 (let ((?x1034 (* depmf_1_4 0)))
 (let ((?x1033 (* depmf_1_3 0)))
 (let ((?x875 (* depmf_1_2 1)))
 (let ((?x1032 (* depmf_1_1 1)))
 (let ((?x867 (* depmf_1_0 2)))
 (let ((?x1037 (+ (+ (+ (* depmv_1_0 var_2_0_0) (* depmv_1_1 var_2_1_0)) ?x867) ?x1032)))
 (= (+ (+ (+ ?x1037 ?x875) ?x1033) ?x1034) 2))))))))
(assert
 (let ((?x883 (* depmf_1_4 1)))
 (let ((?x879 (* depmf_1_3 2)))
 (let ((?x1049 (* depmf_1_2 0)))
 (let ((?x1032 (* depmf_1_1 1)))
 (let ((?x1048 (* depmf_1_0 0)))
 (let ((?x1052 (+ (+ (+ (* depmv_1_0 var_2_0_1) (* depmv_1_1 var_2_1_1)) ?x1048) ?x1032)))
 (= (+ (+ (+ ?x1052 ?x1049) ?x879) ?x883) 1))))))))
(assert
 (let ((?x1065 (* depmf_2_4 0)))
 (let ((?x1064 (* depmf_2_3 0)))
 (let ((?x925 (* depmf_2_2 1)))
 (let ((?x1063 (* depmf_2_1 1)))
 (let ((?x917 (* depmf_2_0 2)))
 (let ((?x1068 (+ (+ (+ (* depmv_2_0 var_2_0_0) (* depmv_2_1 var_2_1_0)) ?x917) ?x1063)))
 (= (+ (+ (+ ?x1068 ?x925) ?x1064) ?x1065) 1))))))))
(assert
 (let ((?x933 (* depmf_2_4 1)))
 (let ((?x929 (* depmf_2_3 2)))
 (let ((?x1080 (* depmf_2_2 0)))
 (let ((?x1063 (* depmf_2_1 1)))
 (let ((?x1079 (* depmf_2_0 0)))
 (let ((?x1083 (+ (+ (+ (* depmv_2_0 var_2_0_1) (* depmv_2_1 var_2_1_1)) ?x1079) ?x1063)))
 (= (+ (+ (+ ?x1083 ?x1080) ?x929) ?x933) 2))))))))
(assert
 (let ((?x1096 (* depmf_3_4 0)))
 (let ((?x1095 (* depmf_3_3 0)))
 (let ((?x975 (* depmf_3_2 1)))
 (let ((?x1094 (* depmf_3_1 1)))
 (let ((?x967 (* depmf_3_0 2)))
 (let ((?x1099 (+ (+ (+ (* depmv_3_0 var_2_0_0) (* depmv_3_1 var_2_1_0)) ?x967) ?x1094)))
 (= (+ (+ (+ ?x1099 ?x975) ?x1095) ?x1096) 0))))))))
(assert
 (let ((?x983 (* depmf_3_4 1)))
 (let ((?x979 (* depmf_3_3 2)))
 (let ((?x1111 (* depmf_3_2 0)))
 (let ((?x1094 (* depmf_3_1 1)))
 (let ((?x1110 (* depmf_3_0 0)))
 (let ((?x1114 (+ (+ (+ (* depmv_3_0 var_2_0_1) (* depmv_3_1 var_2_1_1)) ?x1110) ?x1094)))
 (= (+ (+ (+ ?x1114 ?x1111) ?x979) ?x983) 3))))))))
(assert
 (let (($x247 (> depv_1_1_0 0)))
 (let ((?x1139 (+ (+ (ite (> depv_1_1_0 1) 1 0) depv_1_1_1) depf_1_1_0)))
 (let ((?x1143 (+ (+ (+ (+ ?x1139 depf_1_1_1) depf_1_1_2) depf_1_1_3) depf_1_1_4)))
 (let ((?x1146 (ite (and (> ?x1143 0) $x247 x_1_1) 1 0)))
 (let (($x186 (> depv_1_0_0 0)))
 (let ((?x1128 (+ (+ (ite (> depv_1_0_0 1) 1 0) depv_1_0_1) depf_1_0_0)))
 (let ((?x1132 (+ (+ (+ (+ ?x1128 depf_1_0_1) depf_1_0_2) depf_1_0_3) depf_1_0_4)))
 (let ((?x1135 (ite (and (> ?x1132 0) $x186 x_1_0) 1 0)))
 (=> cuenta_0_0 (and x_0_0 (> (+ ?x1135 ?x1146) 0))))))))))))
(assert
 (let (($x255 (> depv_1_1_1 0)))
 (let ((?x1189 (+ (+ depv_1_1_0 (ite (> depv_1_1_1 1) 1 0)) depf_1_1_0)))
 (let ((?x1193 (+ (+ (+ (+ ?x1189 depf_1_1_1) depf_1_1_2) depf_1_1_3) depf_1_1_4)))
 (let ((?x1196 (ite (and (> ?x1193 0) $x255 x_1_1) 1 0)))
 (let (($x194 (> depv_1_0_1 0)))
 (let ((?x1178 (+ (+ depv_1_0_0 (ite (> depv_1_0_1 1) 1 0)) depf_1_0_0)))
 (let ((?x1182 (+ (+ (+ (+ ?x1178 depf_1_0_1) depf_1_0_2) depf_1_0_3) depf_1_0_4)))
 (let ((?x1185 (ite (and (> ?x1182 0) $x194 x_1_0) 1 0)))
 (=> cuenta_0_1 (and x_0_1 (> (+ ?x1185 ?x1196) 0))))))))))))
(assert
 (let (($x467 (> depv_2_1_0 0)))
 (let ((?x1239 (+ (+ (ite (> depv_2_1_0 1) 1 0) depv_2_1_1) depf_2_1_0)))
 (let ((?x1243 (+ (+ (+ (+ ?x1239 depf_2_1_1) depf_2_1_2) depf_2_1_3) depf_2_1_4)))
 (let ((?x1246 (ite (and (> ?x1243 0) $x467 x_2_1) 1 0)))
 (let (($x406 (> depv_2_0_0 0)))
 (let ((?x1228 (+ (+ (ite (> depv_2_0_0 1) 1 0) depv_2_0_1) depf_2_0_0)))
 (let ((?x1232 (+ (+ (+ (+ ?x1228 depf_2_0_1) depf_2_0_2) depf_2_0_3) depf_2_0_4)))
 (let ((?x1235 (ite (and (> ?x1232 0) $x406 x_2_0) 1 0)))
 (=> cuenta_1_0 (and x_1_0 (> (+ ?x1235 ?x1246) 0))))))))))))
(assert
 (let (($x475 (> depv_2_1_1 0)))
 (let ((?x1289 (+ (+ depv_2_1_0 (ite (> depv_2_1_1 1) 1 0)) depf_2_1_0)))
 (let ((?x1293 (+ (+ (+ (+ ?x1289 depf_2_1_1) depf_2_1_2) depf_2_1_3) depf_2_1_4)))
 (let ((?x1296 (ite (and (> ?x1293 0) $x475 x_2_1) 1 0)))
 (let (($x414 (> depv_2_0_1 0)))
 (let ((?x1278 (+ (+ depv_2_0_0 (ite (> depv_2_0_1 1) 1 0)) depf_2_0_0)))
 (let ((?x1282 (+ (+ (+ (+ ?x1278 depf_2_0_1) depf_2_0_2) depf_2_0_3) depf_2_0_4)))
 (let ((?x1285 (ite (and (> ?x1282 0) $x414 x_2_0) 1 0)))
 (=> cuenta_1_1 (and x_1_1 (> (+ ?x1285 ?x1296) 0))))))))))))
(assert
 (=> cuenta_2_0 (and x_2_0 (> depmv_0_0 0))))
(assert
 (=> cuenta_2_0 (and x_2_0 (> depmv_1_0 0))))
(assert
 (=> cuenta_2_0 (and x_2_0 (> depmv_2_0 0))))
(assert
 (=> cuenta_2_0 (and x_2_0 (> depmv_3_0 0))))
(assert
 (=> cuenta_2_1 (and x_2_1 (> depmv_0_1 0))))
(assert
 (=> cuenta_2_1 (and x_2_1 (> depmv_1_1 0))))
(assert
 (=> cuenta_2_1 (and x_2_1 (> depmv_2_1 0))))
(assert
 (=> cuenta_2_1 (and x_2_1 (> depmv_3_1 0))))
(assert
 (let ((?x1343 (ite cuenta_2_1 1 0)))
(let ((?x1324 (ite cuenta_2_0 1 0)))
(let ((?x1274 (ite cuenta_1_1 1 0)))
(let ((?x1224 (ite cuenta_1_0 1 0)))
(let ((?x1362 (+ (+ (ite cuenta_0_0 1 0) (ite cuenta_0_1 1 0)) ?x1224)))
(<= (+ (+ (+ ?x1362 ?x1274) ?x1324) ?x1343) 3)))))))
(check-sat)
