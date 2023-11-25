# CFET-BEOL SRAM at 2nm --> Si NMOS sdevice simulations of transfer curve at 0.01V and 0.7V |V_DS| 

Device NSFET {
	File {*input files
		Grid = "nanosheet_ns2_2D_NMOS_msh.tdr"
		Doping = "nanosheet_ns2_2D_NMOS_msh.tdr"
      	      *output files
		Plot = "nanosheet_ns2_2D_NMOS_idvg_post.tdr"
		Current = "nanosheet_ns2_2D_NMOS_idvg.plt"
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
	Output = "nanosheet_2D_iv.log"
	# ACExtract = "ac_nanosheet_ns2_2D_NMOS"
     }
     
System { 
	# Mixed mode simulation

	# Insert code here
	NSFET fet_dut (Gate="G" Drain="D" Source="S")
	Vsource_pset vds ("D" "S") {dc = 0}
	Vsource_pset vgs ("G" "S") {dc = 0}
	Vsource_pset to_ground ("S" 0) {dc = 0}
	}

Solve {
Poisson
Coupled{Poisson Electron Hole}
Save(FilePrefix="v0")

Quasistationary
( InitialStep=0.1 MaxStep=0.5 MinStep=0.001
Goal {Parameter=vds.dc value=0.01})
{ Coupled {Poisson Electron Hole}}
Save(FilePrefix="v1")

Quasistationary
( InitialStep=0.1 MaxStep=0.5 MinStep=0.001
Goal {Parameter=vds.dc value=0.7})
{ Coupled {Poisson Electron Hole}}
Save(FilePrefix="v2")

Load(FilePrefix="v1")
NewCurrentFile="main_m0p01_"
Quasistationary
( InitialStep=0.025 MaxStep=0.025 MinStep=0.001
Goal {Parameter=vgs.dc value=0.7})
{ Coupled {Poisson Electron Hole}}
Save(FilePrefix="v3")

Load(FilePrefix="v2")
NewCurrentFile="main_m0p7_"
Quasistationary
( InitialStep=0.025 MaxStep=0.025 MinStep=0.001
Goal {Parameter=vgs.dc value=0.7})
{ Coupled {Poisson Electron Hole}}
Save(FilePrefix="v4")

}