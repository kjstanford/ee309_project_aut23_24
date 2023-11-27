from os import system as sys
import fileinput as fi
from numpy.core.multiarray import dtype
import numpy as np
import pandas as pd
import scipy.linalg as la
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from numpy import pi, exp, log, sin, cos, tan, log10, abs, gradient, sinh, cosh, arctan
from scipy.special import hyp2f1, erf, erfc, erfcinv, gammainc
from scipy.optimize import fsolve
from scipy.signal import savgol_filter
from scipy import sparse
from scipy.sparse import linalg as las
from math import ceil, floor
import time
import csv
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

import os
from multiprocessing import Pool

def multiple_workers(foo, inputs):
    pool = Pool(processes=24)
    outputs = pool.map(foo, inputs)
    return outputs

# constants
kB = 8.617e-5 #eV/K
q = 1.6e-19 #C
mo = 9.11e-31 #kg
hred = 1.054571817e-34
h = hred*2*pi
epso = 8.85e-12

# plotting section
SMALL_SIZE = 22
MEDIUM_SIZE = 26
BIGGER_SIZE = 32

plt.rc('font', size=SMALL_SIZE, weight='bold')          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rcParams["figure.figsize"] = (12, 10)
plt.rcParams['axes.linewidth'] = 2.5
# plt.rc('text', usetex=True)
# plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]


def lin_plot(x, y, c, s, mask=[True], m=[None], l=[None], xlim=0, ylim=0, lw=2.0, xlabel='', ylabel='', title='', figname='temp.png'):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        if mask[i%len(mask)]:
            ax.plot(x[i], y[i], linewidth=lw, marker=m[i%len(m)], color=c[i%len(c)], linestyle=s[i%len(s)], markersize=12)
    # ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xlabel(xlabel=xlabel, fontweight='bold')
    plt.ylabel(ylabel=ylabel, fontweight='bold')
    plt.title(label=title, fontweight='bold')
    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())
    
    labels = ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax.minorticks_on()
    ax.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    
    if not l == [None]:
        ax.legend(l)
    if not xlim == 0:
        ax.set(xlim=xlim)
    if not ylim == 0:
        ax.set(ylim=ylim)
    # plt.figure(figsize=(1,1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

def lin_plot(x, y, c, s, mask=[True], m=[None], l=[None], xlim=0, ylim=0, lw=2.0, xlabel='', ylabel='', title='', figname='temp.png', ms=12):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        if mask[i%len(mask)]:
            ax.plot(x[i], y[i], linewidth=lw, marker=m[i%len(m)], color=c[i%len(c)], linestyle=s[i%len(s)], markersize=ms)
    # ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xlabel(xlabel=xlabel, fontweight='bold')
    plt.ylabel(ylabel=ylabel, fontweight='bold')
    plt.title(label=title, fontweight='bold')
    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())
    labels = ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax.minorticks_on()
    ax.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    if not l == [None]:
        ax.legend(l)
    if not xlim == 0:
        ax.set(xlim=xlim)
    if not ylim == 0:
        ax.set(ylim=ylim)
    # plt.figure(figsize=(1,1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

def logx_plot(x, y, c, s, mask=[True], m=[None], l=[None], cmap=False, xlim=0, ylim=0, lw=2.0, xlabel='', ylabel='', title='', figname='temp.png', ms=12):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        if mask[i%len(mask)]:
            ax.semilogx(x[i], y[i], linewidth=lw, marker=m[i%len(m)], color=c[i%len(c)], linestyle=s[i%len(s)], markersize=ms)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    # ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xlabel(xlabel=xlabel, fontweight='bold')
    plt.ylabel(ylabel=ylabel, fontweight='bold')
    plt.title(label=title, fontweight='bold')
    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())
    labels = ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax.minorticks_on()
    ax.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    if not l == [None]:
        ax.legend(l)
    if not xlim == 0:
        ax.set(xlim=xlim)
    if not ylim == 0:
        ax.set(ylim=ylim)
    # plt.figure(figsize=(1, 1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

def logy_plot(x, y, c, s, mask=[True], m=[None], l=[None], cmap=False, xlim=0, ylim=0, lw=2.0, xlabel='', ylabel='', title='', figname='temp.png', ms=12):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        if mask[i%len(mask)]:
            ax.semilogy(x[i], y[i], linewidth=lw, marker=m[i%len(m)], color=c[i%len(c)], linestyle=s[i%len(s)], markersize=ms)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    # ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xlabel(xlabel=xlabel, fontweight='bold')
    plt.ylabel(ylabel=ylabel, fontweight='bold')
    plt.title(label=title, fontweight='bold')
    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())
    labels = ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax.minorticks_on()
    ax.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    if not l == [None]:
        ax.legend(l)
    if not xlim == 0:
        ax.set(xlim=xlim)
    if not ylim == 0:
        ax.set(ylim=ylim)
    # plt.figure(figsize=(1, 1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

