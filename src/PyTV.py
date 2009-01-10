#!/usr/bin/env python
'''PyTV: Python Text Viewer

Displays text.

Usage: PyTv.py [options]

Options:
   -f ..., --filename=...      load specified filename
   -l ..., --left-margin=...   set the left margin to the specified number of pixels
   -r ..., --right-margin=...  set the right margin to the specified number of pixels
'''
import codecs
import getopt
import gtk
import sys

class PyTV(object):
    
    def __init__(self, filename=None, left_margin=0, right_margin=0):
        self.filename = filename
        self.left_margin = left_margin
        self.right_margin = right_margin
        self.init_gui()
        if self.filename:
            self.load_file_into_buffer(self.filename, self.buffer)
        self.configure()
    
    def init_gui(self):
        self.window = gtk.Window()
        self.window.connect("destroy", self.destroy_event)
        self.vbox = gtk.VBox()

        self.buffer = gtk.TextBuffer()
        self.textView = gtk.TextView(buffer=self.buffer)

        
        scrolled = gtk.ScrolledWindow()
        scrolled.set_policy(
            gtk.POLICY_AUTOMATIC,
            gtk.POLICY_AUTOMATIC
            )
        scrolled.add_with_viewport(self.textView)

        self.vbox.pack_start(scrolled)
        self.window.add(self.vbox)
        self.window.show_all()

    def configure(self):
        self.textView.set_wrap_mode(gtk.WRAP_WORD)
        print self.left_margin
        self.textView.set_left_margin(self.left_margin)
        self.textView.set_right_margin(self.right_margin)

    def load_file_into_buffer(self, filename, buffer):
        infile = open(filename, "r")
        if infile:
            data = infile.read()
            data = unicode(data, errors='ignore')
            infile.close()
            buffer.set_text(data.encode('utf8'))
            

    ##########################
    #   Events
    ##########################
    def destroy_event(self, widget):
        gtk.main_quit()

###################################################
        
def usage():
    print __doc__

def main(argv):
    filename = None
    left_margin = 0
    right_margin = 0
    try:
        opts, args = getopt.getopt(argv, "f:l:r:", ["filename=", "left-margin=", "right-margin="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-l", "--left-margin"):
            left_margin = int(arg)
        elif opt in ("-l", "--right-margin"):
            rirght_margin = int(arg)
    pytv = PyTV(filename, left_margin, right_margin)
    gtk.main()


if __name__ == '__main__':
    main(sys.argv[1:])
        
