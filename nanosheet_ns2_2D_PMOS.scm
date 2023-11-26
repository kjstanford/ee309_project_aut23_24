(sde:clear)

(define file_name "nanosheet_ns2_2D_PMOS")
(define tgm 0.010)
(define tgox 0.0008)
(define tghk 0.0005)
(define tsh 0.007)
(define cgp 0.042)
(define lsp 0.005)
(define Nsd 1e21)
(define Next 1e17)
(define Nch 1e16)
(define lg 0.014)

(define lc (- cgp (+ lg lsp lsp)))
(define ltot (+ lg lsp lsp lc lc))
(define lcsp (+ lc lsp))
(define ttot (+ (* (+ tsh tgox tgox tghk tghk tgm) 2)  tgm))
(define tstep (+ tsh tgox tgox tghk tghk tgm))
(define tc1 0)
(define tc2 (* ttot 0.5))
(define tc3 ttot)

(define A (sdegeo:create-rectangle (position 0 lcsp 0) (position ttot (- ltot lcsp) 0) "Metal" "GMA"))
(define B1 (sdegeo:create-rectangle (position tgm lcsp 0) (position (- ttot (+ tstep tgm)) (- ltot lcsp) 0) "Metal" "GMB1"))
(define B2 (sdegeo:create-rectangle (position (+ tgm tstep) lcsp 0) (position (- ttot tgm) (- ltot lcsp) 0) "Metal" "GMB2"))
(sdegeo:bool-subtract (list A B1 B2))
(define A (sdegeo:create-rectangle (position tc2 lcsp 0) (position (+ tstep tgm) (- ltot lcsp) 0) "Metal" "GMmid"))

(define A (sdegeo:create-rectangle (position tgm lcsp 0) (position (- ttot (+ tstep tgm)) (- ltot lcsp) 0) "HfO2" "GHKA1"))
(define B (sdegeo:create-rectangle (position (+ tgm tghk) lcsp 0) (position (- ttot (+ tstep tgm) tghk) (- ltot lcsp) 0) "HfO2" "GHKB1"))
(sdegeo:bool-subtract (list A B))
(define A (sdegeo:create-rectangle (position (+ tgm tstep) lcsp 0) (position (- ttot  tgm) (- ltot lcsp) 0) "HfO2" "GHKA2"))
(define B (sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk) lcsp 0) (position (- ttot tgm tghk) (- ltot lcsp) 0) "HfO2" "GHKB2"))
(sdegeo:bool-subtract (list A B))

(define A (sdegeo:create-rectangle (position (+ tgm tghk) lcsp 0) (position (- ttot (+ tstep tgm) tghk) (- ltot lcsp) 0) "Oxide" "GOXA1"))
(define B (sdegeo:create-rectangle (position (+ tgm tghk tgox) lcsp 0) (position (- ttot (+ tstep tgm) tghk tgox) (- ltot lcsp) 0) "Oxide" "GOXB1"))
(sdegeo:bool-subtract (list A B))
(define A (sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk) lcsp 0) (position (- ttot tgm tghk) (- ltot lcsp) 0) "Oxide" "GOXA2"))
(define B (sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk tgox) lcsp 0) (position (- ttot tgm tghk tgox) (- ltot lcsp) 0) "Oxide" "GOXB2"))
(sdegeo:bool-subtract (list A B))

(sdegeo:create-rectangle (position (+ tgm tghk tgox) lcsp 0) (position (- ttot (+ tstep tgm) tghk tgox) (- ltot lcsp) 0) "Silicon" "CH1")
(sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk tgox) lcsp 0) (position (- ttot tgm tghk tgox) (- ltot lcsp) 0) "Silicon" "CH2")

(define A (sdegeo:create-rectangle (position 0 lc 0) (position ttot lcsp 0) "Oxide" "SPSOXA"))
(define B1 (sdegeo:create-rectangle (position (+ tgm tghk tgox) lc 0) (position (- ttot (+ tgm tstep) tghk tgox) lcsp 0) "Oxide" "SPSOXB1"))
(define B2 (sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk tgox) lc 0) (position (- ttot tgm tghk tgox) lcsp 0) "Oxide" "SPSOXB2"))
(sdegeo:bool-subtract (list A B1 B2))

(define A (sdegeo:create-rectangle (position 0 (- ltot lcsp) 0) (position ttot (- ltot lc) 0) "Oxide" "SPDOXA"))
(define B1 (sdegeo:create-rectangle (position (+ tgm tghk tgox) (- ltot lcsp) 0) (position (- ttot (+ tgm tstep) tghk tgox) (- ltot lc) 0) "Oxide" "SPDOXB1"))
(define B2 (sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk tgox) (- ltot lcsp) 0) (position (- ttot tgm tghk tgox) (- ltot lc) 0) "Oxide" "SPDOXB2"))
(sdegeo:bool-subtract (list A B1 B2))

(sdegeo:create-rectangle (position (+ tgm tghk tgox) lc 0) (position (- ttot (+ tgm tstep) tghk tgox) lcsp 0) "Silicon" "SPS1")
(sdegeo:create-rectangle (position (+ tgm tghk tgox) (- ltot lcsp) 0) (position (- ttot (+ tgm tstep) tghk tgox) (- ltot lc) 0) "Silicon" "SPD1")
(sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk tgox) lc 0) (position (- ttot tgm tghk tgox) lcsp 0) "Silicon" "SPS2")
(sdegeo:create-rectangle (position (+ (+ tgm tstep) tghk tgox) (- ltot lcsp) 0) (position (- ttot tgm tghk tgox) (- ltot lc) 0) "Silicon" "SPD2")

