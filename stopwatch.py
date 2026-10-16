import tkinter as tk
from tkinter import ttk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("可视化秒表")
        self.running = False
        self.start_time = 0
        self.elapsed = 0
        self.label = ttk.Label(root, text="00:00:00.000", font=("Helvetica", 32))
        self.label.pack(pady=20)
        self.start_btn = ttk.Button(root, text="开始", command=self.start)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        self.pause_btn = ttk.Button(root, text="暂停", command=self.pause)
        self.pause_btn.pack(side=tk.LEFT, padx=10)
        self.reset_btn = ttk.Button(root, text="重置", command=self.reset)
        self.reset_btn.pack(side=tk.LEFT, padx=10)
        self.update()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed
            self.update()

    def pause(self):
        if self.running:
            self.running = False
            self.elapsed = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.start_time = 0
        self.label.config(text="00:00:00.000")

    def update(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
        ms = int((self.elapsed * 1000) % 1000)
        s = int(self.elapsed) % 60
        m = (int(self.elapsed) // 60) % 60
        h = (int(self.elapsed) // 3600)
        self.label.config(text=f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}")
        self.root.after(50, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    Stopwatch(root)
    root.mainloop()