def logy_lin_plot(x, y, c, s, mask=[True], m=[None], l=[None], cmap=False, xlim=0, ylim=0, lw=2.0, xlabel='', ylabel='', title='', figname='temp.png', ms=12):
    fig, ax = plt.subplots()
    ax_twin = ax.twinx()
    for i in range(len(x)):
        if mask[i%len(mask)]:
            ax.semilogy(x[i], y[i], linewidth=lw, marker=m[i%len(m)], color=c[i%len(c)], linestyle=s[i%len(s)], markersize=ms)
            ax_twin.plot(x[i], y[i], linewidth=lw, marker=m[i%len(m)], color=c[i%len(c)], linestyle=s[i%len(s)], markersize=ms)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax_twin.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xlabel(xlabel=xlabel, fontweight='bold')
    plt.ylabel(ylabel=ylabel, fontweight='bold')
    plt.title(label=title, fontweight='bold')
    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())
    labels = ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax.minorticks_on()
    labels = ax_twin.xaxis.get_ticklabels() + ax_twin.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax_twin.minorticks_on()
    # ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=(0.2, 0.4, 0.6, 0.8), numticks=5))
    plt.tick_params(axis='y', which='minor')
    ax.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    ax_twin.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax_twin.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    if not l == [None]:
        ax.legend(l)
    if not xlim == 0:
        ax.set(xlim=xlim)
    if not ylim == 0:
        ax.set(ylim=ylim)
    # plt.figure(figsize=(1,1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

def lin_lin_plot(x1, y1, x2, y2, c1, c2, s1, s2, mask=[True], m1=[None], m2=[None], l=[None], cmap=False, xlim=0, ylim=0, lw=2.0, xlabel='', ylabel='', title='', figname='temp1.png'):
    fig, ax = plt.subplots()
    ax_twin = ax.twinx()
    for i in range(len(x1)):
        if mask[i%len(mask)]:
            ax.plot(x1[i], y1[i], linewidth=lw, marker=m1[i%len(m1)], color=c1[i%len(c1)], linestyle=s1[i%len(s1)], markersize=12)
    
    for i in range(len(x2)):
        if mask[i%len(mask)]:
            ax_twin.plot(x2[i], y2[i], linewidth=lw, marker=m1[i%len(m1)], color=c1[i%len(c1)], linestyle=s2[i%len(s2)], markersize=12)

    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax_twin.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xlabel(xlabel=xlabel, fontweight='bold')
    plt.ylabel(ylabel=ylabel, fontweight='bold')
    plt.title(label=title, fontweight='bold')
    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())
    labels = ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax.minorticks_on()
    labels = ax_twin.xaxis.get_ticklabels() + ax_twin.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax_twin.minorticks_on()
    # ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=(0.2, 0.4, 0.6, 0.8), numticks=5))
    plt.tick_params(axis='y', which='minor')
    ax.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    ax_twin.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax_twin.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    if not l == [None]:
        ax.legend(l)
    if not xlim == 0:
        ax.set(xlim=xlim)
    if not ylim == 0:
        ax.set(ylim=ylim)
    # plt.figure(figsize=(1,1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

# helper functions
def sf(y, wl=31, order=3):  # smoothing linear curves
    yhat = []
    for i in range(len(y)):
        yhat.append(savgol_filter(y[i], window_length=wl, polyorder=order))
    return yhat


def sf_log10(y, wl=31, order=3):  # smoothing logy curves
    yhat = []
    for i in range(len(y)):
        yhat.append(savgol_filter(np.log10(np.abs(y[i])), window_length=wl, polyorder=order))
    return [10 ** yy for yy in yhat]