(sdegeo:create-rectangle (position 0 0 0) (position ttot lc 0) "Silicon" "CS")
(sdegeo:create-rectangle (position 0 (- ltot lc) 0) (position ttot ltot 0) "Silicon" "CD")

(sdedr:define-refeval-window "RW_All" "Rectangle" (position 0 0 0) (position ttot ltot 0))
(sdedr:define-refeval-window "RW_NS" "Rectangle" (position 0 0 0) (position ttot lc 0))
(sdedr:define-refeval-window "RW_ND" "Rectangle" (position 0 (- ltot lc) 0) (position ttot ltot 0))
(sdedr:define-refeval-window "RW_Mid1" "Rectangle" (position tgm 0 0) (position (- ttot (+ tstep tgm)) (- ltot 0) 0))
(sdedr:define-refeval-window "RW_Mid2" "Rectangle" (position (+ tgm tstep) 0 0) (position (- ttot tgm) (- ltot 0) 0))
(sdedr:define-refeval-window "RW_CH1" "Rectangle" (position tgm lcsp 0) (position (- ttot (+ tstep tgm)) (- ltot lcsp) 0))
(sdedr:define-refeval-window "RW_CH2" "Rectangle" (position (+ tgm tstep) lcsp 0) (position (- ttot tgm) (- ltot lcsp) 0))
(sdedr:define-refeval-window "RW_Next11" "Rectangle" (position tgm lc 0) (position (- ttot (+ tstep tgm)) lcsp 0))
(sdedr:define-refeval-window "RW_Next12" "Rectangle" (position tgm (- ltot lcsp) 0) (position (- ttot (+ tstep tgm)) (- ltot lc) 0))
(sdedr:define-refeval-window "RW_Next21" "Rectangle" (position (+ tgm tstep) lc 0) (position (- ttot tgm) lcsp 0))
(sdedr:define-refeval-window "RW_Next22" "Rectangle" (position (+ tgm tstep) (- ltot lcsp) 0) (position (- ttot tgm) (- ltot lc) 0))

(sdedr:define-constant-profile "Dop_NS" "BoronActiveConcentration" Nsd)
(sdedr:define-constant-profile-placement "Dop_PL_NS" "Dop_NS" "RW_NS")
(sdedr:define-constant-profile "Dop_ND" "BoronActiveConcentration" Nsd)
(sdedr:define-constant-profile-placement "Dop_PL_ND" "Dop_ND" "RW_ND")
(sdedr:define-constant-profile "Dop_NCH1" "ArsenicActiveConcentration" Nch)
(sdedr:define-constant-profile-placement "Dop_PL_NCH1" "Dop_NCH1" "RW_CH1")
(sdedr:define-constant-profile "Dop_NCH2" "ArsenicActiveConcentration" Nch)
(sdedr:define-constant-profile-placement "Dop_PL_NCH2" "Dop_NCH2" "RW_CH2")
(sdedr:define-constant-profile "Dop_Next11" "BoronActiveConcentration" Next)
(sdedr:define-constant-profile-placement "Dop_PL_Next11" "Dop_Next11" "RW_Next11")
(sdedr:define-constant-profile "Dop_Next12" "BoronActiveConcentration" Next)
(sdedr:define-constant-profile-placement "Dop_PL_Next12" "Dop_Next12" "RW_Next12")
(sdedr:define-constant-profile "Dop_Next21" "BoronActiveConcentration" Next)
(sdedr:define-constant-profile-placement "Dop_PL_Next21" "Dop_Next21" "RW_Next21")
(sdedr:define-constant-profile "Dop_Next22" "BoronActiveConcentration" Next)
(sdedr:define-constant-profile-placement "Dop_PL_Next22" "Dop_Next22" "RW_Next22")


(sdegeo:set-contact (list (car (find-edge-id (position tc1 (/ ltot 2) 0))) (car (find-edge-id (position tc2 (/ ltot 2) 0))) (car (find-edge-id (position tc3 (/ ltot 2) 0)))) "Gate")
(sdegeo:set-contact (find-edge-id (position 0 (/ lc 2) 0)) "Source")
(sdegeo:set-contact (find-edge-id (position 0 (- ltot (/ lc 2)) 0)) "Drain")

(sdedr:define-refinement-size "Msh_All" 0.002 0.005 0.001 0.001 )
(sdedr:define-refinement-placement "Msh_PL_All" "Msh_All" "RW_All" )
(sdedr:define-refinement-size "Msh_Mid1" 0.001 0.001 0.001 0.001 )
(sdedr:define-refinement-placement "Msh_PL_Mid1" "Msh_Mid1" "RW_Mid1" )
(sdedr:define-refinement-size "Msh_CH1" 0.001 0.001 0.001 0.001 ) 
(sdedr:define-refinement-placement "Msh_PL_CH1" "Msh_CH1" "RW_CH1" )
(sdedr:define-refinement-size "Msh_Mid2" 0.001 0.001 0.001 0.001 )
(sdedr:define-refinement-placement "Msh_PL_Mid2" "Msh_Mid2" "RW_Mid2" )
(sdedr:define-refinement-size "Msh_CH2" 0.001 0.001 0.001 0.001 )
(sdedr:define-refinement-placement "Msh_PL_CH2" "Msh_CH2" "RW_CH2" )

(sde:build-mesh "mesh" "-d" file_name)
