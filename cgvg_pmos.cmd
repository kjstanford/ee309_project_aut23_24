# CFET-BEOL SRAM at 2nm --> Si PMOS sdevice simulations of Cg

Device NSFET {
	File {*input files
		Grid = "nanosheet_ns2_2D_PMOS_msh.tdr"
		Doping = "nanosheet_ns2_2D_PMOS_msh.tdr"
      	      *output files
		Plot = "nanosheet_ns2_2D_PMOS_cgvg_post.tdr"
		Current = "nanosheet_ns2_2D_PMOS_cgvg.plt"
		Parameter = "models.par"
	     }
   	      
	Electrode{
        {Name="Gate" Voltage=0.0 Workfunction=4.71}
        {Name="Drain" Voltage = 0.0}
        {Name="Source" Voltage = 0.0}
        }


	Physics (Material="Silicon"){
		Fermi
		EffectiveIntrinsicDensity( OldSlotboom )
        Mobility( DopingDep )
        Recombination( SRH( DopingDep ))
		}
	Physics (Material="Metal"){
	    MetalWorkfunction ( Workfunction=4.71 )
	}

	Plot {
		eDensity hDensity eCurrent hCurrent Potential 
		SpaceCharge ElectricField Doping DonorConcentration
		AcceptorConcentration ConductionBandEnergy ValenceBandEnergy
		eQuasiFermiPotential hQuasiFermiPotential
	     }
}

 Math {
 Extrapolate
 Iterations=20
 Notdamped=10
 RelErrControl}

File {
	Output = "nanosheet_cv.log"
	ACExtract = "ac_nanosheet_ns2_2D_PMOS"
     }
     
System { 
	# Mixed mode simulation

	# Insert code here
	NSFET fet_dut (Gate="G" Drain="D" Source="S")
	Vsource_pset vd ("D" 0) {dc = 0}
	Vsource_pset vg ("G" 0) {dc = 0}
	Vsource_pset vs ("S" 0) {dc = 0}
	}

Solve {
Poisson
Coupled{Poisson Electron Hole}
Save(FilePrefix="v0")

Quasistationary
( InitialStep=0.1 MaxStep=0.5 MinStep=0.001
Goal {Parameter=vd.dc value=0.7})
{ Coupled {Poisson Electron Hole}}
Save(FilePrefix="v1")

Quasistationary
( InitialStep=0.1 MaxStep=0.5 MinStep=0.001
Goal {Parameter=vs.dc value=0.7})
{ Coupled {Poisson Electron Hole}}
Save(FilePrefix="v2")

NewCurrentFile="main_"
Quasistationary
( InitialStep=0.025 MaxStep=0.025 MinStep=0.001
Goal {Parameter=vg.dc value=0.7})
{ACCoupled (StartFrequency=1.e4 EndFrequency=1.e4 NumberOfPoints=1 Decade
Node("G" "D" "S")
Exclude(vg vd vs)) {Poisson Electron Hole Circuit Contact}}
Save(FilePrefix="v3")

}