def agilent_csv_cleaner(fname):
    full_data_set = []
    with open(fname, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            # print(line_count, row)
            if row[0] in ['Dimension1', 'Dimension2', 'DataName', 'DataValue']:
                full_data_set.append(row)
            line_count += 1
    print(f'Processed {line_count} lines')

    line_count = 0
    data_set = []
    N1 = 0
    N2 = 0
    while line_count < len(full_data_set):
        row = full_data_set[line_count]
        if row[0] == 'Dimension1':
            N1 = int(row[1])
            print('Dimension1:', N1)
            line_count += 1
            row = full_data_set[line_count]
            N2 = int(row[1])
            print('Dimension2:', N2)
            line_count += 1
            temp_data = [[[str(X) for X in full_data_set[line_count][1:9]]] for ii in range(N2)]
            line_count += 1
            for ii in range(N2):
                for elem in range(N1):
                    # print(full_data_set[line_count])
                    temp_data[ii].append([float(X) for X in full_data_set[line_count][1:9]])
                    line_count += 1
            data_set += temp_data
    print(f'Number of datasets: {len(data_set)}')

    pd_data_set = [pd.DataFrame(X[1:], columns=X[0]) for X in data_set]

    return pd_data_set, N1


def vth_calc(Vg, Id, vt_i):
    for i in range(len(Vg)):
        if Id[i] >= vt_i:
            break
    idxl = i

    return Vg[idxl - 1] + (Vg[idxl] - Vg[idxl - 1]) * (log10(vt_i) - log10(Id[idxl - 1])) / (
                log10(Id[idxl]) - log10(Id[idxl - 1]))

def keithley_reader_xls(fname):
    # sname = lambda i: 'Data' if i == 0 else f'Append{i}'
    sname = lambda i: 'Data' if i == 0 else f'Cycle{i+1}'
    df_sheet_all = pd.read_excel(fname, sheet_name=None)
    i = 0
    pd_data_set = []
    while sname(i) in df_sheet_all:
        pd_data_set.append(df_sheet_all[sname(i)])
        i += 1
    return pd_data_set

def SS_calc(Vg, Id, lower_i, higher_i):
    for i in range(int(len(Vg)/2)):
        if Id[i] >= lower_i: #lower limit
            break
    idxl = i
    for i in range(int(len(Vg)/2)):
        if Id[i] >= higher_i: # higher limit for SS extraction
            break
    idxu = i
    print(Id[idxl], Id[idxu])
    return (Vg[idxu] - Vg[idxl])*1e3/(log10(Id[idxu]) - log10(Id[idxl]))

def read_lis(fname):
    lines = list(fi.input(files = fname))

    line_num = 0
    first_word = lines[line_num].split()
    first_word = None if len(first_word) == 0 else first_word[0]
    acq_start = 0
    acq_list = []
    while first_word != 'y':
        if acq_start == 1:
            acq_list.append(lines[line_num].split())
        if first_word == 'time':
            line_num += 2
            acq_start = 1
        else:
            line_num += 1
        first_word = lines[line_num].split()
        first_word = None if len(first_word) == 0 else first_word[0]

    time_acq_list = np.array([ float(x[0]) for x in acq_list ])
    vsn_acq_list = np.array([ float(x[1]) for x in acq_list ])
    vwbl_acq_list = np.array([ float(x[2]) for x in acq_list ])
    vwwl_acq_list = np.array([ float(x[3]) for x in acq_list ])
    vrwl_acq_list = np.array([ float(x[4]) for x in acq_list ])
    
    return time_acq_list, vsn_acq_list, vwwl_acq_list, vwbl_acq_list, vrwl_acq_list

def read_lis_iv(fname):
    lines = list(fi.input(files = fname))

    line_num = 0
    first_word = lines[line_num].split()
    first_word = None if len(first_word) == 0 else first_word[0]
    acq_start = 0
    acq_list = []
    while first_word != 'y':
        if acq_start == 1:
            acq_list.append(lines[line_num].split())
        if first_word == 'vgate':
            line_num += 2
            acq_start = 1
        else:
            line_num += 1
        first_word = lines[line_num].split()
        first_word = None if len(first_word) == 0 else first_word[0]

    vg_acq_list = np.array([ float(x[0]) for x in acq_list ])
    id_acq_list = np.array([ float(x[1]) for x in acq_list ])

    return vg_acq_list, id_acq_list

def read_lis_cv(fname):
    lines = list(fi.input(files = fname))

    line_num = 0
    first_word = lines[line_num].split()
    first_word = None if len(first_word) == 0 else first_word[0]
    acq_start = 0
    acq_list = []
    while first_word != 'y':
        if acq_start == 1:
            acq_list.append(lines[line_num].split())
        if first_word == 'time':
            line_num += 2
            acq_start = 1
        else:
            line_num += 1
        first_word = lines[line_num].split()
        first_word = None if len(first_word) == 0 else first_word[0]

    vg_acq_list = np.array([ float(x[2]) for x in acq_list ])
    id_acq_list = np.array([ float(x[1]) for x in acq_list ])

    return vg_acq_list, id_acq_list

def generate_spice_netlist(fname, params):
    i_lines = list(fi.input(files = fname+'_template.sp'))
    o_lines = []

    for line in i_lines:
        line_list = line.split()
        if len(line_list) == 4:
            if line_list[0] == ".PARAM" and line_list[3][0]=='@':
                line_list[3] = str(params[line_list[1]])
        if len(line_list) > 1:
            if line_list[0] == '*out*':
                line_list[0] = ''
                if params['out_mode'] == 1:
                    line_list[2] = 'I(vrb)'
            if params['gc_mode'] == 0:
                if line_list[0] == '*ww*' or line_list[0] == '*wb*' or line_list[0] == '*rwd*':
                    line_list[0] = ''
            if params['gc_mode'] == 1:
                if line_list[0] == '*wwd*' or line_list[0] == '*wbd*' or line_list[0] == '*rwd*':
                    line_list[0] = ''
            if params['gc_mode'] == 2:
                if line_list[0] == '*wwd*' or line_list[0] == '*wbd*' or line_list[0] == '*rw*':
                    line_list[0] = ''  
        o_lines.append(' '.join(line_list))

    # print(o_lines)
    with open(fname+'.sp', 'w') as fp:
        fp.write('\n'.join(o_lines))
    fp.close()