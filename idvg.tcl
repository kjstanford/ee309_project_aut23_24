load_file main_m0p01_fet_dut_nanosheet_ns2_2D_PMOS_idvg.plt
create_plot -1d
select_plots {Plot_1}
create_curve -plot Plot_1 -dataset {main_m0p01_fet_dut_nanosheet_ns2_2D_PMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Drain TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p01_fet_dut_nanosheet_ns2_2D_PMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Source TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p01_fet_dut_nanosheet_ns2_2D_PMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Gate TotalCurrent}
export_curves {Curve_1 Curve_2 Curve_3} -plot Plot_1 -filename ./csv_tcad_model/main_m0p01_fet_dut_nanosheet_ns2_2D_PMOS_idvg.csv -format csv -overwrite
load_file main_m0p7_fet_dut_nanosheet_ns2_2D_PMOS_idvg.plt
create_plot -1d
select_plots {Plot_1}
create_curve -plot Plot_1 -dataset {main_m0p7_fet_dut_nanosheet_ns2_2D_PMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Drain TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p7_fet_dut_nanosheet_ns2_2D_PMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Source TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p7_fet_dut_nanosheet_ns2_2D_PMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Gate TotalCurrent}
export_curves {Curve_1 Curve_2 Curve_3} -plot Plot_1 -filename ./csv_tcad_model/main_m0p7_fet_dut_nanosheet_ns2_2D_PMOS_idvg.csv -format csv -overwrite
load_file main_m0p01_fet_dut_nanosheet_ns2_2D_NMOS_idvg.plt
create_plot -1d
select_plots {Plot_1}
create_curve -plot Plot_1 -dataset {main_m0p01_fet_dut_nanosheet_ns2_2D_NMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Drain TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p01_fet_dut_nanosheet_ns2_2D_NMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Source TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p01_fet_dut_nanosheet_ns2_2D_NMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Gate TotalCurrent}
export_curves {Curve_1 Curve_2 Curve_3} -plot Plot_1 -filename ./csv_tcad_model/main_m0p01_fet_dut_nanosheet_ns2_2D_NMOS_idvg.csv -format csv -overwrite
load_file main_m0p7_fet_dut_nanosheet_ns2_2D_NMOS_idvg.plt
create_plot -1d
select_plots {Plot_1}
create_curve -plot Plot_1 -dataset {main_m0p7_fet_dut_nanosheet_ns2_2D_NMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Drain TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p7_fet_dut_nanosheet_ns2_2D_NMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Source TotalCurrent}
create_curve -plot Plot_1 -dataset {main_m0p7_fet_dut_nanosheet_ns2_2D_NMOS_idvg} -axisX {Gate OuterVoltage} -axisY {Gate TotalCurrent}
export_curves {Curve_1 Curve_2 Curve_3} -plot Plot_1 -filename ./csv_tcad_model/main_m0p7_fet_dut_nanosheet_ns2_2D_NMOS_idvg.csv -format csv -overwrite
exit