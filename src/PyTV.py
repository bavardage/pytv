#!/usr/bin/env python

import codecs
import getopt
import gtk
import sys

class PyTV(object):
    
    def __init__(self, filename=None):
        self.filename = filename
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
        
def usage():
    pass #print usage

def main(argv):
    filename = None
    try:
        opts, args = getopt.getopt(argv, "f:", ["filename=",])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-f", "--filename"):
            filename = arg
    pytv = PyTV(filename)
    gtk.main()


if __name__ == '__main__':
    main(sys.argv[1:])
        
