for label in labels:
            frame = tk.Frame(self.principal)
            frame.pack(pady=5)
            tk.Label(frame, text=label, width=20, anchor="w").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT, padx=10)
            entries[label] = entry


