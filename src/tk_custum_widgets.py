#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
def create_textbox(root, values, **kwargs):
        """Creates and Grids A Combobox"""
        box = ttk.Combobox(root, values=values, **kwargs)
        box.set(values[0])
        return box

class TKConsole(tk.Frame):
    def __init__(self, parent, dovsb=True, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.text = tk.Text(self, *args, **kwargs)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.hsb = tk.Scrollbar(self, orient="horizontal", command=self.text.xview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.configure(xscrollcommand=self.hsb.set)
        if dovsb: self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.text.pack(side="left", fill="x", expand=True)

        # expose some text methods as methods on this object
        self.insert = self._insert
        self.delete = self.text.delete
        self.get = self.text.get
        self.bind = self.text.bind
        self.config = self.text.config
        self.pprint = self._pprint
        
    def _insert(self, pos, text, sep="\n", *args, **kwargs):
        self.text.insert(pos, f"{sep}{text}", *args, **kwargs)
        self.text.tag_configure("white", foreground="white")
        self.text.tag_add("white", "1.0", "end")    
        self.text.see("end-4c")
    
    
    def _pprint(self, text_raw, suffix="", *args, **kwargs):
        """Prettier Printing"""
        text = ""
        if isinstance(text_raw, list):
            for item in text_raw:
                text = f"{text}{item}\n"
        elif isinstance(text_raw, dict):
            for key, value in text_raw.items():
                text = f"{text}{key} - {value}\n"
        else:
            text = text_raw
        self._insert("end", text, *args, **kwargs)
        
class ScrolledFrame(tk.Frame):
    # !!! FROM stackoverflow.com !!! #
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)