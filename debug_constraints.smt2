; benchmark generated from python API
(set-info :status unknown)
(declare-fun ocupaf_0_0_0_1 () Bool)
(declare-fun ocupaf_0_0_0_0 () Bool)
(declare-fun ocupaf_0_0_1_1 () Bool)
(declare-fun ocupaf_0_0_1_0 () Bool)
(declare-fun var_0_0_0 () Int)
(declare-fun x_0_0 () Bool)
(declare-fun ocupamv_0_0_0 () Bool)
(declare-fun ocupamf_0_1 () Bool)
(declare-fun ocupamf_0_0 () Bool)
(declare-fun ocupamv_0_1_0 () Bool)
(declare-fun ocupamv_1_0_0 () Bool)
(declare-fun ocupamf_1_1 () Bool)
(declare-fun ocupamf_1_0 () Bool)
(declare-fun ocupamv_1_1_0 () Bool)
(declare-fun cuenta_0_0 () Bool)
(assert
 (let ((?x13 (ite ocupaf_0_0_0_1 1 0)))
 (let ((?x11 (ite ocupaf_0_0_0_0 1 0)))
 (let ((?x14 (+ ?x11 ?x13)))
 (or (= ?x14 0) (= ?x14 1))))))
(assert
 (let ((?x39 (ite ocupaf_0_0_1_1 1 0)))
 (let ((?x37 (ite ocupaf_0_0_1_0 1 0)))
 (let ((?x40 (+ ?x37 ?x39)))
 (or (= ?x40 0) (= ?x40 1))))))
(assert
 (let ((?x39 (ite ocupaf_0_0_1_1 1 0)))
 (let ((?x36 (ite ocupaf_0_0_1_0 2 0)))
 (let ((?x45 (+ (+ (ite ocupaf_0_0_0_0 2 0) (ite ocupaf_0_0_0_1 1 0)) ?x36)))
 (let ((?x46 (+ ?x45 ?x39)))
 (<= ?x46 2))))))
(assert
 (let ((?x39 (ite ocupaf_0_0_1_1 1 0)))
 (let ((?x37 (ite ocupaf_0_0_1_0 1 0)))
 (let ((?x40 (+ ?x37 ?x39)))
 (let ((?x13 (ite ocupaf_0_0_0_1 1 0)))
 (let ((?x11 (ite ocupaf_0_0_0_0 1 0)))
 (let ((?x14 (+ ?x11 ?x13)))
 (> (+ ?x14 ?x40) 1))))))))
(assert
 (let ((?x39 (ite ocupaf_0_0_1_1 1 0)))
 (let ((?x36 (ite ocupaf_0_0_1_0 2 0)))
 (let ((?x45 (+ (+ (ite ocupaf_0_0_0_0 2 0) (ite ocupaf_0_0_0_1 1 0)) ?x36)))
 (let ((?x46 (+ ?x45 ?x39)))
 (= var_0_0_0 ?x46))))))
(assert
 (=> ocupamv_0_0_0 x_0_0))
(assert
 (let ((?x70 (ite ocupamf_0_1 1 0)))
 (let ((?x72 (+ (+ (ite ocupamv_0_0_0 1 0) (ite ocupamf_0_0 1 0)) ?x70)))
 (or (= ?x72 0) (= ?x72 1)))))
(assert
 (=> ocupamv_0_1_0 x_0_0))
(assert
 (let ((?x70 (ite ocupamf_0_1 1 0)))
 (let ((?x86 (+ (+ (ite ocupamv_0_1_0 1 0) (ite ocupamf_0_0 1 0)) ?x70)))
 (or (= ?x86 0) (= ?x86 1)))))
(assert
 (let ((?x70 (ite ocupamf_0_1 1 0)))
 (let ((?x67 (ite ocupamf_0_0 2 0)))
 (let ((?x84 (ite ocupamv_0_1_0 1 0)))
 (let ((?x98 (+ (+ (+ (+ (+ (ite ocupamv_0_0_0 1 0) ?x67) ?x70) ?x84) ?x67) ?x70)))
 (<= ?x98 2))))))
(assert
 (=> ocupamv_1_0_0 x_0_0))
(assert
 (let ((?x113 (ite ocupamf_1_1 1 0)))
 (let ((?x115 (+ (+ (ite ocupamv_1_0_0 1 0) (ite ocupamf_1_0 1 0)) ?x113)))
 (or (= ?x115 0) (= ?x115 1)))))
(assert
 (=> ocupamv_1_1_0 x_0_0))
(assert
 (let ((?x113 (ite ocupamf_1_1 1 0)))
 (let ((?x129 (+ (+ (ite ocupamv_1_1_0 1 0) (ite ocupamf_1_0 1 0)) ?x113)))
 (or (= ?x129 0) (= ?x129 1)))))
(assert
 (let ((?x113 (ite ocupamf_1_1 1 0)))
 (let ((?x110 (ite ocupamf_1_0 2 0)))
 (let ((?x127 (ite ocupamv_1_1_0 1 0)))
 (let ((?x141 (+ (+ (+ (+ (+ (ite ocupamv_1_0_0 1 0) ?x110) ?x113) ?x127) ?x110) ?x113)))
 (<= ?x141 2))))))
(assert
 (let ((?x70 (ite ocupamf_0_1 1 0)))
 (let ((?x67 (ite ocupamf_0_0 2 0)))
 (let ((?x148 (ite ocupamv_0_1_0 var_0_0_0 0)))
 (let ((?x152 (+ (+ (+ (+ (ite ocupamv_0_0_0 var_0_0_0 0) ?x67) ?x70) ?x148) ?x67)))
 (= (+ ?x152 ?x70) 12))))))
(assert
 (let ((?x113 (ite ocupamf_1_1 1 0)))
 (let ((?x110 (ite ocupamf_1_0 2 0)))
 (let ((?x159 (ite ocupamv_1_1_0 var_0_0_0 0)))
 (let ((?x163 (+ (+ (+ (+ (ite ocupamv_1_0_0 var_0_0_0 0) ?x110) ?x113) ?x159) ?x110)))
 (= (+ ?x163 ?x113) 12))))))
(assert
 (let (($x170 (and x_0_0 ocupamv_0_0_0)))
 (=> $x170 cuenta_0_0)))
(assert
 (let (($x170 (and x_0_0 ocupamv_0_0_0)))
 (=> cuenta_0_0 $x170)))
(assert
 (let (($x177 (and x_0_0 ocupamv_0_1_0)))
 (=> $x177 cuenta_0_0)))
(assert
 (let (($x177 (and x_0_0 ocupamv_0_1_0)))
 (=> cuenta_0_0 $x177)))
(assert
 (let (($x183 (and x_0_0 ocupamv_1_0_0)))
 (=> $x183 cuenta_0_0)))
(assert
 (let (($x183 (and x_0_0 ocupamv_1_0_0)))
 (=> cuenta_0_0 $x183)))
(assert
 (let (($x189 (and x_0_0 ocupamv_1_1_0)))
 (=> $x189 cuenta_0_0)))
(assert
 (let (($x189 (and x_0_0 ocupamv_1_1_0)))
 (=> cuenta_0_0 $x189)))
(assert
 (let ((?x169 (ite cuenta_0_0 1 0)))
(<= ?x169 2)))
(check-sat)
