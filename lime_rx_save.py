#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lime RX - SAVE TO FILE
# Author: U.A. (c) 2020
# Generated: Thu Jun 11 13:27:28 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from datetime import datetime
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import limesdr
import sip
import sys
from gnuradio import qtgui


class lime_rx_save(gr.top_block, Qt.QWidget):

    def __init__(self, CF=1147, sample_rate=20, path="/media/admin_k41/09a3c2ca-b1d8-4539-9e36-fde4ac33526b/output"):
        gr.top_block.__init__(self, "Lime RX - SAVE TO FILE")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lime RX - SAVE TO FILE")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "lime_rx_save")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Parameters
        ##################################################
        self.CF = CF
        self.sample_rate = sample_rate
        self.path = path

        ##################################################
        # Variables
        ##################################################
        self.window = window = 2048*3
        self.variable_qtgui_label_1 = variable_qtgui_label_1 = CF
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = sample_rate
        #self.filename = filename = path + "/" + datetime.now().strftime("%H.%M.%S_%Y.%m.%d_freq_") + str(CF) + "_short.bin"
        self.filename = filename = path
        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_label_1_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_1_formatter = None
        else:
          self._variable_qtgui_label_1_formatter = lambda x: str(x)

        self._variable_qtgui_label_1_tool_bar.addWidget(Qt.QLabel('\xd0\x9d\xd0\xb5\xd1\x81\xd1\x83\xd1\x89\xd0\xb0\xd1\x8f \xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xbe\xd1\x82\xd0\xb0 (\xd0\x9c\xd0\x93\xd1\x86)'+": "))
        self._variable_qtgui_label_1_label = Qt.QLabel(str(self._variable_qtgui_label_1_formatter(self.variable_qtgui_label_1)))
        self._variable_qtgui_label_1_tool_bar.addWidget(self._variable_qtgui_label_1_label)
        self.top_layout.addWidget(self._variable_qtgui_label_1_tool_bar)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xbe\xd1\x81\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f (\xd0\x9c\xd0\x93\xd1\x86, MSps)'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	window, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	CF*1000000, #fc
        	sample_rate*1000000, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.09)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	window, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	CF*1000000, #fc
        	sample_rate*1000000, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.limesdr_source_0 = limesdr.source('', 0, '')
        self.limesdr_source_0.set_sample_rate(sample_rate*1000000)
        self.limesdr_source_0.set_center_freq(CF*1000000, 0)
        self.limesdr_source_0.set_bandwidth(sample_rate*1000000,0)
        self.limesdr_source_0.set_gain(70,0)
        self.limesdr_source_0.set_antenna(1,0)
        self.limesdr_source_0.calibrate(sample_rate*1000000, 0)

        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((100000, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((100000, ))
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 1)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_short*1, filename, False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_imag_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_interleave_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_float_to_short_0_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lime_rx_save")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_CF(self):
        return self.CF

    def set_CF(self, CF):
        self.CF = CF
        self.set_filename(self.path + "/" + datetime.now().strftime("%H.%M.%S_%Y.%m.%d_freq_") + str(self.CF) + "_short.bin")
        self.set_variable_qtgui_label_1(self._variable_qtgui_label_1_formatter(self.CF))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.CF*1000000, self.sample_rate*1000000)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.CF*1000000, self.sample_rate*1000000)
        self.limesdr_source_0.set_center_freq(self.CF*1000000, 0)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.sample_rate))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.CF*1000000, self.sample_rate*1000000)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.CF*1000000, self.sample_rate*1000000)
        self.limesdr_source_0.set_bandwidth(self.sample_rate*1000000,0)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_filename(self.path + "/" + datetime.now().strftime("%H.%M.%S_%Y.%m.%d_freq_") + str(self.CF) + "_short.bin")

    def get_window(self):
        return self.window

    def set_window(self, window):
        self.window = window

    def get_variable_qtgui_label_1(self):
        return self.variable_qtgui_label_1

    def set_variable_qtgui_label_1(self, variable_qtgui_label_1):
        self.variable_qtgui_label_1 = variable_qtgui_label_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_1_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_1))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0_0.open(self.filename)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-f", "--CF", dest="CF", type="eng_float", default=eng_notation.num_to_str(1147),
        help="Set CF [default=%default]")
    parser.add_option(
        "-s", "--sample-rate", dest="sample_rate", type="eng_float", default=eng_notation.num_to_str(20),
        help="Set sample_rate [default=%default]")
    parser.add_option(
        "-p", "--path", dest="path", type="string", default="/media/admin_k41/09a3c2ca-b1d8-4539-9e36-fde4ac33526b/output",
        help="Set path [default=%default]")
    return parser


def main(top_block_cls=lime_rx_save, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(CF=options.CF, sample_rate=options.sample_rate, path=options.path)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
