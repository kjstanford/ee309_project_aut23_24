load_file main_ac_nanosheet_ns2_2D_PMOS_ac_des.plt
create_plot -1d
select_plots {Plot_1}
create_curve -plot Plot_1 -dataset {main_ac_nanosheet_ns2_2D_PMOS_ac_des} -axisX {v(G)} -axisY {c(G,G)}
create_curve -plot Plot_1 -dataset {main_ac_nanosheet_ns2_2D_PMOS_ac_des} -axisX {v(G)} -axisY {c(D,G)}
create_curve -plot Plot_1 -dataset {main_ac_nanosheet_ns2_2D_PMOS_ac_des} -axisX {v(G)} -axisY {c(S,G)}
export_curves {Curve_1 Curve_2 Curve_3} -plot Plot_1 -filename ./csv_tcad_model/main_ac_nanosheet_ns2_2D_PMOS_ac_des.csv -format csv -overwrite
load_file main_ac_nanosheet_ns2_2D_NMOS_ac_des.plt
create_plot -1d
select_plots {Plot_1}
create_curve -plot Plot_1 -dataset {main_ac_nanosheet_ns2_2D_NMOS_ac_des} -axisX {v(G)} -axisY {c(G,G)}
create_curve -plot Plot_1 -dataset {main_ac_nanosheet_ns2_2D_NMOS_ac_des} -axisX {v(G)} -axisY {c(D,G)}
create_curve -plot Plot_1 -dataset {main_ac_nanosheet_ns2_2D_NMOS_ac_des} -axisX {v(G)} -axisY {c(S,G)}
export_curves {Curve_4 Curve_5 Curve_6} -plot Plot_1 -filename ./csv_tcad_model/main_ac_nanosheet_ns2_2D_NMOS_ac_des.csv -format csv -overwrite
exit